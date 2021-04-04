##################################################
# Nama file: wxpython_staticsizebox.py
##################################################

import wx

class MainFrame(wx.Frame):
   def __init__(self, parent):
      wx.Frame.__init__ (self, parent, id = wx.ID_ANY,
                         title = "Demo StaticBoxSizer",
                         pos = wx.DefaultPosition,
                         size = wx.Size(300,300),
                         style = wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
		
      self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
		
      self.panel = wx.Panel(self)

      box = wx.StaticBox(self.panel, -1, "Judul Box")
            
      sizer = wx.StaticBoxSizer(box, wx.VERTICAL)
		
      self.button1 = wx.Button(self.panel, wx.ID_ANY, "Button 1",
                               wx.DefaultPosition, wx.DefaultSize, 0)
      sizer.Add(self.button1, 0, wx.ALL, 5)

      self.button2 = wx.Button(self.panel, wx.ID_ANY, "Button 2",
                               wx.DefaultPosition, wx.DefaultSize, 0)
      sizer.Add(self.button2, 0, wx.ALL, 5)
      
      self.button3 = wx.Button(self.panel, wx.ID_ANY, "Button 3",
                               wx.DefaultPosition, wx.DefaultSize, 0)
      sizer.Add(self.button3, 0, wx.ALL, 5)
      
      self.panel.SetSizer(sizer)
      
      self.Layout()		
      self.Centre(wx.BOTH)
		
if __name__ == "__main__":
   app = wx.App()
   mainform = MainFrame(None)
   mainform.Show()
   app.MainLoop()
