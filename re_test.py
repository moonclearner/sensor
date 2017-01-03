# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re


def parsecommand(RevBuf):
    ledstatus=[]
    if not RevBuf=='':
        slices = RevBuf.split(';')
        for i in slices[1:5]:
            print i
            match = re.search(",([0,1])",i)
            if match:
                ledstatus.append(match.group()[1])
        print  ledstatuss

parsecommand(r'\x80D\x80\x00\x06771323\x05\x008,;red_statu,1;green_statu,0;yellow_statu,0;blue_statu,0;')