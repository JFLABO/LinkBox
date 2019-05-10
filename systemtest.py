# -*- coding: utf-8 -*-
import os
import wx
import psutil
import platform

# gives a single float value
a=psutil.cpu_percent()

# gives an object with many fields
b=psutil.virtual_memory()

# you can convert that object to a dictionary 
c=dict(psutil.virtual_memory()._asdict())

d=platform.processor()
app = wx.App()

# メッセージボックスを表示
wx.MessageBox(u'SYSTEMTEST::'+d+ str(a) + str(b) + str(c), u'この画面が出た場合はOKです。')
# 出ない場合は環境にプログラムが足りない可能性があります。
