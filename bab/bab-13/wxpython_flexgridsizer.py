##################################################
# Nama file: wxpython_flexgridsizer.py
##################################################

import wx

class MainFrame(wx.Frame):	
   def __init__(self, parent):
      wx.Frame.__init__(self, parent, id = wx.ID_ANY,
                        title = "SMS Sender",
                        pos = wx.DefaultPosition,
                        size = wx.Size(408,218),
                        style = wx.DEFAULT_FRAME_STYLE | 
                        wx.TAB_TRAVERSAL)
		
      self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
      self.SetBackgroundColour(
           wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
		
      fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
      fgSizer1.SetFlexibleDirection(wx.BOTH)
      fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
		
      self.statictext1 = wx.StaticText(self, wx.ID_ANY, "No. HP",
                                       wx.DefaultPosition,
                                       wx.Size(70,-1), 0)
      self.statictext1.Wrap(-1)
      fgSizer1.Add(self.statictext1, 0, wx.ALL, 5)
		
      self.textctrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                   wx.DefaultPosition,
                                   wx.Size(300,-1), 0)
      fgSizer1.Add(self.textctrl1, 0, wx.ALL, 5)
		
      self.statictext2 = wx.StaticText(self, wx.ID_ANY, "Pesan",
                                       wx.DefaultPosition,
                                       wx.Size(70,-1), 0)
      self.statictext2.Wrap(-1)
      fgSizer1.Add(self.statictext2, 0, wx.ALL, 5)
		
      self.textctrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                   wx.DefaultPosition, wx.Size(300,100),
                                   wx.TE_MULTILINE)
      fgSizer1.Add(self.textctrl2, 0, wx.ALL, 5)
				
      fgSizer1.AddSpacer(5)
		
      self.button1 = wx.Button(self, wx.ID_ANY, "&Kirim SMS",
                               wx.DefaultPosition,
                               wx.DefaultSize, 0)
      fgSizer1.Add(self.button1, 0, wx.ALL, 5)
		
      self.SetSizer(fgSizer1)
      self.Layout()
		
      self.Centre(wx.BOTH)
		
if __name__ == "__main__":
   app = wx.App()
   mainform = MainFrame(None)
   mainform.Show()
   app.MainLoop()
