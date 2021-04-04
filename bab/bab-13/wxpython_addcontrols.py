##################################################
# Nama file: wxpython_addcontrols.py
##################################################

import wx

class MainFrame(wx.Frame):
   def __init__(self, parent):
      wx.Frame.__init__(self, parent,
                      title="Frame dengan Button",
                      size=(400, 200))
      
      # menempatkan panel di dalam frame
      panel = wx.Panel(self)

      # menempatkan button di atas panel
      button = wx.Button(panel, label="Keluar",
                         pos=(150, 55),
                         size=(90, 30))

if __name__ == "__main__":
   app = wx.App()
   mainform = MainFrame(None)
   mainform.Show()
   app.MainLoop()
