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
import Crypto.Cipher.AES as AES
from time import sleep
import base64

class GridFrame(wx.Frame):
    def __init__(self, parent):
        
        f=wx.Frame.__init__(self, parent)
        #wx.Frame.__init__(self, parent, id, title,size=(250, 250))

        #f.setSize(100,650)
        # Create a wxGrid object
        self.SetTransparent(50)
        grid = wx.grid.Grid(self, -1)
        # Then we call CreateGrid to set the dimensions of the grid
        # (100 rows and 10 columns in this example)
        grid.CreateGrid(50, 3)

        # We can set the sizes of individual rows and columns
        # in pixels
        #grid.SetRowSize(0, 20)
        #grid.SetColSize(0, 640)

        # And set grid cell contents as strings
        #grid.SetCellValue(0, 0, 'wxGrid is good')
        #attr = gridlib.GridCellAttr()
        #attr.SetReadOnly(True)
        i=0
        json_dict={}
        json_arr=[[],[],[]]
        json_arr.clear()
        #JSON データの書き込み
        host = socket.gethostname()
        #json_dict["agent"]=host
        dt=datetime.datetime.today()
        dtts=dt.strftime("%Y/%m/%d %H:%M:%S")
        json_arr.append([host,"meta infomation",dtts])
        #json_dict["rpt_at"]=dt.strftime("%Y/%m/%d %H:%M:%S")
        
        for name in glob.iglob('../**/*.url', recursive=True):
        #print(name)
            #if i == 49:
            #    continue

            #grid.SetCellValue(i, 0, name)
            
            #json_dict[name]=name
            with open(name) as f:
                s = f.read()
                
            #print(s.replace(' ', '-'))
            url=s.replace('[InternetShortcut]', '')
            url=url.replace('URL=', '')
            url=url.replace('URL=', '')
            url=url.strip()
            
            #grid.SetCellValue(i, 1, url)
            
            #grid.SetRowAttr(i, attr)
            #json_arr[i][1]=url
            
            #ts=os.stat(name).st_mtime
            ts=datetime.datetime.fromtimestamp(os.stat(name).st_mtime)
            dt2=ts.strftime('%Y/%m/%d  %H:%M:%S')

            #json_obj["timestamp"]=ts
            #json_arr[i][2]=ts
            #print(grid.GetCellValue(1,1))
            
            #URL JSON生成
            json_arr.append([name,url,dt2])

            i=i+1
        #変数を格納

        #gridにmodelをバインド
            
        f2 = open('linkbox_dict.json', 'w', encoding='utf8')
        #json_arr.remove(0)
        #sort reverse
        json_arr.sort(key=itemgetter(2),reverse=True)
        #json.dump(json_arr, f2, ensure_ascii=False)
        #encoding='utf8'
        json.dump(json_arr, f2,indent=2, ensure_ascii=False)
        f2.close
        with open('linkbox_dict.json', 'a') as f3:
            print(']]', file=f3)

        #remore datapack
        #f = open('remote_data_pack.linkbox', 'w',encoding="utf8")

        #json_data = json.load(f)
        #ネットワーク正当性検証
        #key検証
        with open('linkbox_dict.json',encoding="utf8") as f6:
            coredata = f6.read()
            
        """main
        """
        #size=len(coredata)
        ts1=datetime.datetime.today()
        dt3=ts1.strftime('%Y_%m_%d_%H_%M_%S')
            
        path_w = 'remote_data_pack'+dt3+'.linkbox'

        #key = b'0123456789abcdef'
        #fsz = os.path.getsize(path_w)
        #iv = b'0' * fsz

        # AES-CBC モードで暗号化
        #aes = AES.new(key, AES.MODE_CBC, iv)
        # bytes 型を渡す
        #cipher = aes.encrypt(coredata.encode('utf8'))
        #fsz = os.path.getsize(path_w)
        #with open(path_w, 'w') as fout:
        #    fout.write(struct.pack('<Q', fsz))
        #file = open('./linkbox_dict.json', 'rt',encoding="utf8").read()
        #obj=[]
        #obj.append(file)
        #enc_file = base64.b64encode(obj)
        with open(path_w, mode='w',encoding="utf8") as f5:
            f5.write(str(coredata))
        # 使い回せないでのデコード用を新しく用意する
        #aes = AES.new(key, AES.MODE_CBC, iv)
        # bytes 型が返る
        #plain = aes.decrypt(cipher).decode('ascii')
        #print(plain)
    
        #grid = wx.grid.Grid(self)
        # Set model.
        #grid.SetTable(MyTable())

        #grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.click)
        
        #self.SetTransparent(255)
        #sleep(1)
        f = open('linkbox_dict.json', 'r',encoding="utf8")

        json_data = json.load(f)
        j=0
        grid.SetColSize(0, 640)
        grid.SetColSize(1, 1)
        grid.SetColSize(2, 110)
        for jsn_key in json_data:
            if j == 49:
                continue
            #print(jsn_key[0])
            #s=str(jsn_key)
            #data=s.split(',')
            grid.SetCellValue(j, 0, jsn_key[0])
            #print(jsn_key[1])
            #while True:
            #    try:
            #        print(jsn_key[1])
            #    except:
            #        pass
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
        #for name in json_data:
        #print(json_data)   
        self.Show()
        
    def GetValue(self, row, col):
        return self.data[row][col]
    
    def click(self, event):
        obj = event.GetEventObject()
        print(vars(self))
        print(vars(event))
        print(obj)
        #url=obj.GetCellValue(event.GetRow(),event.GetCol())
        url=obj.GetCellValue(event.GetRow(),1)
        
        #url=self.grid.GetCellValue(self,1,1)
        #url=wx._grid.GridCellAttr
        print(url)
        #print(self.grid.GetCellValue(1,1))
        #url=self.g
        #url=self.grid.GetCellValue(1,1)
        #url = "amazon.co.jp"
        webbrowser.open(url)
        #print('Double click')
        
if __name__ == '__main__':

    app = wx.App(0)

    frame = GridFrame(None)
    frame.SetTransparent(10)
    #frame.set_window_size(100,470)
    #frame.SetDimensions(0,0,840,480)
    frame.SetSize(0,0,990,480)
    frame.Centre()
    #self.SetTransparent(1)
    frame.SetTransparent(250)
    app.MainLoop()

#magic
