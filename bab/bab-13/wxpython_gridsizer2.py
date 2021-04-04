##################################################
# Nama file: wxpython_gridsizer2.py
##################################################

import wx

class MainFrame(wx.Frame):	
   def __init__(self, parent):
      wx.Frame.__init__(self, parent, id = wx.ID_ANY,
                        title = "Login",
                        pos = wx.DefaultPosition,
                        size = wx.Size(410,145),
                        style = wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
		
      self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
      self.SetBackgroundColour(
           wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
		
      sizer = wx.GridSizer(0, 2, 0, 0)
		
      self.statictext1 = wx.StaticText(self, wx.ID_ANY, "Username",
                                       wx.DefaultPosition,
                                       wx.DefaultSize, 0)
      self.statictext1.Wrap(-1)
      sizer.Add(self.statictext1, 0, wx.ALL, 5)
		
      self.textctrl1 = wx.TextCtrl(self, wx.ID_ANY,
                                   wx.EmptyString,
                                   wx.DefaultPosition,
                                   wx.Size(184,-1), 0)
      sizer.Add(self.textctrl1, 1, wx.ALL, 5)
		
      self.statictext2 = wx.StaticText(self, wx.ID_ANY, "Password",
                                       wx.DefaultPosition,
                                       wx.DefaultSize, 0)
      self.statictext2.Wrap(-1)
      sizer.Add(self.statictext2, 0, wx.ALL, 5)
		
      self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY,
                                     wx.EmptyString,
                                     wx.DefaultPosition,
                                     wx.Size(184,-1),
                                     wx.TE_PASSWORD)
      sizer.Add(self.m_textCtrl4, 0, wx.ALL, 5)
				
      sizer.AddSpacer(5)
		
      hsizer = wx.BoxSizer(wx.HORIZONTAL)
		
      self.button1 = wx.Button(self, wx.ID_ANY, "&Login",
                               wx.DefaultPosition,
                               wx.DefaultSize, 0)
      hsizer.Add(self.button1, 0, wx.ALL, 5)
		
      self.button2 = wx.Button(self, wx.ID_ANY, "E&xit",
                               wx.DefaultPosition,
                               wx.DefaultSize, 0)
      hsizer.Add(self.button2, 0, wx.ALL, 5)		
		
      sizer.Add(hsizer, 1, wx.EXPAND, 5)		
		
      self.SetSizer(sizer)
      self.Layout()
		
      self.Centre(wx.BOTH)
		
if __name__ == "__main__":
   app = wx.App()
   mainform = MainFrame(None)
   mainform.Show()
   app.MainLoop()
