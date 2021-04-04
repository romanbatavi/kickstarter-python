#########################################################
# Nama file: pyqt_qgridlayout.py
#########################################################

import sys
from PyQt5.QtWidgets import *

class MainForm(QWidget):
   def __init__(self):
      super().__init__()
      self.setupUi()
      
   def setupUi(self):
      self.resize(400, 100)
      self.move(300, 300)
      self.setWindowTitle('Demo QGridLayout')

      self.button1 = QPushButton('Button 1')
      self.button2 = QPushButton('Button 2')
      self.button3 = QPushButton('Button 3')
      self.button4 = QPushButton('Button 4')
      self.button5 = QPushButton('Button 5')
      self.button6 = QPushButton('Button 6')
      
      layout = QGridLayout()
      layout.addWidget(self.button1, 0, 0)
      layout.addWidget(self.button2, 0, 1)
      layout.addWidget(self.button3, 0, 2)
      layout.addWidget(self.button4, 1, 0)
      layout.addWidget(self.button5, 1, 1)
      layout.addWidget(self.button6, 1, 2)
      
      self.setLayout(layout)

if __name__ == '__main__':
   a = QApplication(sys.argv)
      
   form = MainForm()
   form.show()
   
   a.exec_()
