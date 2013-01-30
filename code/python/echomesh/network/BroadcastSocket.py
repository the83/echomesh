from __future__ import absolute_import, division, print_function, unicode_literals

# Send and receive UDP broadcast packets

import select
import socket
import sys
import time

from echomesh.base import Platform
from echomesh.util.thread.MasterRunnable import MasterRunnable

DEFAULT_PORT = 1248
DEFAULT_BUFFER_SIZE = 1024

USAGE = '%s read | write' % sys.argv[0]

class Socket(MasterRunnable):
  def __init__(self, port):
    super(Socket, self).__init__()
    self.port = port
    self._open()

  def _open(self):
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.socket.bind(('', self.bind_port))

  def stop(self):
    super(Socket, self).stop()
    self.socket.close()

class Send(Socket):
  def __init__(self, port):
    self.bind_port = 0
    super(Send, self).__init__(port)

  def _open(self):
    super(Send, self)._open()
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

  def write(self, data):
    try:
      self.socket.sendto(data, ('<broadcast>', self.port))
    except:
      if self.is_running:
        raise

class Receive(Socket):
  def __init__(self, port, buffer_size=DEFAULT_BUFFER_SIZE):
    self.bind_port = port
    self.buffer_size = buffer_size
    super(Receive, self).__init__(port)

  def _open(self):
    super(Receive, self)._open()
    self.socket.setblocking(0)

  def receive(self, timeout):
    try:
      result = select.select([self.socket], [], [], timeout)
      return result[0] and result[0][0].recv(self.buffer_size)
    except:
      if self.is_running:
        raise

