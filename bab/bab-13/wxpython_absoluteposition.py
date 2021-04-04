##################################################
# Nama file: wxpython_absoluteposition.py
##################################################

import wx

class MainFrame(wx.Frame):
   def __init__(self, parent):
      wx.Frame.__init__(self, parent,
                      title="Demo posisi absolut",
                      size=(282, 203))
      
      # menempatkan panel di dalam frame
      self.panel = wx.Panel(self)

      # membuat menubar
      self.menubar = wx.MenuBar()
      # membuat menu
      self.filemenu = wx.Menu()
      self.editmenu = wx.Menu()

      # menambahkan menu ke menubar
      self.menubar.Append(self.filemenu, "&File")
      self.menubar.Append(self.editmenu, "&Edit")

      # menempatkan menubar di atas panel
      self.SetMenuBar(self.menubar)

      # menempatkan TextCtrl di atas panel
      self.textctrl = wx.TextCtrl(self.panel,
                         pos=(3, 3),
                         size=(260, 140),
                         style=wx.TE_MULTILINE)
      
if __name__ == "__main__":
   app = wx.App()
   mainform = MainFrame(None)
   mainform.Show()
   app.MainLoop()
