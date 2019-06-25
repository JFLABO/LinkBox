#受け取ったファイル名をlinkbox_dict.jsonに変更してデータファイルを差し替えてください

#hey hello
#D&Dでファイルを表示
#ファイル名を指定して開く
# -*- coding: utf-8 -*-
#LinkBoxフォルダに有るインターネットショートカット(.url)を自動で一覧にする
#.urlはChromeでデスクトップにドラッグアンドドロップしてできるファイル
import wx
import wx.grid
import wx.grid as gridlib
import glob
import webbrowser
import json
import socket
import datetime
import os
from operator import itemgetter

class GridFrame(wx.Frame):
    def __init__(self, parent):
        
        f=wx.Frame.__init__(self, parent)
        self.SetTransparent(50)
        grid = wx.grid.Grid(self, -1)
        grid.CreateGrid(150, 3)
            
        #json_data = json.load(f)
        #ネットワーク正当性検証
        #key検証
        f = open('linkbox_dict.json', 'r',encoding="utf8")
        json_data = json.load(f)
        j=0
        grid.SetColSize(0, 640)
        grid.SetColSize(1, 1)
        grid.SetColSize(2, 110)
        for jsn_key in json_data:
            if j == 149:
                continue
            grid.SetCellValue(j, 0, jsn_key[0])
            if len(jsn_key)<2:
                #continue
                print(jsn_key)
            else:
                grid.SetCellValue(j, 1, jsn_key[1])
                grid.SetCellValue(j, 2, jsn_key[2])
            
            attr = gridlib.GridCellAttr()
            attr.SetReadOnly(True)
            grid.SetRowAttr(j, attr)
            j=j+1
        grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.click)
        f.close
        self.Show()
        
    def GetValue(self, row, col):
        return self.data[row][col]
    
    def click(self, event):
        obj = event.GetEventObject()
        print(vars(self))
        print(vars(event))
        print(obj)
        url=obj.GetCellValue(event.GetRow(),1)
        print(url)
        webbrowser.open(url)
    
if __name__ == '__main__':

    app = wx.App(0)
    frame = GridFrame(None)
    frame.SetTransparent(10)
    frame.SetSize(0,0,990,480)
    frame.Centre()
    frame.SetTransparent(250)
    app.MainLoop()

#the magic
