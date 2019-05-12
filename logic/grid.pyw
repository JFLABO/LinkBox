# -*- coding: utf-8 -*-
import wx
import wx.grid
import glob
import webbrowser

class GridFrame(wx.Frame):
    def __init__(self, parent):
        f=wx.Frame.__init__(self, parent)
        #f.setSize(100,650)
        # Create a wxGrid object
        grid = wx.grid.Grid(self, -1)

        # Then we call CreateGrid to set the dimensions of the grid
        # (100 rows and 10 columns in this example)
        grid.CreateGrid(50, 3)

        # We can set the sizes of individual rows and columns
        # in pixels
        grid.SetRowSize(0, 20)
        grid.SetColSize(0, 640)

        # And set grid cell contents as strings
        #grid.SetCellValue(0, 0, 'wxGrid is good')
        i=0
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
            i=i+1
            
        grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.click)
        self.Show()
        
    def GetValue(self, row, col):
        return self.data[row][col]
    
    def click(self, event):
        obj = event.GetEventObject()
        print(vars(self))
        print(vars(event))
        print(obj)
        url=obj.GetCellValue(1,1)
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
    #frame.set_window_size(100,470)
    #frame.SetDimensions(0,0,840,480)
    frame.SetSize(0,0,840,480)
    app.MainLoop()

#magic
