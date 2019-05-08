# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from LinkBox import Ui_Dialog

class Test(QtWidgets.QDialog):
  def __init__(self,parent=None):
    super(Test, self).__init__(parent)
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)
    #def slot1(self): #イベント処理の関数
    #self.ui.label.setText('Hello World!')

if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  window = Test()
  window.show()
  sys.exit(app.exec_())

#magic
