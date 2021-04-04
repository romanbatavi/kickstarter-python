##################################################
# Nama file: wxpython_event1.py
##################################################

import wx

class MainFrame(wx.Frame):
   def __init__(self, parent):
      wx.Frame.__init__(self, parent,
                      title="Demo Event 1",
                      size=(400, 200))
      
      # menempatkan panel di dalam frame
      panel = wx.Panel(self)

      # menempatkan button di atas panel
      button = wx.Button(panel, label="Keluar",
                         pos=(150, 55),
                         size=(90, 30))

      self.Bind(wx.EVT_BUTTON, self.OnClick, button)

   def OnClick(self, event):
      self.Close(True)	# menutup frame
      self.Destroy()	# membuang objek frame dari memori

if __name__ == "__main__":
   app = wx.App()
   mainform = MainFrame(None)
   mainform.Show()
   app.MainLoop()
