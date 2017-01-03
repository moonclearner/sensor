# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# ThreadingTCPServer + StreamRequestHandler = 多线程socket

from SocketServer import ThreadingTCPServer,BaseRequestHandler
import traceback


class MyBaseRequestHandlerr(BaseRequestHandler):  
    """ 
    #从BaseRequestHandler继承，并重写handle方法 
    """  
    def handle(self):  
        global RevBuf
        #循环监听（读取）来自客户端的数据  
        while True:  
            #当客户端主动断开连接时，self.recv(1024)会抛出异常  
            try:  
                #一次读取1024字节,并去除两端的空白字符(包括空格,TAB,\r,\n)  
                RevBuf = self.request.recv(1024).strip()  
                  
                #self.client_address是客户端的连接(host, port)的元组  
                print "receive from (%r):%r" % (self.client_address, RevBuf)  
                  
                #转换成大写后写回(发生到)客户端  
                print SendBuf
                self.request.sendall(RevBuf)  
            except:  
                traceback.print_exc()  
                break 

def server():
    host = "127.0.0.1"
    port = 21010
    ADDR = (host,port)
    try:
        server = ThreadingTCPServer(ADDR,MyBaseRequestHandlerr)
        server.serve_forever()
    except Exception as e:
        raise e
    finally:
        server.shutdown()
        pass

	pass

if __name__ == '__main__':
    server()


