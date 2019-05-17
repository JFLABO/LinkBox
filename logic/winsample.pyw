import wx
import wx.grid
import wx.grid as gridlib
import glob
import webbrowser
import json

class SampleApp(wx.App):
    def OnInit(self):
        self.init_frame()
        return True

    def init_frame(self):
        self.frm_main = wx.Frame(None)
        
        self.sizer = wx.BoxSizer()
        self.frm_main.SetSizer(self.sizer)
        self.txt_title = wx.TextCtrl(self.frm_main)
        self.sizer.Add(self.txt_title, 1, wx.ALIGN_TOP)
        self.btn_submit = wx.Button(self.frm_main)
        self.btn_submit.SetLabel("検索")
        self.sizer.Add(self.btn_submit, 0, wx.ALIGN_TOP)
        self.frm_main.SetTitle("sample_2_2")
        self.frm_main.SetSize(0,0,840,480)
        
        element_array = ('element_1', 'element_2', 'element_4','element_3', 'element_5')
        combobox_1 = wx.ComboBox(self.frm_main, wx.ID_ANY, '選択してください',choices=element_array, style=wx.CB_SIMPLE)
        #self.sizer.Add(self.combobox_1, 0, wx.ALIGN_TOP)
        
        grid = wx.grid.Grid(self.frm_main,pos=(50,50))
        #grid.SetPo
        #self.sizer.Add(self.grid, 0, wx.ALIGN_TOP)
        
        # Then we call CreateGrid to set the dimensions of the grid
        # (100 rows and 10 columns in this example)
        grid.CreateGrid(150, 3)

        # We can set the sizes of individual rows and columns
        # in pixels
        grid.SetRowSize(0, 20)
        grid.SetColSize(0, 640)

        # And set grid cell contents as strings
        #grid.SetCellValue(0, 0, 'wxGrid is good')
        attr = gridlib.GridCellAttr()
        attr.SetReadOnly(True)
        #grid.SetRowAttr(0, attr)
        i=0
        json_dict={}
        for name in glob.iglob('../**/*.url', recursive=True):
        #print(name)
            grid.SetCellValue(i, 0, name)
            with open(name) as f:
                s = f.read()
            #print(s.replace(' ', '-'))
            url=s.replace('[InternetShortcut]', '')
            url=url.replace('URL=', '')
            url=url.replace('URL=', '')
            url=url.strip()    
            grid.SetCellValue(i, 1, url)
            #print(grid.GetCellValue(1,1))
            grid.SetRowAttr(i, attr)
            json_dict[name]=url
            i=i+1
        #辞書を作成
            
        #JSON データの書き込み
        f2 = open('linkbox_dict.json', 'w')
        json.dump(json_dict, f2)

        grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.click)
        grid.SetSize(0,0,840,480)
        
        self.frm_main.SetSize((840, 200))
        self.frm_main.Show()
        
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
        
if __name__ == "__main__":
    app = SampleApp(False)
    app.MainLoop()
