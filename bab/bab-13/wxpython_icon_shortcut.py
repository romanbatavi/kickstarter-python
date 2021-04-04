##################################################
# Nama file: wxpython_icon_shortcut.py
##################################################

import wx
import locale

class MainFrame(wx.Frame):	
   def __init__(self, parent):
      wx.Frame.__init__(self, parent, id = wx.ID_ANY,
                        title = "Demo Icon dan Shortcut",
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

      # membuat menu
      self.filemenu = wx.Menu()

      # membuat item
      self.filemenuitem = wx.MenuItem(self.filemenu, wx.ID_EXIT,
                                      "Keluar\tCtrl+A")      

      # membuat icon
      locale = wx.Locale(wx.LANGUAGE_ENGLISH)
      self.filemenuitem.SetBitmap(wx.Bitmap("delete.png"))

      # menambahkan item menu ke menu
      self.filemenu.Append(self.filemenuitem)

      self.Bind(wx.EVT_MENU, self.onExit, self.filemenuitem)

      # menempatkan menu ke dalam menubar
      self.menubar.Append(self.filemenu, "&File")

      # menempatkan menubar ke dalam frame
      self.SetMenuBar(self.menubar)    
 				
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
