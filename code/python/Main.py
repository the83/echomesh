#!/usr/bin/python

from __future__ import absolute_import, division, print_function, unicode_literals

ECHOMESH_EXTERNALS_OVERRIDE_SYSTEM_PACKAGES = True
# If this is True, you want Echomesh to use its own external packages in
# preference to any you might have installed in your system path.

USE_DIGITS_FOR_PROGRESS_BAR = not False
PRINT_STARTUP_TIMES = not False

def run():
  import sys

  times = []

  def p(msg='', count=[0]):
    """Print progress messages while echomesh loads."""
    print(msg, end='')
    dot = str(count[0]) if USE_DIGITS_FOR_PROGRESS_BAR else '.'
    print(dot, end='')
    count[0] = (count[0] + 1) % 10

    sys.stdout.flush()

    import time
    times.append(time.time())

  p('Loading echomesh ')

  import os.path
  p()

  from echomesh.base import Path
  p()  # 11ms

  # Make sure we can find the external packages,
  external = os.path.join(Path.CODE_PATH, 'external')
  p()

  if ECHOMESH_EXTERNALS_OVERRIDE_SYSTEM_PACKAGES:
    sys.path.insert(1, external)
  else:
    sys.path.append(external)
  p()

  from echomesh.base import Config  # Must be the first import.
  p()  # 1215ms

  Config.recalculate(args=sys.argv)
  p() # 1329ms

  if not (Config.get('autostart') or len(sys.argv) < 2 or sys.argv[1] != 'autostart'):
    from echomesh.util import Log
    print()
    Log.logger(__name__).info("Not autostarting because autostart=False")
    exit(0)
  p()

  from echomesh.sound import SetOutput
  p()  # 274ms

  SetOutput.set_output(Config.get('audio', 'output', 'route'))
  p()  # 425ms

  from echomesh import Echomesh
  p()  # This is the big one, taking 3709ms on my RP.

  echomesh = Echomesh.Echomesh()
  p()  # 599ms

  print()

  if Config.get('diagnostics', 'dump_startup_times'):
    print()
    for i in range(len(times) - 1):
      print(i, ':', int(1000 * (times[i + 1] - times[i])))
    print()

  echomesh.start()
  echomesh.loop()
  echomesh.join()

  if Config.get('diagnostics', 'dump_unused_configs'):
    import yaml
    print(yaml.safe_dump(Config.get_unvisited()))


if __name__ == '__main__':
  try:
    run()
  except:
    import traceback
    print(traceback.format_exc())
