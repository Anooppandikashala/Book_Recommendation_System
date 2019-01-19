# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Welcome.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from test import Ui_Test
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Welcome(object):

    def checkGo(self):
    	self.test=QtGui.QMainWindow()
    	self.ui = Ui_Test()
    	self.ui.setupUi(self.test)
    	self.test.show()
    def setupUi(self, Welcome):
        Welcome.setObjectName(_fromUtf8("Welcome"))
        Welcome.resize(569, 503)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/StartPage/network.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Welcome.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtGui.QWidget(Welcome)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 431, 441))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(429, 439))
        self.label.setMaximumSize(QtCore.QSize(429, 439))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/StartPage/new.jpg")))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayoutWidget = QtGui.QWidget(Welcome)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(460, 20, 101, 461))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.BtnGo = QtGui.QPushButton(self.verticalLayoutWidget)
        self.BtnGo.setObjectName(_fromUtf8("BtnGo"))
        self.verticalLayout.addWidget(self.BtnGo)
        
	###################################################
        self.BtnGo.clicked.connect(self.checkGo)
        
        ###################################################
        self.retranslateUi(Welcome)
        QtCore.QObject.connect(self.BtnGo, QtCore.SIGNAL(_fromUtf8("clicked()")), Welcome.close)
        QtCore.QMetaObject.connectSlotsByName(Welcome)

    def retranslateUi(self, Welcome):
        Welcome.setWindowTitle(_translate("Welcome", "Welcome", None))
        self.BtnGo.setText(_translate("Welcome", "Go..!", None))

import logo_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Welcome = QtGui.QWidget()
    ui = Ui_Welcome()
    ui.setupUi(Welcome)
    Welcome.show()
    sys.exit(app.exec_())

