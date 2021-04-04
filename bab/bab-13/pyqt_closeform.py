#########################################################
# Nama file: pyqt_closeform.py
#########################################################

import sys
from PyQt5.QtWidgets import *

class MainForm(QWidget):
   def __init__(self):
      super().__init__()
      self.setupUi()
      
   def setupUi(self):
      self.resize(300, 200)
      self.move(300, 300)
      self.setWindowTitle('Demo Menutup Form')
      
      self.button = QPushButton('Tutup')
      self.button.move(50,50)
      self.button.setParent(self)
      
      self.button.clicked.connect(self.buttonClick)

   def buttonClick(self):
      self.close()

if __name__ == '__main__':
   a = QApplication(sys.argv)
      
   form = MainForm()
   form.show()
   
   a.exec_()
