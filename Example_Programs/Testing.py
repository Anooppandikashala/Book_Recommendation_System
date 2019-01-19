# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import csv
import sys
import shutil
import os
import random



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

#bookname=""
#isbn=""
headers = None
nameisbn = {}
isbnname = {}
isbnrating = {}
isbndesc = {}

cntlistFiction=[]
cntlistIndianNovel=[]
cntlistJournal=[]
cntlistLiterature=[]


class Ui_Test(object):

    def Clicked1(self,item):
    	
    	print("hello"+item.text())
    	self.bookname=str(item.text())
    	#self.listWidgetCategory.clear()
    	self.googleBookName1()
    	#QtGui.QMessageBox.information(self, "ListWidget", "You clicked: "+self.item.text())
    
    def Clicked(self,item):
    	
    	print("hello"+item.text())
    	self.bookname=str(item.text())
    	#self.listWidgetCategory.clear()
    	self.googleBookName()
    	#QtGui.QMessageBox.information(self, "ListWidget", "You clicked: "+self.item.text())
    

    def createDict(self):
    	self.csvFile1="./NewDataSet/full/nameandisbn.csv"
    	self.csvFile2="./NewDataSet/full/isbnandname.csv"
    	self.csvFile3="./NewDataSet/full/isbnandrating.csv"
    	self.csvFile4="./NewDataSet/fiction/bookname.csv"
    	self.csvFile5="./NewDataSet/indiannovel/bookname.csv"
    	self.csvFile6="./NewDataSet/journal/bookname.csv"
    	self.csvFile7="./NewDataSet/literature/bookname.csv"
    	self.csvFile8="./NewDataSet/full/isbnanddesc.csv"
    	
    	flag1=os.path.exists(self.csvFile1)
    	if(not flag1):#to check existing path or not?
		print("Give proper path")
	else:
		reader=csv.reader(open(self.csvFile1))
		for row in reader:
			if reader.line_num == 1:
    				headers = row[1:]
    			else:
    				ddd=row[1]
				nameisbn[row[0]] = ddd
	
	flag2=os.path.exists(self.csvFile2)
    	if(not flag2):#to check existing path or not?
		print("Give proper path")
	else:
		reader=csv.reader(open(self.csvFile2))
		for row in reader:
			if reader.line_num == 1:
    				headers = row[1:]
    			else:
    				ddd=row[1]
				isbnname[row[0]] = ddd
	flag3=os.path.exists(self.csvFile3)
    	if(not flag3):#to check existing path or not?
		print("Give proper path")
	else:
		reader=csv.reader(open(self.csvFile3))
		for row in reader:
			if reader.line_num == 1:
    				headers = row[1:]
    			else:
    				ddd=row[1]
				isbnrating[row[0]] = ddd
    	
    	'''reader= csv.reader(open(csvFile4))
	for row in reader1:
		#print row[0]
		if reader1.line_num > 1:
			cntlist.append(row[0])'''

	flag4=os.path.exists(self.csvFile4)
    	if(not flag4):#to check existing path or not?
		print("Give proper path")
	else:
		reader=csv.reader(open(self.csvFile4))
		for row in reader:
			if reader.line_num > 1:
				cntlistFiction.append(row[0])
				
	flag5=os.path.exists(self.csvFile5)
    	if(not flag5):#to check existing path or not?
		print("Give proper path")
	else:
		reader=csv.reader(open(self.csvFile5))
		for row in reader:
			if reader.line_num > 1:
				cntlistIndianNovel.append(row[0])
				
	flag6=os.path.exists(self.csvFile6)
    	if(not flag6):#to check existing path or not?
		print("Give proper path")
	else:
		reader=csv.reader(open(self.csvFile6))
		for row in reader:
			if reader.line_num > 1:
				cntlistJournal.append(row[0])
				
	
	flag7=os.path.exists(self.csvFile7)
    	if(not flag7):#to check existing path or not?
		print("Give proper path")
	else:
		reader=csv.reader(open(self.csvFile7))
		for row in reader:
			if reader.line_num > 1:
				cntlistLiterature.append(row[0])
				
	flag8=os.path.exists(self.csvFile8)
    	if(not flag1):#to check existing path or not?
		print("Give proper path")
	else:
		reader=csv.reader(open(self.csvFile8))
		for row in reader:
			if reader.line_num == 1:
    				headers = row[1:]
    			else:
    				ddd=row[1]
				isbndesc[row[0]] = ddd			
	
    	
    def selectionchange(self,j):
    
    	self.listWidgetSimilarBooks.clear()
      	print "Items in the list are :"
		
      	'''for count in range(self.comboBox.count()):
      		print self.comboBox.itemText(count)'''
      	print "Current index",j,"selection changed ",self.comboBox.currentText()
      	if(j==0):
      		#--
      		self.listWidgetCategory.clear()
    		for i in cntlistFiction:
			self.item1 = QtGui.QListWidgetItem(i)
			self.listWidgetCategory.addItem(self.item1)
			
	elif(j==1):
      		#--
      		self.listWidgetCategory.clear()
    		for i in cntlistIndianNovel:
			self.item2 = QtGui.QListWidgetItem(i)
			self.listWidgetCategory.addItem(self.item2)
			
	elif(j==2):
      		#--
      		self.listWidgetCategory.clear()
    		for i in cntlistJournal:
			self.item3 = QtGui.QListWidgetItem(i)
			self.listWidgetCategory.addItem(self.item3)
			
	elif(j==3):
      		#--
      		self.listWidgetCategory.clear()
    		for i in cntlistLiterature:
			self.item3 = QtGui.QListWidgetItem(i)
			self.listWidgetCategory.addItem(self.item3)    	



    def googleBookName1(self):
    	'''print(self.bookname)
    	self.csvFile="./NewDataSet/full/nameandisbn.csv"
    	
    	flag=os.path.exists(self.csvFile)
    	if(not flag):#to check existing path or not?
		print("Give proper path")
	else:
		reader=csv.reader(open(self.csvFile))
		for row in reader:
			if reader.line_num == 1:
    				headers = row[1:]
    			else:
    				ddd=row[1]
				nameisbn[row[0]] = ddd'''
	print self.bookname
	self.x=str(nameisbn.has_key(self.bookname))
	print(self.x)
	if(self.x):
		print("Found")
		self.result=""
		self.isbn1=nameisbn.get(self.bookname)
		xxxx=float(isbnrating.get(self.isbn1))
		xyz=str(nameisbn.get(self.bookname))
		print(xxxx)
		if(xxxx>=4):
			self.result="Best Book"
		elif(xxxx>=3):
			self.result="Good Book"
		elif(xxxx>=2):
			self.result="Average Book"
		else:
			self.result="Minimum Average Book"
		
			
		self.output="Rating of the book:\nBook Name : "+self.bookname+"  is  :  "+str(xxxx)+"  out of 5 \nOur Recommendation : "+self.result
		
		
		#self.textEdit2.setText()
		
	else:
		self.output="OOPs !!!\nThe Searched Book is not In our Database.\n"
			
	print(self.output) 
	self.textEditrating.setText(self.output)
    
    
    def googleBookName(self):
    	'''print(self.bookname)
    	self.csvFile="./NewDataSet/full/nameandisbn.csv"
    	
    	flag=os.path.exists(self.csvFile)
    	if(not flag):#to check existing path or not?
		print("Give proper path")
	else:
		reader=csv.reader(open(self.csvFile))
		for row in reader:
			if reader.line_num == 1:
    				headers = row[1:]
    			else:
    				ddd=row[1]
				nameisbn[row[0]] = ddd'''
	print self.bookname
	self.x=str(nameisbn.has_key(self.bookname))
	print(self.x)
	if(self.x):
		print("Found")
		self.result=""
		self.isbn1=nameisbn.get(self.bookname)
		xxxx=float(isbnrating.get(self.isbn1))
		xyz=str(nameisbn.get(self.bookname))
		print(xxxx)
		if(xxxx>=4):
			self.result="Best Book"
		elif(xxxx>=3):
			self.result="Good Book"
		elif(xxxx>=2):
			self.result="Average Book"
		else:
			self.result="Minimum Average Book"
		
			
		self.output="Rating of the book:\nBook Name : "+self.bookname+"  is  :  "+str(xxxx)+"  out of 5 \nOur Recommendation : "+self.result
		
		
		#self.textEdit2.setText()
		
	else:
		self.output="OOPs !!!\nThe Searched Book is not In our Database.\n"
			
	print(self.output) 
	self.textEditrating.setText(self.output)
	
	xyz=str(isbndesc.get(self.isbn1))
	print xyz
	
	if xyz == 'Indian novels':
		random.shuffle(cntlistIndianNovel)
		self.listWidgetSimilarBooks.clear()
    		for i in cntlistIndianNovel:
			self.item5 = QtGui.QListWidgetItem(i)
			self.listWidgetSimilarBooks.addItem(self.item5)
			
	elif xyz == 'journals':
		random.shuffle(cntlistJournal)
		self.listWidgetSimilarBooks.clear()
    		for i in cntlistJournal:
			self.item6 = QtGui.QListWidgetItem(i)
			self.listWidgetSimilarBooks.addItem(self.item6)
			
	elif xyz == 'fiction':
		random.shuffle(cntlistFiction)
		self.listWidgetSimilarBooks.clear()
    		for i in cntlistFiction:
			self.item7 = QtGui.QListWidgetItem(i)
			self.listWidgetSimilarBooks.addItem(self.item7)
			
	elif xyz == 'literature':
		random.shuffle(cntlistLiterature)
		self.listWidgetSimilarBooks.clear()
    		for i in cntlistLiterature:
			self.item8 = QtGui.QListWidgetItem(i)
			self.listWidgetSimilarBooks.addItem(self.item8)
	

    def googleIsbn(self):
    	'''print(self.bookname)
    	self.csvFile="./NewDataSet/full/nameandisbn.csv"
    	
    	flag=os.path.exists(self.csvFile)
    	if(not flag):#to check existing path or not?
		print("Give proper path")
	else:
		reader=csv.reader(open(self.csvFile))
		for row in reader:
			if reader.line_num == 1:
    				headers = row[1:]
    			else:
    				ddd=row[1]
				nameisbn[row[0]] = ddd'''
	
	self.x=str(isbnrating.has_key(self.isbn))
	print(self.x)
	if(self.x):
		print("Found")
		self.result=""
		isbn=self.isbn
		xxxx=float(isbnrating.get(isbn))
		print(xxxx)
		if(xxxx>=4):
			self.result="Best Book"
		elif(xxxx>=3):
			self.result="Good Book"
		elif(xxxx>=2):
			self.result="Average Book"
		else:
			self.result="Minimum Average Book"
		
			
		self.output="Rating of the book:\nBook ISBN : "+self.isbn+"  is  :  "+str(xxxx)+"  out of 5 \nOur Recommendation : "+self.result
		
		
		#self.textEdit2.setText()
		
	else:
		self.output="OOPs !!!\nThe Searched Book is not In our Database.\nOr\nGive a correct ISBN."
			
	print(self.output) 
	self.textEditrating.setText(self.output)
		
		
		
		
    def btnClick1(self):
    	self.listWidgetSimilarBooks.clear()
    	self.listWidgetCategory.clear()
    	self.bookname=str(self.textEditbookname.text())
    	print(self.bookname)
    	if(self.bookname == ""):
    		self.textEditrating.setText("OOPs ! \n Please Give a Book Name")
    	else :
    		self.googleBookName()
    	
    	
    def btnClick2(self):
    	self.listWidgetSimilarBooks.clear()
    	self.listWidgetCategory.clear()
    	self.isbn=str(self.textEditisbn.text())
    	print(self.isbn)
    	if(self.isbn == ""):
    		self.textEditrating.setText("OOPs ! \n Please Give a Book ISBN Number")
    	else :
    		self.googleIsbn()
    		


    def setupUi(self, Test):
    	
    	self.createDict()
    	
        Test.setObjectName(_fromUtf8("Test"))
        Test.resize(825, 582)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Test.sizePolicy().hasHeightForWidth())
        Test.setSizePolicy(sizePolicy)
        Test.setMinimumSize(QtCore.QSize(577, 480))
        font = QtGui.QFont()
        font.setKerning(True)
        Test.setFont(font)
        Test.setLayoutDirection(QtCore.Qt.LeftToRight)
        Test.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(Test)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 211, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btnBookname = QtGui.QPushButton(self.centralwidget)
        self.btnBookname.setGeometry(QtCore.QRect(10, 120, 85, 27))
        self.btnBookname.setObjectName(_fromUtf8("btnBookname"))
        ########################################################
        #self.createDict()
        self.btnBookname.clicked.connect(self.btnClick1)
        
        ########################################################
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 290, 74, 23))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.btnisbn = QtGui.QPushButton(self.centralwidget)
        self.btnisbn.setGeometry(QtCore.QRect(10, 230, 85, 27))
        self.btnisbn.setObjectName(_fromUtf8("btnisbn"))
        ########################################################
        
        self.btnisbn.clicked.connect(self.btnClick2)
        
        ########################################################
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.textEditrating = QtGui.QTextEdit(self.centralwidget)
        self.textEditrating.setGeometry(QtCore.QRect(10, 320, 261, 201))
        self.textEditrating.setObjectName(_fromUtf8("textEditrating"))
        ########################################################
        
        
        
        
        ########################################################
        self.textEditbookname = QtGui.QLineEdit(self.centralwidget)
        self.textEditbookname.setGeometry(QtCore.QRect(10, 80, 221, 31))
        self.textEditbookname.setObjectName(_fromUtf8("textEditbookname"))
        ########################################################
        
        #self.textEditbookname.setText("Book Name")
        
        
        ########################################################
        self.textEditisbn = QtGui.QLineEdit(self.centralwidget)
        self.textEditisbn.setGeometry(QtCore.QRect(10, 190, 221, 31))
        self.textEditisbn.setObjectName(_fromUtf8("textEditisbn"))
        ########################################################
        
        #self.textEditisbn.setText("ISBN Number")
        
        
        ########################################################
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 801, 41))
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
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(1)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 50, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(280, 80, 221, 24))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        ########################################################
        
        
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        
        
        ########################################################
        self.listWidgetCategory = QtGui.QListWidget(self.centralwidget)
        self.listWidgetCategory.setGeometry(QtCore.QRect(280, 110, 521, 151))
        self.listWidgetCategory.setObjectName(_fromUtf8("listWidgetCategory"))
        '''item = QtGui.QListWidgetItem()
        self.listWidgetCategory.addItem(item)'''
        ########################################################
        
        
        self.listWidgetCategory.itemClicked.connect(self.Clicked)
        
        
        
        ########################################################
        self.listWidgetSimilarBooks = QtGui.QListWidget(self.centralwidget)
        self.listWidgetSimilarBooks.setGeometry(QtCore.QRect(280, 320, 521, 201))
        self.listWidgetSimilarBooks.setObjectName(_fromUtf8("listWidgetSimilarBooks"))
        '''item = QtGui.QListWidgetItem()
        self.listWidgetSimilarBooks.addItem(item)'''
        ########################################################
        
        
        self.listWidgetSimilarBooks.itemClicked.connect(self.Clicked1)
        
        
        ########################################################
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 290, 191, 23))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 270, 791, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(260, 50, 16, 221))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 40, 791, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        Test.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Test)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuAbout_Us = QtGui.QMenu(self.menubar)
        self.menuAbout_Us.setObjectName(_fromUtf8("menuAbout_Us"))
        Test.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Test)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Test.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Test)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Test.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionClose = QtGui.QAction(Test)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout_Us.menuAction())

        self.retranslateUi(Test)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(_fromUtf8("activated()")), Test.close)
        QtCore.QMetaObject.connectSlotsByName(Test)

    def retranslateUi(self, Test):
        Test.setWindowTitle(_translate("Test", "Test", None))
        self.label_2.setText(_translate("Test", "Search By  Book Name", None))
        self.btnBookname.setText(_translate("Test", "Search..", None))
        self.label_3.setText(_translate("Test", "Rating :", None))
        self.btnisbn.setText(_translate("Test", "Search..", None))
        self.label_4.setText(_translate("Test", "Search By ISBN  ", None))
        self.label.setText(_translate("Test", "    BOOK RECOMMENDATION SYSTEM", None))
        self.label_5.setText(_translate("Test", "Search By Category  ", None))
        self.comboBox.setItemText(0, _translate("Test", "Fiction", None))
        self.comboBox.setItemText(1, _translate("Test", "Indian Novels", None))
        self.comboBox.setItemText(2, _translate("Test", "Journals", None))
        self.comboBox.setItemText(3, _translate("Test", "Literature", None))
        __sortingEnabled = self.listWidgetCategory.isSortingEnabled()
        self.listWidgetCategory.setSortingEnabled(False)
        ############################################################
        
        '''item = self.listWidgetCategory.item(0)
        item.setText(_translate("Test", "New Item", None))'''
        
        ############################################################
        
        self.listWidgetCategory.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidgetSimilarBooks.isSortingEnabled()
        self.listWidgetSimilarBooks.setSortingEnabled(False)
        
        ############################################################
        
        '''item = self.listWidgetSimilarBooks.item(0)
        item.setText(_translate("Test", "New Item", None))'''
        
        ############################################################
        
        self.listWidgetSimilarBooks.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("Test", "Similar Books", None))
        self.menuFile.setTitle(_translate("Test", "File", None))
        self.menuEdit.setTitle(_translate("Test", "Edit", None))
        self.menuAbout_Us.setTitle(_translate("Test", "About Us", None))
        self.toolBar.setWindowTitle(_translate("Test", "toolBar", None))
        self.actionClose.setText(_translate("Test", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Test = QtGui.QMainWindow()
    ui = Ui_Test()
    ui.setupUi(Test)
    Test.show()
    sys.exit(app.exec_())

