##################################################
# Nama file: wxpython_frameposition2.py
##################################################

import wx

def main():
   app = wx.App()
   frame = wx.Frame(None, -1, 'Program Minimal',
                    style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU |
                            wx.SYSTEM_MENU | wx.CAPTION |
                            wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                    size = (500, 350))
	
   # menentukan posisi form
   frame.SetPosition((500, 250))
   
   frame.Show()
   app.MainLoop()

if __name__ == "__main__":
   main()
