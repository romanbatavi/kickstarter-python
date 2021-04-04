##################################################
# Nama file: wxpython_event2.py
##################################################

import wx

class MainFrame(wx.Frame):
   def __init__(self, parent):
      wx.Frame.__init__(self, parent,
                      title="Frame dengan dua Button",
                      size=(400, 200))
      
      # menempatkan panel di dalam frame
      self.panel = wx.Panel(self)

      # menempatkan text control di atas panel
      self.text = wx.TextCtrl(self.panel,
                         pos=(100, 30),
                         size=(185, 20))

      # menempatkan button1 di atas panel
      self.button1 = wx.Button(self.panel, label="Hello",
                         pos=(100, 55),
                         size=(90, 30))
      
      # menempatkan button2 di atas panel
      self.button2 = wx.Button(self.panel, label="Keluar",
                         pos=(195, 55),
                         size=(90, 30))

      # event-handler ketika button1 di-klik
      self.Bind(wx.EVT_BUTTON, self.OnButton1Click, self.button1)
      
      # event-handler ketika button2 di-klik
      self.Bind(wx.EVT_BUTTON, self.OnButton2Click, self.button2)

   def OnButton1Click(self, event):
      self.text.SetValue("Hello wxPython!")

   def OnButton2Click(self, event):
      self.Close(True)
      self.Destroy()

if __name__ == "__main__":
   app = wx.App()
   mainform = MainFrame(None)
   mainform.Show()
   app.MainLoop()
