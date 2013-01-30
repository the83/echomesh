import Queue
import socket
import time
import yaml

from echomesh.network import BroadcastSocket
from echomesh.util import Log
from echomesh.util.thread import ThreadLoop
from echomesh.util.thread.MasterRunnable import MasterRunnable

LOGGER = Log.logger(__name__)

class DataSocket(MasterRunnable):
  def __init__(self, port, timeout, callback):
    super(DataSocket, self).__init__()
    self.timeout = timeout
    self.callback = callback
    self.queue = Queue.Queue()

    try:
      self.receive_socket = BroadcastSocket.Receive(port)
      self.send_socket = BroadcastSocket.Send(port)
    except socket.error as e:
      if e.errno == errno.EADDRINUSE:
        raise Exception('A DataSocket is already running on port %d'  % port)
      else:
        raise

    send = ThreadLoop.ThreadLoop(single_loop=self._send, name='send')
    receive = ThreadLoop.ThreadLoop(single_loop=self._receive, name='receive')

    self.add_mutual_stop_slave(self.receive_socket, self.send_socket, receive, send)
    self.send = self.queue.put

  def _receive(self):
    pckt = self.receive_socket.receive(self.timeout)
    if pckt:
      LOGGER.debug('receiving %s', pckt)
      self.callback(yaml.safe_load(pckt))

  def _send(self):
    try:
      item = self.queue.get(True, self.timeout)
      value = yaml.safe_dump(item)
      self.send_socket.write(value)
    except Queue.Empty:
      pass
    if self.is_running:
      time.sleep(self.timeout)

