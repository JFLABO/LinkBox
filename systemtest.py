# -*- coding: utf-8 -*-
import os
import wx
import psutil
import platform
import subprocess  
import multiprocessing

info=subprocess.check_output(["wmic","cpu","get", "name"])  
#print info.split('@')[1].split(' ')[1]

# gives a single float value
a=psutil.cpu_percent()

# gives an object with many fields
b=psutil.virtual_memory()

# you can convert that object to a dictionary 
c=dict(psutil.virtual_memory()._asdict())

d=platform.processor()
app = wx.App()

info2=multiprocessing.cpu_count()
# メッセージボックスを表示
wx.MessageBox(u'SYSTEMTEST::'+d+ str(a) + str(b) + str(c)+str(info)+str(info2)+"Cores", u'タイトル')
