##################################################
# Nama file: wxpython_mixsizebox.py
##################################################

import wx

class MainFrame(wx.Frame):
   def __init__(self, parent):
      wx.Frame.__init__(self, parent, id = wx.ID_ANY,
                        title = "Kamus",
                        pos = wx.DefaultPosition,
                        size = wx.Size(533,450),
                        style = wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
		
      self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
		
      sizer = wx.BoxSizer(wx.VERTICAL)
		
      self.statictext1 = wx.StaticText(self, wx.ID_ANY,
                                       "Masukkan kata yang dicari",
                                       wx.DefaultPosition,
                                       wx.DefaultSize, 0 )
      self.statictext1.Wrap(-1)
      sizer.Add(self.statictext1, 0, wx.ALL, 5)
		
      hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
		
      self.textctrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                   wx.DefaultPosition, wx.DefaultSize, 0)
      hsizer1.Add(self.textctrl1, 1, wx.ALL, 5)
		
      self.button1 = wx.Button(self, wx.ID_ANY, "&Cari",
                               wx.DefaultPosition, wx.DefaultSize, 0)
      hsizer1.Add(self.button1, 0, wx.ALL, 5)
		
      sizer.Add(hsizer1, 0, wx.EXPAND, 5)
		
      self.checkbox1 = wx.CheckBox(self, wx.ID_ANY,
         "Case insensitive (tidak membedakan huruf kecil dan huruf besar)",
         wx.DefaultPosition, wx.DefaultSize, 0)
      self.checkbox1.SetValue(True) 
      sizer.Add(self.checkbox1, 0, wx.ALL, 5)
		
      self.statictext2 = wx.StaticText(self, wx.ID_ANY,
                                       "Daftar kata",
                                       wx.DefaultPosition,
                                       wx.DefaultSize, 0)
      self.statictext2.Wrap(-1)
      sizer.Add(self.statictext2, 0, wx.ALL, 5)
		
      listbox1Choices = []
      self.listbox1 = wx.ListBox(self, wx.ID_ANY,
                                 wx.DefaultPosition,
                                 wx.Size(-1,140),
                                 listbox1Choices, 0)
      sizer.Add(self.listbox1, 0, wx.ALL|wx.EXPAND, 5)
		
      self.statictext3 = wx.StaticText( self, wx.ID_ANY,
                                        "Arti (terjemahan)",
                                        wx.DefaultPosition,
                                        wx.DefaultSize, 0)
      self.statictext3.Wrap(-1)
      sizer.Add(self.statictext3, 0, wx.ALL, 5)
		
      self.textctrl2 = wx.TextCtrl(self, wx.ID_ANY,
                                   wx.EmptyString,
                                   wx.DefaultPosition,
                                   wx.Size(-1,60),
                                   wx.TE_MULTILINE | wx.TE_READONLY)
      sizer.Add(self.textctrl2, 0,
                wx.ALL | wx.EXPAND, 5)
		
      self.staticline1 = wx.StaticLine(self, wx.ID_ANY,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.LI_HORIZONTAL)
      sizer.Add(self.staticline1, 0, wx.EXPAND | wx.ALL, 5)
		
      hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
		
      hsizer2.AddSpacer(5)
		
      self.button2 = wx.Button(self, wx.ID_ANY,
                               "&Keluar",
                               wx.DefaultPosition,
                               wx.DefaultSize, 0)
      hsizer2.Add(self.button2, 0, wx.ALL, 5)		
		
      sizer.Add(hsizer2, 1, wx.EXPAND, 5)		
		
      self.SetSizer(sizer)
      self.Layout()
		
      self.Centre(wx.BOTH)
		
if __name__ == "__main__":
   app = wx.App()
   mainform = MainFrame(None)
   mainform.Show()
   app.MainLoop()
