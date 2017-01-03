# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from socket import *

Host = '127.0.0.1'
Port = 21010
ADDR = (Host,Port)

BufferSize = 1024

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	data = raw_input('>>>')
	if not data:
		break
	tcpCliSock.send(data)

	data = tcpCliSock.recv(BufferSize)

	if not data:
		break
	print data

tcpCliSock.close()