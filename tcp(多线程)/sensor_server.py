# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# ThreadingTCPServer + StreamRequestHandler = 多线程socket

from SocketServer import ThreadingTCPServer,BaseRequestHandler,StreamRequestHandler
import traceback

class MyStreamRequestHandlerr(StreamRequestHandler):  
    """ 
    #继承StreamRequestHandler，并重写handle方法 
    #（StreamRequestHandler继承自BaseRequestHandler） 
    """  
    def handle(self):  
        while True:  
            #客户端主动断开连接时，self.rfile.readline()会抛出异常  
            try:  
                #self.rfile类型是socket._fileobject,读写模式是"rb",方法有  
                #read,readline,readlines,write(data),writelines(list),close,flush  
                data = self.rfile.readline().strip()  
                print "receive from (%r):%r" % (self.client_address, data)  
                  
                #self.wfile类型是socket._fileobject,读写模式是"wb"  
                self.wfile.write(data.upper())  
            except:  
                traceback.print_exc()  
                break  

class MyBaseRequestHandlerr(BaseRequestHandler):  
    """ 
    #从BaseRequestHandler继承，并重写handle方法 
    """  
    def handle(self):  
        #循环监听（读取）来自客户端的数据  
        while True:  
            #当客户端主动断开连接时，self.recv(1024)会抛出异常  
            try:  
                #一次读取1024字节,并去除两端的空白字符(包括空格,TAB,\r,\n)  
                data = self.request.recv(1024).strip()  
                  
                #self.client_address是客户端的连接(host, port)的元组  
                print "receive from (%r):%r" % (self.client_address, data)  
                  
                #转换成大写后写回(发生到)客户端  
                self.request.sendall(data.upper())  
            except:  
                traceback.print_exc()  
                break 

def main():
	host = "192.168.191.1"
	port = 21010
	ADDR = (host,port)

	server = ThreadingTCPServer(ADDR,MyBaseRequestHandlerr)
	server.serve_forever()
	pass

if __name__ == '__main__':
	main()


