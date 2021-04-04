##################################################
# Nama file: wxpython_gridbagsizer.py
##################################################

import wx
import wx.grid

class MainFrame(wx.Frame):	
   def __init__(self, parent):
      wx.Frame.__init__(self, parent, id = wx.ID_ANY,
                        title = "Demo GridBagSizer",
                        pos = wx.DefaultPosition,
                        size = wx.Size(499,248),
                        style = wx.DEFAULT_FRAME_STYLE |
                                wx.TAB_TRAVERSAL )
		
      self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
      self.SetBackgroundColour(
         wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
		
      sizer = wx.GridBagSizer(0, 0)
      sizer.SetFlexibleDirection(wx.BOTH)
      sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
		
      self.statictext1 = wx.StaticText(self, wx.ID_ANY, "Data Pelanggan",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
      self.statictext1.Wrap(-1)
      self.statictext1.SetFont(wx.Font(14, 74, 90,
                                       92, False, "Arial"))
		
      sizer.Add(self.statictext1,
                wx.GBPosition(0, 0),
                wx.GBSpan(1, 5),
                wx.ALIGN_CENTER | wx.ALL, 5)
		
      self.grid1 = wx.grid.Grid(self, wx.ID_ANY,
                                wx.DefaultPosition,
                                wx.DefaultSize, 0)
      
      self.grid1.CreateGrid(5, 5)
      self.grid1.EnableEditing(True)
      self.grid1.EnableGridLines(True)
      self.grid1.EnableDragGridSize(False)
      self.grid1.SetMargins(0, 0)
		
      self.grid1.EnableDragColMove(False)
      self.grid1.EnableDragColSize(True)
      self.grid1.SetColLabelSize(30)
      self.grid1.SetColLabelValue(0, "ID")
      self.grid1.SetColLabelValue(1, "Nama")
      self.grid1.SetColLabelValue(2, "Alamat")
      self.grid1.SetColLabelValue(3, "Kota")
      self.grid1.SetColLabelValue(4, "No. HP")
      self.grid1.SetColLabelAlignment(wx.ALIGN_CENTRE,
                                      wx.ALIGN_CENTRE)
      
      self.grid1.EnableDragRowSize(True)
      self.grid1.SetRowLabelSize(80)
      self.grid1.SetRowLabelAlignment(wx.ALIGN_CENTRE,
                                      wx.ALIGN_CENTRE)
		
      self.grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT,
                                         wx.ALIGN_TOP)
      sizer.Add(self.grid1,
                wx.GBPosition(1, 0),
                wx.GBSpan(1, 5),
                wx.ALL, 5)
		
      self.staticline1 = wx.StaticLine(self, wx.ID_ANY,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.LI_HORIZONTAL)
      sizer.Add(self.staticline1,
                wx.GBPosition(2, 0),
                wx.GBSpan(1, 5),
                wx.EXPAND | wx.ALL, 5)
		
      self.button1 = wx.Button(self, wx.ID_ANY, "&Tambah",
                               wx.DefaultPosition,
                               wx.DefaultSize, 0)
      sizer.Add(self.button1, wx.GBPosition(3, 0),
                wx.GBSpan(1, 1), wx.ALL, 5)
		
      self.button2 = wx.Button(self, wx.ID_ANY, "&Ubah",
                               wx.DefaultPosition,
                               wx.DefaultSize, 0)
      sizer.Add(self.button2, wx.GBPosition(3, 1),
                wx.GBSpan(1, 1),
                wx.ALL, 5)
		
      self.button3 = wx.Button(self, wx.ID_ANY,
                               "&Hapus", wx.DefaultPosition,
                               wx.DefaultSize, 0)
      sizer.Add(self.button3, wx.GBPosition(3, 2),
                wx.GBSpan(1, 1), wx.ALL, 5)
		
      self.button4 = wx.Button(self, wx.ID_ANY,
                               "&Keluar", wx.DefaultPosition,
                               wx.DefaultSize, 0)
      sizer.Add(self.button4, wx.GBPosition(3, 4),
                wx.GBSpan(1, 1), wx.ALL, 5)
				
      self.SetSizer(sizer)
      self.Layout()
		
      self.Centre(wx.BOTH)
		
if __name__ == "__main__":
   app = wx.App()
   mainform = MainFrame(None)
   mainform.Show()
   app.MainLoop()
