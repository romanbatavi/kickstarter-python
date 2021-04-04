#########################################################
# Nama file: pyqt_centerform.py
#########################################################

import sys
from PyQt5.QtWidgets import *

class MainForm(QWidget):
   def __init__(self):
      super().__init__()
      self.setupUi()
      
   def setupUi(self):
      self.resize(300, 200)
      self.setCenter()            
      self.setWindowTitle('Demo Form di Tengah Layar')

   def setCenter(self):
      desktop = QDesktopWidget()
      
      screenwidth = desktop.screen().width()
      screenheight = desktop.screen().height()
      
      self.setGeometry((screenwidth - self.width()) // 2,
                       (screenheight - self.height()) // 2,
                       self.width(),
                       self.height())

if __name__ == '__main__':
   a = QApplication(sys.argv)
      
   form = MainForm()
   form.show()
   
   a.exec_()
