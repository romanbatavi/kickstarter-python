#########################################################
# Nama file: pyqt_minimal1.py
#########################################################

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class MinimalForm(QWidget):
   def __init__(self):
      super().__init__()
      self.setupUi()
      
   def setupUi(self):
      self.resize(200, 100)
      self.move(300, 300)
      self.setWindowTitle('GUI Minimal')
      
      self.label = QLabel('Hello PyQt5')
      self.label.move(55,40)
      self.label.setParent(self)

if __name__ == '__main__':
   a = QApplication(sys.argv)
      
   minform = MinimalForm()
   minform.show()
   
   a.exec_()
