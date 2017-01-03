# sensor collection system
from __future__ import unicode_literals
# starting time: 30, December,2016 
# author: moonclearner
# -*- coding: utf-8 -*-

from socket import *
from time import ctime

Host = '127.0.0.1'
Port = 21010
BufferSize = 1024 
ADDR = (Host,Port)


def server_init():
	tcpserversock = socket(AF_INET,SOCK_STREAM)
	tcpserversock.bind(ADDR)
	tcpserversock.listen(5)
	while True:
		print "waiting for connection ..."	
		tcpCliSock, addr =tcpserversock.accept()
		print '...connected from:',addr
		while True:
			data = tcpCliSock.recv(BufferSize)
			if not data:
				break
			tcpCliSock.send('[%s] %s' % (ctime(),data))
		tcpCliSock.close()
	pass

server_init()


