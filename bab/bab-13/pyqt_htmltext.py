#########################################################
# Nama file: pyqt_htmltext.py
#########################################################

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class TextForm(QWidget):
   def __init__(self):
      super().__init__()
      self.setupUi()
      
   def setupUi(self):
      self.resize(300, 200)
      self.move(300, 300)
      self.setWindowTitle('Demo Tag HTML')
      
      self.label1 = QLabel('<h1>Hello <font color=blue>PyQt5</font></h1>')
      self.label1.move(10,10)
      self.label1.setParent(self)
      
      self.label2 = QLabel('''
      Contoh teks yang dibuat dengan tag HTML. Teks dapat dijadikan <b>tebal</b>,
      <i>miring</i>, dan <u>bergaris bawah</i>
      ''')      
      self.label2.setWordWrap(True)
      self.label2.move(10,50)
      self.label2.setParent(self)

if __name__ == '__main__':
   a = QApplication(sys.argv)
      
   form = TextForm()
   form.show()
   
   a.exec_()
