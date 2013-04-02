from __future__ import absolute_import, division, print_function, unicode_literals

import threading

import echomesh.color.Light

from echomesh.base import Config
from echomesh.element import Element
from echomesh.element import Scene
from echomesh.element import Sequence
from echomesh.expression import Units
from echomesh.util import Log

LOGGER = Log.logger(__name__)

LATCH_BYTE_COUNT = 3
LATCH = bytearray(0 for i in xrange(LATCH_BYTE_COUNT))

INTERNAL_LATCH_BYTE_COUNT = 0

def _light_array(count, x=0x80):
  b = bytearray(x for i in xrange(count + INTERNAL_LATCH_BYTE_COUNT))
  for i in xrange(INTERNAL_LATCH_BYTE_COUNT):
    b[-1 - i] = 0
  return b

class Light(Sequence.Sequence):
  def __init__(self, parent, description):
    super(Light, self).__init__(parent, description)
    scenes = description.get('scenes', {}).iteritems()
    self.scenes = dict((k, Scene.scene(self, v)) for k, v in scenes)
    self.timeout = Units.convert(description.get('period', '50ms'))
    self.active_scenes = set()
    self.device = None
    self.light_count = Config.get('light', 'count')
    self.clear = _light_array(self.light_count)
    self.pattern = _light_array(self.light_count)
    self.lock = threading.Lock()

  def _write(self, lights):
    with self.lock:
      self.device.write(lights)
      self.device.flush()
      self.device.write(LATCH)
      self.device.flush()

  def _clear(self):
    self._write(self.clear)

  def _on_run(self):
    super(Light, self)._on_run()
    self.device = open('/dev/spidev0.0', 'wb')
    self._clear()

  def _on_pause(self):
    self._clear()
    with self.lock:
      self.device.close()
      self.device = None

  def run_scene(self, scene):
    self.active_scenes.add(self.scenes[scene.scene])

  def pause_scene(self, scene):
    self.active_scenes.remove(self.scenes[scene.scene])
    if not len(self.active_scenes):
      self._clear()

  def single_loop(self):
    super(Light, self).single_loop()
    scenes = [s() for s in self.active_scenes]
    lights = echomesh.color.Light.combine(echomesh.color.Light.sup, *scenes)
    for i, light in enumerate(lights):
      if light is None:
        light = [0x80, 0x80, 0x80]
      else:
        light = [min(0xFF, int(0x80 + 0x7F * x)) for x in light]
        r, g, b = light
        light = [b, r, g]
      self.pattern[3 * i:3 * (i + 1)] = light
    self._write(self.pattern)

