# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from SocketServer import ThreadingTCPServer,BaseRequestHandler
import traceback
import threading
import re

import sys

reload(sys)

sys.setdefaultencoding('utf')

############################

server_status=0  #服务器状态 0：关闭 1:开启


command_ledstatus=[0,0,0,0]
checkbox_ledstatus=[0,0,0,0]
a=0

LED=['red','green','yello','blue']


#######################
RevBuf = ''
SendBuf = ''





try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



#######多线程服务器的handle程序
class MyBaseRequestHandlerr(BaseRequestHandler):  
    """ 
    #从BaseRequestHandler继承，并重写handle方法 
    """  
    def handle(self):  
        global SendBuf,RevBuf
        #循环监听（读取）来自客户端的数据  
        while True:  
            #当客户端主动断开连接时，self.recv(1024)会抛出异常  
            try:  
                #一次读取1024字节,并去除两端的空白字符(包括空格,TAB,\r,\n)  
                RevBuf = str(self.request.recv(1024).strip())
                  
                #self.client_address是客户端的连接(host, port)的元组  
                print "receive from (%r):%r" % (self.client_address, RevBuf)  
                if not SendBuf =='':
                    self.request.sendall(SendBuf)
                else:
                    self.request.sendall("got")
            except:  
                traceback.print_exc()  
                break 



def server():
    global servertcpthread
    try:
        print 'activating server...'
        servertcpthread.serve_forever()
    except Exception as e:
        raise e
    finally:
        servertcpthread.shutdown()
        pass
    pass

            
serverT1=''


host = "127.0.0.1"
port = 21010
ADDR = (host,port)
servertcpthread = ThreadingTCPServer(ADDR,MyBaseRequestHandlerr)

