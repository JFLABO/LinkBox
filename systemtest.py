# -*- coding: utf-8 -*-
import os
import wx
import psutil
# gives a single float value
a=psutil.cpu_percent()
# gives an object with many fields
b=psutil.virtual_memory()
# you can convert that object to a dictionary 
c=dict(psutil.virtual_memory()._asdict())

app = wx.App()

# メッセージボックスを表示
wx.MessageBox(u'TEST'+ str(a) + str(b) + str(c), u'タイトル')
