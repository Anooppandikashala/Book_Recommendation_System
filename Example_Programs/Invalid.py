# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Invalid.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_InvalidAdmin(object):
    
    def setupUi(self, InvalidAdmin):
        InvalidAdmin.setObjectName(_fromUtf8("InvalidAdmin"))
        InvalidAdmin.resize(446, 379)
        InvalidAdmin.setMinimumSize(QtCore.QSize(446, 379))
        InvalidAdmin.setMaximumSize(QtCore.QSize(446, 379))
        self.verticalLayoutWidget_2 = QtGui.QWidget(InvalidAdmin)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(309, 310, 121, 51))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButtonOk = QtGui.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButtonOk.setFont(font)
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.verticalLayout_2.addWidget(self.pushButtonOk)
        self.verticalLayoutWidget_3 = QtGui.QWidget(InvalidAdmin)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 170, 421, 131))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.textBrowser = QtGui.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.verticalLayoutWidget = QtGui.QWidget(InvalidAdmin)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 0, 191, 161))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(189, 159))
        self.label.setMaximumSize(QtCore.QSize(189, 159))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/Logo/alert.jpg")))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(InvalidAdmin)
        QtCore.QObject.connect(self.pushButtonOk, QtCore.SIGNAL(_fromUtf8("clicked()")), InvalidAdmin.close)
        QtCore.QMetaObject.connectSlotsByName(InvalidAdmin)

    def retranslateUi(self, InvalidAdmin):
        InvalidAdmin.setWindowTitle(_translate("InvalidAdmin", "Invalid Admin", None))
        self.pushButtonOk.setText(_translate("InvalidAdmin", "OK", None))
        self.textBrowser.setHtml(_translate("InvalidAdmin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Invalid Admin ID</span><span style=\" font-size:22pt; font-weight:600; color:#ff0000;\"> </span><span style=\" font-size:22pt; font-weight:600; text-decoration: underline; color:#ff0000;\">!</span><span style=\" color:#ff0000;\"> </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#00007f;\">Please Login With valid admin ID.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#00007f;\"><br /></p></body></html>", None))

import Alert_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    InvalidAdmin = QtGui.QWidget()
    ui = Ui_InvalidAdmin()
    ui.setupUi(InvalidAdmin)
    InvalidAdmin.show()
    sys.exit(app.exec_())

