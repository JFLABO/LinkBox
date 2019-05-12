# -*- coding: utf-8 -*-
import wx
import wx.grid
import glob

class GridFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)

        # Create a wxGrid object
        grid = wx.grid.Grid(self, -1)

        # Then we call CreateGrid to set the dimensions of the grid
        # (100 rows and 10 columns in this example)
        grid.CreateGrid(50, 1)

        # We can set the sizes of individual rows and columns
        # in pixels
        grid.SetRowSize(0, 60)
        grid.SetColSize(0, 120)

        # And set grid cell contents as strings
        #grid.SetCellValue(0, 0, 'wxGrid is good')
        i=0
        for name in glob.iglob('../**/*.url', recursive=True):
        #print(name)
            grid.SetCellValue(i, 0, name)
            i=i+1
      self.Show()

if __name__ == '__main__':

    app = wx.App(0)
    frame = GridFrame(None)
    app.MainLoop()

#magic
