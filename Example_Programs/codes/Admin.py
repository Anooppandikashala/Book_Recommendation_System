# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Invalid import Ui_InvalidAdmin
from Training import Ui_Training

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

class Ui_AdminLogin(object):
    def checkInvalidLogin(self):
    	self.trainWindow=QtGui.QWidget()
    	self.ui = Ui_InvalidAdmin()
    	self.ui.setupUi(self.trainWindow)
    	self.trainWindow.show()
    	
    def checkValidLogin(self):
    	self.validLogin=QtGui.QMainWindow()
    	self.ui = Ui_Training()
    	self.ui.setupUi(self.validLogin)
    	self.validLogin.show()
    	
    	#AdminLogin.close()
    def loginCheck(self):
    	usrname=self.textEditUsername.text()
    	psswrd=self.textEditPassword.text()
    	
    	if(usrname=="admin" and psswrd=="admin123"):
    		print("logined successful")
    		self.checkValidLogin()
    		
    		
    	else:
    		print("Invalid Admin Entry")
    		self.checkInvalidLogin()
    	
    	
    	
    def setupUi(self, AdminLogin):
        AdminLogin.setObjectName(_fromUtf8("AdminLogin"))
        AdminLogin.resize(576, 480)
        AdminLogin.setMinimumSize(QtCore.QSize(576, 480))
        AdminLogin.setMaximumSize(QtCore.QSize(576, 480))
        self.verticalLayoutWidget = QtGui.QWidget(AdminLogin)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 551, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtGui.QWidget(AdminLogin)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(15, 250, 551, 50))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(AdminLogin)
        self.label_3.setGeometry(QtCore.QRect(120, 310, 81, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(AdminLogin)
        self.label_4.setGeometry(QtCore.QRect(120, 360, 81, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        
        
        self.textEditUsername = QtGui.QLineEdit(AdminLogin)
        self.textEditUsername.setGeometry(QtCore.QRect(230, 310, 241, 21))
        self.textEditUsername.setObjectName(_fromUtf8("textEditUsername"))
        self.textEditPassword = QtGui.QLineEdit(AdminLogin)
        self.textEditPassword.setGeometry(QtCore.QRect(230, 360, 241, 21))
        self.textEditPassword.setEchoMode(QtGui.QLineEdit.Password)
        
        
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditPassword.sizePolicy().hasHeightForWidth())
        self.textEditPassword.setSizePolicy(sizePolicy)
        self.textEditPassword.setObjectName(_fromUtf8("textEditPassword"))
        self.BtnLogin = QtGui.QPushButton(AdminLogin)
        self.BtnLogin.setGeometry(QtCore.QRect(370, 410, 99, 27))
        self.BtnLogin.setObjectName(_fromUtf8("BtnLogin"))
        
        ###################################################
        self.BtnLogin.clicked.connect(self.loginCheck)
        
        ###################################################
        
        self.verticalLayoutWidget_3 = QtGui.QWidget(AdminLogin)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 70, 551, 171))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setMinimumSize(QtCore.QSize(549, 169))
        self.label_6.setMaximumSize(QtCore.QSize(549, 169))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8(":/StartPage/book1112.jpg")))
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)

        self.retranslateUi(AdminLogin)
        QtCore.QObject.connect(self.BtnLogin, QtCore.SIGNAL(_fromUtf8("clicked()")), AdminLogin.close)
        QtCore.QMetaObject.connectSlotsByName(AdminLogin)

    def retranslateUi(self, AdminLogin):
        AdminLogin.setWindowTitle(_translate("AdminLogin", "Admin Login", None))
        self.label.setText(_translate("AdminLogin", "BOOK RECOMMENDATION SYSTEM ", None))
        self.label_2.setText(_translate("AdminLogin", "Admin Login", None))
        self.label_3.setText(_translate("AdminLogin", "Username :", None))
        self.label_4.setText(_translate("AdminLogin", "Password :", None))
        self.BtnLogin.setText(_translate("AdminLogin", "Login...!", None))

import logo_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AdminLogin = QtGui.QWidget()
    ui = Ui_AdminLogin()
    ui.setupUi(AdminLogin)
    AdminLogin.show()
    sys.exit(app.exec_())

