from __future__ import absolute_import, division, print_function, unicode_literals

from echomesh.network import ClientServer
from echomesh.sound import PlayerSetter
from echomesh.util import Dict
from echomesh.util import Log
from echomesh.util.thread.MasterRunnable import MasterRunnable

LOGGER = Log.logger(__name__)

_ENVELOPE_ERROR = "ExternalPlayer.%s must either be constant or an envelope."

def _fix(player, name):
  part = getattr(player, name)
  result = {'is_constant': part.is_constant}
  if part.is_constant:
    result['value'] = part.evaluate()
  elif part.envelope:
    result['envelope'] = part.envelope.description()
  else:
    raise Exception(_ENVELOPE_ERROR % name)
  setattr(player, name, result)

class ExternalPlayer(MasterRunnable):
  _FIELDS = 'begin', 'end', 'file', 'passthrough', 'level', 'pan', 'loops'

  def __init__(self, element, level=1, pan=0, loops=1, **kwds):
    ClientServer.instance()
    super(ExternalPlayer, self).__init__()
    PlayerSetter.set_player(self, element, level=1, pan=0, loops=1, **kwds)
    _fix(self, '_level')
    _fix(self, '_pan')
    data = dict((f, getattr(self, '_' + f)) for f in ExternalPlayer._FIELDS)
    self._write(type='construct', **data)

  def _on_run(self):
    self._write(type='run')

  def _on_begin(self):
    self._write(type='begin')

  def _on_pause(self):
    self._write(type='pause')

  def unload(self):
    self._write(type='unload')

  def _write(self, **data):
    data['hash'] = hash(self)
    ClientServer.instance().write(type='audio', data=data)
