##################################################
# Nama file: wxpython_vsizebox.py
##################################################

import wx

class MainFrame(wx.Frame):	
   def __init__(self, parent):
      wx.Frame.__init__ (self, parent, id = wx.ID_ANY,
                         title = "Demo Vertical SizeBox",
                         pos = wx.DefaultPosition,
                         size = wx.Size(345,160),
                         style = wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
		
      self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
		
      sizer = wx.BoxSizer(wx.VERTICAL)
		
      self.button1 = wx.Button(self, wx.ID_ANY, "Button 1",
                               wx.DefaultPosition, wx.DefaultSize, 0)
      sizer.Add(self.button1, 0, wx.ALL, 5)
		
      self.button2 = wx.Button(self, wx.ID_ANY, "Button 2",
                               wx.DefaultPosition, wx.DefaultSize, 0)
      sizer.Add(self.button2, 0, wx.ALL, 5)
		
      self.SetSizer(sizer)
      self.Layout()
		
      self.Centre(wx.BOTH)
      
if __name__ == "__main__":
   app = wx.App()
   mainform = MainFrame(None)
   mainform.Show()
   app.MainLoop()
