#!/usr/bin/python

import select
import socket

BUFFER_SIZE = 1024
DEFAULT_PORT = 8888
PORT_NAME = '<broadcast>'
PORT_NAME = ''

## From http://code.activestate.com/recipes/577278/ (r1)

def receive_broadcast(port):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind((PORT_NAME, port))
  s.setblocking(0)

  while True:
    result = select.select([s],[],[])
    msg = result[0][0].recv(BUFFER_SIZE)
    print msg

if __name__ == '__main__':
  receive_broadcast(DEFAULT_PORT)