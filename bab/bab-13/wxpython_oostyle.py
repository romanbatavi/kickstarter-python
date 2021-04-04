##################################################
# Nama file: wxpython_oostyle.py
##################################################

import wx

# mendefinisikan kelas MainFrame
class MainFrame(wx.Frame):
   def __init__(self, parent, ID, title,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.DEFAULT_FRAME_STYLE):
      # memanggil konstruktor wx.Frame
      wx.Frame.__init__(self, parent, ID,
                        title, pos, size, style)

if __name__ == "__main__":
   app = wx.App()

   # membuat objek dari kelas MyFrame
   mainform = MainFrame(None, -1, "Program Minimal")
   mainform.Show()

   app.MainLoop()
