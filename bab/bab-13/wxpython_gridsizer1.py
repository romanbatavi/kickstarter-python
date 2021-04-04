##################################################
# Nama file: wxpython_gridsizer1.py
##################################################

import wx

class MainFrame(wx.Frame):
   def __init__(self, parent):
      wx.Frame.__init__ (self, parent, id = wx.ID_ANY,
                         title = "Demo GridSizer",
                         pos = wx.DefaultPosition,
                         size = wx.Size(300,110),
                         style = wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
		
      self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
		
      self.panel = wx.Panel(self)
      
      # bentuk konstruktor: GridSizer(rows, cols, vgap, hgap)
      sizer = wx.GridSizer(2, 3, 5, 5)
		
      self.button1 = wx.Button(self.panel, wx.ID_ANY, "Button 1",
                               wx.DefaultPosition, wx.DefaultSize, 0)
      sizer.Add(self.button1, 0, wx.ALL, 2)

      self.button2 = wx.Button(self.panel, wx.ID_ANY, "Button 2",
                               wx.DefaultPosition, wx.DefaultSize, 0)
      sizer.Add(self.button2, 0, wx.ALL, 2)
      
      self.button3 = wx.Button(self.panel, wx.ID_ANY, "Button 3",
                               wx.DefaultPosition, wx.DefaultSize, 0)
      sizer.Add(self.button3, 0, wx.ALL, 2)

      self.button4 = wx.Button(self.panel, wx.ID_ANY, "Button 4",
                               wx.DefaultPosition, wx.DefaultSize, 0)
      sizer.Add(self.button4, 0, wx.ALL, 2)

      self.button5 = wx.Button(self.panel, wx.ID_ANY, "Button 5",
                               wx.DefaultPosition, wx.DefaultSize, 0)
      sizer.Add(self.button5, 0, wx.ALL, 2)
      
      self.button6 = wx.Button(self.panel, wx.ID_ANY, "Button 6",
                               wx.DefaultPosition, wx.DefaultSize, 0)
      sizer.Add(self.button6, 0, wx.ALL, 2)
      
      self.panel.SetSizer(sizer)
      
      self.Layout()		
      self.Centre(wx.BOTH)
		
if __name__ == "__main__":
   app = wx.App()
   mainform = MainFrame(None)
   mainform.Show()
   app.MainLoop()