##############################################
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(765, 295)

        self.timer = QTimer()

        self.commandline = QtGui.QLineEdit(Dialog)
        self.commandline.setGeometry(QtCore.QRect(370, 220, 351, 21))
        self.commandline.setObjectName(_fromUtf8("commandline"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(410, 200, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.push_sendcommand = QtGui.QPushButton(Dialog)
        self.push_sendcommand.setGeometry(QtCore.QRect(560, 260, 71, 21))
        self.push_sendcommand.setObjectName(_fromUtf8("push_sendcommand"))


        self.open_server = QtGui.QPushButton(Dialog)
        self.open_server.setGeometry(QtCore.QRect(80, 2, 75, 25))
        self.open_server.setObjectName(_fromUtf8("push_sendcommand"))

        self.open_client = QtGui.QPushButton(Dialog)
        self.open_client.setGeometry(QtCore.QRect(0, 2, 75, 25))
        self.open_client.setObjectName(_fromUtf8("push_sendcommand"))

        self.pushclrcommand = QtGui.QPushButton(Dialog)
        self.pushclrcommand.setGeometry(QtCore.QRect(670, 260, 75, 23))
        self.pushclrcommand.setObjectName(_fromUtf8("pushclrcommand"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(370, 20, 261, 161))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit.setReadOnly(True)
        self.checkBox_linkstatus = QtGui.QCheckBox(Dialog)
        self.checkBox_linkstatus.setGeometry(QtCore.QRect(80, 210, 91, 16))
        self.checkBox_linkstatus.setObjectName(_fromUtf8("checkBox_linkstatus"))
        self.checkBox_red = QtGui.QCheckBox(Dialog)
        self.checkBox_red.setGeometry(QtCore.QRect(660, 54, 91, 16))
        self.checkBox_red.setObjectName(_fromUtf8("checkBox_red"))
        self.checkBox_yellow = QtGui.QCheckBox(Dialog)
        self.checkBox_yellow.setGeometry(QtCore.QRect(660, 76, 91, 16))
        self.checkBox_yellow.setObjectName(_fromUtf8("checkBox_yellow"))
        self.checkBox_blue = QtGui.QCheckBox(Dialog)
        self.checkBox_blue.setGeometry(QtCore.QRect(660, 98, 91, 16))
        self.checkBox_blue.setObjectName(_fromUtf8("checkBox_blue"))
        self.checkBox_green = QtGui.QCheckBox(Dialog)
        self.checkBox_green.setGeometry(QtCore.QRect(660, 120, 91, 16))
        self.checkBox_green.setObjectName(_fromUtf8("checkBox_green"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 83, 71, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.wifiSSID = QtGui.QLineEdit(Dialog)
        self.wifiSSID.setGeometry(QtCore.QRect(148, 81, 181, 20))
        self.wifiSSID.setObjectName(_fromUtf8("wifiSSID"))
        self.targetIP = QtGui.QLineEdit(Dialog)
        self.targetIP.setGeometry(QtCore.QRect(148, 29, 181, 20))
        self.targetIP.setObjectName(_fromUtf8("targetIP"))
        self.push_link = QtGui.QPushButton(Dialog)
        self.push_link.setGeometry(QtCore.QRect(190, 210, 75, 23))
        self.push_link.setObjectName(_fromUtf8("push_link"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 134, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.targetPort = QtGui.QLineEdit(Dialog)
        self.targetPort.setGeometry(QtCore.QRect(148, 55, 181, 20))
        self.targetPort.setObjectName(_fromUtf8("targetPort"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(27, 28, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(27, 58, 91, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.wifiPasswd = QtGui.QLineEdit(Dialog)
        self.wifiPasswd.setGeometry(QtCore.QRect(148, 107, 181, 20))
        self.wifiPasswd.setObjectName(_fromUtf8("wifiPasswd"))
        self.serverIP = QtGui.QLineEdit(Dialog)
        self.serverIP.setGeometry(QtCore.QRect(148, 133, 181, 20))
        self.serverIP.setObjectName(_fromUtf8("serverIP"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 108, 71, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.serverPort = QtGui.QLineEdit(Dialog)
        self.serverPort.setGeometry(QtCore.QRect(148, 159, 181, 20))
        self.serverPort.setObjectName(_fromUtf8("serverPort"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 160, 71, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.checkBox_linkstatus.raise_()
        self.checkBox_red.raise_()
        self.checkBox_yellow.raise_()
        self.checkBox_blue.raise_()
        self.checkBox_green.raise_()
        self.commandline.raise_()
        self.label.raise_()
        self.push_sendcommand.raise_()
        self.pushclrcommand.raise_()
        self.textEdit.raise_()
        self.label_4.raise_()
        self.wifiSSID.raise_()
        self.targetIP.raise_()
        self.push_link.raise_()
        self.label_3.raise_()
        self.targetPort.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.wifiPasswd.raise_()
        self.serverIP.raise_()
        self.label_6.raise_()
        self.serverPort.raise_()
        self.label_7.raise_()

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushclrcommand, QtCore.SIGNAL(_fromUtf8("clicked()")), self.commandline.clear)
        QtCore.QObject.connect(self.push_sendcommand, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sendcommand)
        QtCore.QObject.connect(self.push_link, QtCore.SIGNAL(_fromUtf8("clicked()")), self.get_link_parameters)
        QtCore.QObject.connect(self.checkBox_red, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sendredLedstatus)
        QtCore.QObject.connect(self.checkBox_yellow, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sendyellowLedstatus)
        QtCore.QObject.connect(self.checkBox_blue, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sendblueLedstatus)
        QtCore.QObject.connect(self.checkBox_green, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sendgreenLedstatus)
        QtCore.QObject.connect(self.open_client, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sendgreenLedstatus)
        QtCore.QObject.connect(self.open_server, QtCore.SIGNAL(_fromUtf8("clicked()")), self.openserver)
        QtCore.QObject.connect(self.timer, SIGNAL('timeout()'), self.set_checkbox_ledstatus)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "发送命令", None))
        self.push_sendcommand.setText(_translate("Dialog", "发送命令", None))

        self.open_server.setText(_translate("Dialog", "打开服务器", None))
        self.open_client.setText(_translate("Dialog", "打开客户端", None))

        self.pushclrcommand.setText(_translate("Dialog", "清除命令", None))
        self.checkBox_linkstatus.setText(_translate("Dialog", "连接状态", None))
        self.checkBox_red.setText(_translate("Dialog", "redLED", None))
        self.checkBox_yellow.setText(_translate("Dialog", "yellowLED", None))
        self.checkBox_blue.setText(_translate("Dialog", "blueLED", None))
        self.checkBox_green.setText(_translate("Dialog", "greenLED", None))
        self.label_4.setText(_translate("Dialog", "WIFI_SSID", None))
        self.push_link.setText(_translate("Dialog", "进行连接", None))
        self.label_3.setText(_translate("Dialog", "服务器IP", None))
        self.label_2.setText(_translate("Dialog", "目标路由器IP", None))
        self.label_5.setText(_translate("Dialog", "目标路由器端口", None))
        self.label_6.setText(_translate("Dialog", "WIFI_PASSAD", None))
        self.label_7.setText(_translate("Dialog", "服务器端口", None))

    def write_in_textedit(self,buffer):
        global a
        if(a>15):
            a=1
            self.textEdit.setText(buffer)
        else:
            a+=1
            self.textEdit.append(buffer)

    def sendcommand(self):
        global SendBuf,a
        SendBuf=str(self.commandline.text())
        print SendBuf
        buf="发送命令："+SendBuf

        self.write_in_textedit(buf)

    def sendredLedstatus(self):
        global SendBuf,a
        # if(self.checkBox_red.checkState() == QtCore.Qt.Checked):
        if(self.checkBox_red.checkState() ==2):
            buf="点亮："+LED[0]
            self.write_in_textedit(buf)
            SendBuf="{LED11}"
            checkbox_ledstatus[0]=1
        else:
            buf="关闭："+LED[0]
            self.write_in_textedit(buf)
            SendBuf="{LED10}"
            print checkbox_ledstatus[0]
            checkbox_ledstatus[0]=0
        print SendBuf

    def sendgreenLedstatus(self):
        global SendBuf,a
        if(self.checkBox_green.checkState() ==2):
            buf="点亮："+LED[1]
            self.write_in_textedit(buf)
            SendBuf = "{LED21}"
            checkbox_ledstatus[1]=1
        else:
            buf="关闭："+LED[1]
            self.write_in_textedit(buf)
            SendBuf = "{LED20}"
            checkbox_ledstatus[1]=0

    def sendyellowLedstatus(self):
        global SendBuf,a
        if(self.checkBox_yellow.checkState() ==2):
            buf="点亮："+LED[2]
            self.write_in_textedit(buf)
            SendBuf = "{LED31}"
            checkbox_ledstatus[2]=1
        else:
            buf="关闭："+LED[2]
            self.write_in_textedit(buf)
            SendBuf = "{LED30}"
            checkbox_ledstatus[2]=0

    def sendblueLedstatus(self):
        global SendBuf,a
        if(self.checkBox_blue.checkState() ==2):
            buf="点亮："+LED[3]
            self.write_in_textedit(buf)
            SendBuf = "{LED41}"
            checkbox_ledstatus[3]=1
        else:
            buf="关闭："+LED[3]
            self.write_in_textedit(buf)
            SendBuf = "{LED40}"
            checkbox_ledstatus[3]=0

    def get_link_parameters(self):
        link_parameter = [str(self.targetIP.text()),int(self.targetPort.text()),
        str(self.wifiSSID.text()),str(self.wifiPasswd.text()),str(self.serverIP.text()),str(self.serverPort.text())]
        print link_parameter
        pass

    def parsecommand(self):
        buf=[]
        if RevBuf:
            slices = RevBuf.split(';')
            for i in slices[1:5]:
                print i
                match = re.search(",([0,1])",i)
                if match:
                    buf.append(match.group()[1])
        print buf
        return buf

    def set_checkbox_ledstatus(self):
        global command_ledstatus,RevBuf
        if RevBuf:
            buf_led = self.parsecommand()
            if buf_led:
                command_ledstatus=buf_led
                if command_ledstatus:
                    if command_ledstatus[0]==1:
                        self.checkBox_red.setCheckState(0)
                    else:
                        self.checkBox_red.setCheckState(2)
            else:
                print "get error data..."
                RevBuf = ''



    def openserver(self):
        global server_status,serverT1,servertcpthread
        if server_status==0:
            server_status=1
            

            serverT1=threading.Thread(target = server,name= 111)
            serverT1.start()
            print serverT1


            self.timer.start(1000)
            self.open_server.setText(_translate("Dialog", "关闭服务器", None))
        else:
            if server_status==1:
                print servertcpthread
                servertcpthread.server_close()
                self.open_server.setText(_translate("Dialog", "打开服务器", None))
                self.timer.stop()
                server_status=0
                print "server already deactivated"
                print serverT1
################################################################






def windows():
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    pass






if __name__ == '__main__':
    t1 = threading.Thread(target = windows,name='windows')
    t1.start()

