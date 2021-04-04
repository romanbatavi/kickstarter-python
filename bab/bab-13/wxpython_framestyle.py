##################################################
# Nama file: wxpython_framestyle.py
##################################################

import wx

def main():
   app = wx.App()
   frame = wx.Frame(None, -1, 'Program Minimal',
                    style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU |
                            wx.SYSTEM_MENU | wx.CAPTION |
                            wx.CLOSE_BOX | wx.CLIP_CHILDREN)
   frame.Show()
   app.MainLoop()

if __name__ == "__main__":
   main()
