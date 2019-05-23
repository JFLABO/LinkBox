# -*- coding: utf-8 -*-
#UI Demo (c)2019 JFLABO GNU

# Form implementation generated from reading ui file 'LinkBox.ui',
# licensing of 'LinkBox.ui' applies.
#
# Created: Fri May 24 08:08:31 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!
import wx
from PySide2 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QDialog

#from ui_mainwindow import Ui_MainWindow

class Ui_Dialog(object):
    #def __init__(self):
        #super(Ui_Dialog, self).__init__()
        #self.ui = Ui_Dialog()
        #self.ui.setupUi(self)
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(794, 555)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(610, 520, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(0, 40, 111, 471))
        self.listView.setObjectName("listView")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(450, 0, 256, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(710, 0, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(120, 40, 661, 471))
        self.tableView.setObjectName("tableView")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 431, 41))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 86, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(90, 20, 86, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(170, 20, 86, 16))
        self.radioButton_3.setObjectName("radioButton_3")

        self.retranslateUi(Dialog)
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Dialog", "検索", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Dialog", "並べ替え", None, -1))
        self.radioButton.setText(QtWidgets.QApplication.translate("Dialog", "登録日順", None, -1))
        self.radioButton_2.setText(QtWidgets.QApplication.translate("Dialog", "優先度順", None, -1))
        self.radioButton_3.setText(QtWidgets.QApplication.translate("Dialog", "重要度順", None, -1))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    #app = QtGui.QApplication(sys.argv)
    #Dialog = QtGui.QDialog()
    #ui = Ui_Dialog()
    #ui.setupUi(Dialog)
    #Dialog.show()
    #sys.exit(app.exec_())
    #app = wx.App(0)
    #Ui_Dialog()
    
    #app = QApplication(sys.argv)
    #window = QDialog()
    #form = Ui_Dialog()
    #form.setupUi(window)
    #window.show()
    #form.show()
    #self.ui = Ui_Dialog()
    #self.ui.setupUi(self)
    #self.ui = Ui_Dialog()
    #self.ui.setupUi(self)
    #frame  = Ui_Dialog()
    #frame.setupUi(self)
    #app.MainLoop()

