# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Training.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import csv
import os
import sys
import shutil
from PyQt4 import QtCore, QtGui
from SentimentAnalysis import Bs
from kmeantest import cluster
from VPR import vpr
file_path = os.path.dirname(__file__)
if file_path != "":
    os.chdir(file_path)

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
headers = None
content = {}
namereview={}
f4=open("./namereview.csv","a")
filepath="../ExampleFiles/book2.txt"
#bookfile = open(filepath, "w")
class Ui_Training(object):
    
   
    def kmeanscluster(self):
    	a=cluster()
    	a.KMEANS()
    def readFile(self):
    	'''self.bookfile.write(self.stra);
	self.bookfile.close()'''
	#if(self.bookfile.closed):
	print("successful")
	self.plainTextEditResult.setText("Training Completed !")
	#else:
	#	self.plainTextEditResult.setText("Training Incomplete Try Again !")
    def google(self):
    	#self.csvFile9="./NewDataSet/book1.csv"
    	#flag0=os.path.exists(self.csvFile9)
    	self.csvFile9=self.Fileurl
    	flag0=os.path.exists(self.csvFile9)
    	if(not flag0):#to check existing path or not?
		print("Give proper path")
	else:
		reader=csv.reader(open(self.csvFile9))
		cnt=0.0
		for i in reader:
			cnt=cnt+1
		print ("Count")
		print (cnt)
		reader=csv.reader(open(self.csvFile9))
		luv=0.0
		for row in reader:
			luv=luv+1
			print luv
			print cnt
			uu=int((float(luv/cnt))*100)
			print uu
			vv=""
			vv="Training in progress : "+str(uu)+"% Completed !"
			print vv
			self.plainTextEditResult.setText(vv)
			if reader.line_num == 1:
    				headers = row[1:]
    			else:
    				ddd=row[1]
    				a=str(ddd)
				x=len(a)
				#print x
				s=[]
				j=0
				strs=""
				gog=""
				rating=0
				
				for i in range(x):
					if(a[i]!="$" and i!=(x-1)):
						#print a[i]
						strs=strs+a[i]
					else:
						#print strs
						s.append(strs)
						strs=""
				l=len(s)
				#to implement sentiment analysis
				obj=Bs()
				ratinglist=[]
				for i in range(l):
					#print s[i]
					tyu=float(obj.name(str(s[i])))
					ratinglist.append(tyu)
					#rating=rating+tyu
				#print "Rating :"
				#print rating
				#print "Average Rating :"
				a=vpr()
				
				kkukk=a.analysis(ratinglist)
				#print kkukk
				gog=str(row[0])+","+str(kkukk)+"\n"
				f4.write(gog)
				
				namereview[row[0]] = kkukk
			#
				
				
		print "-----------------------------------------------------------------------------------"
		print "namereview"
		print namereview
		print "-----------------------------------------------------------------------------------"
		f4.close()
		self.kmeanscluster()		
	'''print namereview
	t=len(namereview)
	print t
	for x in namereview:
		print x'''
    	''''print(self.Fileurl)
    	#csvFile="/home/anoop/Desktop/PythonProject/DataSet/BXCSVDump/aabbccdd.csv"
    	
    	flag=os.path.exists(self.Fileurl)
    	if(not flag):#to check existing path or not?
		print("Give proper path")
		''''''self.plainTextEditResult.setText("Give Proper Path !")''''''
	else:
		reader=csv.reader(open(self.Fileurl))
		self.bookfile = open(filepath, "w")
		for row in reader:
			if reader.line_num == 1:
    				headers = row[1:]
    			else:
    				ddd=row[1]
				content[row[0]] = ddd
		fff=content.items()
		self.stra=""
		tab=" : "
		newline="\n"
		for i,j in fff:
			#self.plainTextEdit.setText(i)
			#self.plainTextEdit.setText(j)
			#print(i,j)
			gg=i+tab+j+newline
			#print(gg)
			self.stra=self.stra+gg
			#stra=stra+
		self.readFile()'''

		#self.plainTextEdit.setText(stra)

	'''if(x):
		#print("Found")
		xxxx=content.get(key)
		#self.plainTextEdit.setText(xxxx)
		#print(content)
		fff=content.items()
		stra=""
		tab=" : "
		newline="\n"
		for i,j in fff:
			#self.plainTextEdit.setText(i)
			#self.plainTextEdit.setText(j)
			#print(i,j)
			gg=i+tab+j+newline
			#print(gg)
			stra=stra+gg
			#stra=stra+
		self.plainTextEdit.setText(stra)
		#print(stra)
			
	else:
		print("not found")

	print("dictionary values:")
	print(content)
	fff=content.items()
	for i,j in fff:
		print(i,j)'''
    	
    def btnClick(self):
    	self.Fileurl=str(self.lineEditFileBrowse.text())
        #print(Fileurl)
        self.google()
        
    def setupUi(self, Training):
        Training.setObjectName(_fromUtf8("Training"))
        Training.resize(576, 481)
        Training.setMinimumSize(QtCore.QSize(576, 481))
        Training.setMaximumSize(QtCore.QSize(576, 481))
        self.centralwidget = QtGui.QWidget(Training)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 551, 61))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(549, 59))
        self.label.setMaximumSize(QtCore.QSize(549, 49))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 80, 551, 41))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setMinimumSize(QtCore.QSize(549, 29))
        self.label_2.setMaximumSize(QtCore.QSize(549, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 130, 551, 41))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setMinimumSize(QtCore.QSize(549, 29))
        self.label_3.setMaximumSize(QtCore.QSize(549, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 250, 211, 61))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.BtnTrain = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.BtnTrain.setFont(font)
        self.BtnTrain.setObjectName(_fromUtf8("BtnTrain"))
        self.horizontalLayout.addWidget(self.BtnTrain)
        ###############################################
        
        self.BtnTrain.clicked.connect(self.btnClick)
        ###############################################
       
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(30, 320, 511, 101))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.plainTextEditResult = QtGui.QTextEdit(self.verticalLayoutWidget_4)
        self.plainTextEditResult.setObjectName(_fromUtf8("plainTextEditResult"))
        self.verticalLayout_4.addWidget(self.plainTextEditResult)
        self.lineEditFileBrowse = QtGui.QLineEdit(self.centralwidget)
        self.lineEditFileBrowse.setGeometry(QtCore.QRect(180, 200, 371, 29))
        self.lineEditFileBrowse.setObjectName(_fromUtf8("lineEditFileBrowse"))
        ###############################################
        
        
        ###############################################
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        Training.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Training)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 576, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuAboutus = QtGui.QMenu(self.menubar)
        self.menuAboutus.setObjectName(_fromUtf8("menuAboutus"))
        Training.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Training)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Training.setStatusBar(self.statusbar)
        self.actionClose = QtGui.QAction(Training)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionUndo = QtGui.QAction(Training)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionRedo = QtGui.QAction(Training)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))
        self.actionThis_Project = QtGui.QAction(Training)
        self.actionThis_Project.setObjectName(_fromUtf8("actionThis_Project"))
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuAboutus.addAction(self.actionThis_Project)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAboutus.menuAction())

        self.retranslateUi(Training)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(_fromUtf8("activated()")), Training.close)
        QtCore.QMetaObject.connectSlotsByName(Training)

    def retranslateUi(self, Training):
        Training.setWindowTitle(_translate("Training", "Training", None))
        self.label.setText(_translate("Training", "  BOOK RECOMMENDATION SYSTEM", None))
        self.label_2.setText(_translate("Training", "Admin Login", None))
        self.label_3.setText(_translate("Training", " Training  Session..!", None))
        self.BtnTrain.setText(_translate("Training", "Update System", None))
        self.label_4.setText(_translate("Training", "Input a File Path:", None))
        self.menuFile.setTitle(_translate("Training", "File", None))
        self.menuEdit.setTitle(_translate("Training", "Edit", None))
        self.menuAboutus.setTitle(_translate("Training", "Aboutus", None))
        self.actionClose.setText(_translate("Training", "Close", None))
        self.actionUndo.setText(_translate("Training", "Undo", None))
        self.actionRedo.setText(_translate("Training", "Redo", None))
        self.actionThis_Project.setText(_translate("Training", "This Project", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Training = QtGui.QMainWindow()
    ui = Ui_Training()
    ui.setupUi(Training)
    Training.show()
    sys.exit(app.exec_())

