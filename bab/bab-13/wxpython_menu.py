##################################################
# Nama file: wxpython_menu.py
##################################################

import wx

class MainFrame(wx.Frame):	
   def __init__(self, parent):
      wx.Frame.__init__(self, parent, id = wx.ID_ANY,
                        title = "Demo Menu",
                        pos = wx.DefaultPosition,
                        size = wx.Size(300,200),
                        style = wx.DEFAULT_FRAME_STYLE |
                                wx.TAB_TRAVERSAL)
		
      self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
      self.SetBackgroundColour(
         wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
		
      sizer = wx.BoxSizer(wx.VERTICAL)

      # membuat menubar
      self.menubar = wx.MenuBar()

      # menempatkan menubar ke dalam frame
      self.SetMenuBar(self.menubar)    

      # membuat menu
      self.filemenu = wx.Menu()

      # menempatkan menu ke dalam menubar
      self.menubar.Append(self.filemenu, "&File")

      # membuat item untuk menu File
      self.filemenuitem = self.filemenu.Append(wx.ID_EXIT,
                                               "Keluar")

      self.Bind(wx.EVT_MENU, self.onExit, self.filemenuitem)
				
      self.SetSizer(sizer)
      self.Layout()
		
      self.Centre(wx.BOTH)

   def onExit(self, event):
      self.Close()
      
if __name__ == "__main__":
   app = wx.App()
   mainform = MainFrame(None)
   mainform.Show()
   app.MainLoop()
