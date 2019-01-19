
#---------------------------------------------------------------------------
'''Author Group10'''
#---------------------------------------------------------------------------
from SentimentAnalysis import Bs
from PyQt4 import QtCore, QtGui
from Admin import Ui_AdminLogin
from SentenceSplit import SentenceSplits
from about import Ui_Dialog
from kmeantest import cluster


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

#dictionaries
headers = None
nameisbn = {}
isbnname = {}
isbnrating = {}
isbndesc = {}
namereview={}
sentimented_rating={}



#book lists
cntlistFiction=[]
cntlistIndianNovel=[]
cntlistJournal=[]
cntlistLiterature=[]
cntlistfull=[]

#clustered lists
toprated=[]
lowrated=[]
medrated=[]


#clustered lists writing to files
f1=open("/home/anoop/toprated.txt","r")
f2=open("/home/anoop/medrated.txt","r")
f3=open("/home/anoop/lowrated.txt","r")
fcluster1=open("./clusterisbnrate.csv","w")
fcluster2=open("./clusternamerate.csv","w")
#f4=open("./namereview.csv","w")

csvFile0="./NewDataSet/full/bookname.csv"
class Ui_Test(object):


    #to create csv files for clustering
    def createclustercsv(self):
    	for i in range(len(cntlistfull)):
    		data=str(cntlistfull[i])
    		fisbn=(nameisbn.get(data))
    		print data
    		
    		
    		frate1=float(isbnrating.get(fisbn))
    		frate2=float(sentimented_rating.get(data))
    		print i
		print "-----------------------"
		print frate1
		print frate2
		print "-----------------------" 
		
		fratef=(frate1+frate2)/2
		dd=""
		dd=str(fisbn)+","+str(fratef)+"\n"
		
		fcluster1.write(dd)
		dd=str(data)+","+str(fratef)+"\n"
		fcluster2.write(dd)
		
		
	fcluster1.close()
	fcluster2.close()	
		
    #to find rating from sentimented score		
    def findrating(self,rate):
    	if(rate==0):
    		return 2.5
    	if(rate<0):
    		if(rate<-5):
    			return 0.0
    		elif(rate<-3):
    			return 0.5
    		elif(rate<-2):
    			return 1.0
    		elif(rate<-1):
    			return 1.5
    		else:
    			return 2.0
    	if(rate > 0):
    		if(rate<5):
    			return 5.0
    		elif(rate<4):
    			return 4.5
    		elif(rate<3):
    			return 4.0
    		elif(rate<2):
    			return 3.5
    		elif(rate<1):
    			return 3.0
    		else:
    			return 2.3
    		
    def updateSystem(self):
    	print "In update"
    	self.adminWindow=QtGui.QWidget()
    	self.ui = Ui_AdminLogin()
    	self.ui.setupUi(self.adminWindow)
    	self.adminWindow.show()
    	
    	
    def thisProject(self):
    	print "In thisProject"
    	self.adminWindow1=QtGui.QDialog()
    	self.ui = Ui_Dialog()
    	self.ui.setupUi(self.adminWindow1)
    	self.adminWindow1.show()
    	
    def Clicked2(self,item):
    	self.listWidgetCategory.clear()
    	self.textEditbookname.clear()
    	self.textEditisbn.clear()
    	print("hello"+item.text())
    	self.bookname=str(item.text())
    	#self.listWidgetCategory.clear()
    	self.googleBookName()
    	#QtGui.QMessageBox.information(self, "ListWidget", "You clicked: "+self.item.text())
    
    def Clicked1(self,item):
    	
    	print("hello"+item.text())
    	self.bookname=str(item.text())
    	self.listWidgetCategory.clear()
    	self.textEditbookname.clear()
    	self.textEditisbn.clear()
    	
    	self.googleBookName1()
    	#QtGui.QMessageBox.information(self, "ListWidget", "You clicked: "+self.item.text())
    
    def Clicked(self,item):
    	#self.listWidgetCategory.clear()
    	self.textEditbookname.clear()
    	self.textEditisbn.clear()
    	print("hello"+item.text())
    	self.bookname=str(item.text())
    	#self.listWidgetCategory.clear()
    	self.googleBookName()
    	#QtGui.QMessageBox.information(self, "ListWidget", "You clicked: "+self.item.text())
    

    def createDict(self):
    
    	while(1):
		str1 = f1.readline();
		if str1 != "" :
			str1=str1.strip("\n")
			toprated.append(str1)
			#print str
		else:
			break	
    
    	while(1):
		str1 = f2.readline();
		if str1 != "" :
			str1=str1.strip("\n")
			medrated.append(str1)
			#print str
		else:
			break
    	while(1):
		str1 = f3.readline();
		if str1 != "" :
			str1=str1.strip("\n")
			lowrated.append(str1)
			#print str
		else:
			break
			
			
	print "--------------------------------------------------------------------------"
    	print "toprated:"
    	print toprated
    	print "--------------------------------------------------------------------------"
    	print "medrated:"
    	print medrated
    	print "--------------------------------------------------------------------------"
    	print "lowrated:"
    	print lowrated
    	print "--------------------------------------------------------------------------"
    	
    	
    	#Datasets
    	#--------------------------------------------------------------------------------------------------------
    	self.csvFile1="./NewDataSet/full/nameandisbn.csv"
    	self.csvFile2="./NewDataSet/full/isbnandname.csv"
    	self.csvFile3="./NewDataSet/full/isbnandrating.csv"
    	self.csvFile4="./NewDataSet/fiction/bookname.csv"
    	self.csvFile5="./NewDataSet/indiannovel/bookname.csv"
    	self.csvFile6="./NewDataSet/journal/bookname.csv"
    	self.csvFile7="./NewDataSet/literature/bookname.csv"
    	self.csvFile8="./NewDataSet/full/isbnanddesc.csv"
    	
    	
    	
    	self.csvFile9="./NewDataSet/namereview.csv"
    	#--------------------------------------------------------------------------------------------------------
    	
    	flag1=os.path.exists(self.csvFile9)
    	if(not flag1):#to check existing path or not?
		print("Give proper path")
	else:
		reader=csv.reader(open(self.csvFile9))
		for row in reader:
			'''if reader.line_num >> 1:
    				headers = row[1:]
    			else:'''
    			ddd=row[1]
			sentimented_rating[row[0]] = ddd
    	
    	print "--------------------------------------------------------------------------------------------------------"
    	for keys,values in sentimented_rating.items():
    		print(keys)
    		print(values)
    	print "--------------------------------------------------------------------------------------------------------"
    	'''#For sentiment analysis
    	self.csvFile9="./NewDataSet/book1.csv"
    	flag0=os.path.exists(self.csvFile9)
    	if(not flag0):#to check existing path or not?
		print("Give proper path")
	else:
		reader=csv.reader(open(self.csvFile9))
		cnt=0
		for i in reader:
			cnt=cnt+1
		print ("Count")
		print (cnt)
		for row in reader:
			if reader.line_num >> 1:
    				headers = row[1:]
    			else:
    				ddd=row[1]
    				a=str(ddd)
				x=len(a)
				print x
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
						print strs
						s.append(strs)
						strs=""
				l=len(s)
				obj=Bs()
				for i in range(l):
					#print s[i]
					tyu=float(obj.name(str(s[i])))
					rating=rating+tyu
				print "Rating :"
				print rating
				print "Average Rating :"
				kkukk=rating/l
				print kkukk
				gog=str(row[0])+","+str(kkukk)+"\n"
				f4.write(gog)
				
				namereview[row[0]] = kkukk
				
		print "-----------------------------------------------------------------------------------"
		print "namereview"
		print namereview
		print "-----------------------------------------------------------------------------------"		
	print namereview
	t=len(namereview)
	print t
	for x in namereview:
		print x'''
	
    	#--------------------------------------------------------------------------------------------------------
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
		if reader1.line_num < 1:
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
    	if(flag5):#to check existing path or not?
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
				
	#--------------------------------------------------------------
	flag6=os.path.exists(csvFile0)
    	if(not flag6):#to check existing path or not?
		print("Give proper path")
	else:
		reader=csv.reader(open(csvFile0))
		for row in reader:
			if reader.line_num > 1:
				cntlistfull.append(row[0])			
	#--------------------------------------------------------------
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
    	self.textEditrating.clear()
      	print "Items in the list are :"
		
      	'''for count in range(self.comboBox.count()):
      		print self.comboBox.itemText(count)'''
      	print "Current index",j,"selection changed ",self.comboBoxCategory.currentText()
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



    def selectionchange1(self,j):
    	self.textEditrating.clear()
    	self.listWidgetSimilarBooks.clear()
    	if(j==0):
      		#--
      		self.listWidgetCategory.clear()
      		self.listWidgetRating.clear()
    		for i in toprated:
			self.item1 = QtGui.QListWidgetItem(i)
			item2=str(isbnname.get(str(i)))
			print item2
			self.listWidgetRating.addItem(item2)
			
	if(j==1):
      		#--
      		self.listWidgetCategory.clear()
      		self.listWidgetRating.clear()
    		for i in medrated:
			self.item1 = QtGui.QListWidgetItem(i)
			item2=str(isbnname.get(str(i)))
			print item2
			self.listWidgetRating.addItem(item2)
			
	if(j==2):
      		#--
      		self.listWidgetCategory.clear()
      		self.listWidgetRating.clear()
    		for i in lowrated:
			self.item1 = QtGui.QListWidgetItem(i)
			item2=str(isbnname.get(str(i)))
			print item2
			self.listWidgetRating.addItem(item2)
    
    def googleBookName1(self):
    	print(self.bookname)
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
				nameisbn[row[0]] = ddd
				
	print self.bookname
	self.x= nameisbn.has_key(self.bookname)
	print(self.x)
	if(self.x):
		print("Found")
		self.result=""
		self.isbn1=nameisbn.get(self.bookname)
		xxxx1=float(isbnrating.get(self.isbn1))
		yyyy=float(sentimented_rating.get(self.bookname))
		print "--------------------------------------------------------------"
		print "yyyyy"
		print yyyy
		print "--------------------------------------------------------------"
		yyyy=self.findrating(yyyy)
		xxxx=(yyyy+xxxx1)/2
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
		
			
		self.result="Rating of the book:\nBook Name : "+self.bookname+"  is  :  "+str(xxxx)+"  out of 5 \nOur Recommendation : "+self.result+"\nBook ISBN : "+str(self.isbn1)
		
		
		#self.textEdit2.setText()
		
	else:
		self.result="OOPs !!!\nThe Searched Book is not In our Database.\n"
			
	print(self.result) 
	self.textEditrating.setText(self.result)
    
    def part1(self):
    	xyz=str(isbndesc.get(self.isbn1))
	print xyz
	
    	if xyz == 'indian novels':
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
    		for i in cntlistLiterature:
			self.item7 = QtGui.QListWidgetItem(i)
			self.listWidgetSimilarBooks.addItem(self.item7)
			
	elif xyz == 'literature':
		random.shuffle(cntlistLiterature)
		self.listWidgetSimilarBooks.clear()
    		for i in cntlistFiction:
			self.item8 = QtGui.QListWidgetItem(i)
			self.listWidgetSimilarBooks.addItem(self.item8)
	

    def googleBookName(self):
    	
	print self.bookname
	self.x= nameisbn.has_key(self.bookname)
	print(self.x)
	if(self.x):
		print("Found")
		self.result=""
		self.isbn1=nameisbn.get(self.bookname)
		xxxx1=float(isbnrating.get(self.isbn1))
		yyyy=float(sentimented_rating.get(self.bookname))
		print "--------------------------------------------------------------"
		print "yyyyy"
		print yyyy
		print "--------------------------------------------------------------"
		yyyy=self.findrating(yyyy)
		xxxx=(yyyy+xxxx1)/2
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
		
		xyz=str(isbndesc.get(self.isbn1))	
		self.result="Rating of the book:\nBook Name : "+self.bookname+"  is  :  "+str(xxxx)+"  out of 5 \nOur Recommendation : "+self.result+"\nBook ISBN : "+str(self.isbn1)+"\nBook Category : "+xyz
		
		print(self.result) 
		self.textEditrating.setText(self.result)
		#self.textEdit2.setText()
		self.part1()
		
	else:
		self.result="OOPs !!!\nThe Searched Book is not In our Database.\n"
		print(self.result) 
		self.textEditrating.setText(self.result)	
	
	
	
	
	
	
    def part2(self):
    	xyz=str(isbndesc.get(self.isbn))
	print xyz
	
	if xyz == 'indian novels':
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
    	print(self.bookname)
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
				nameisbn[row[0]] = ddd
	
	self.x=isbnrating.has_key(self.isbn)
	self.y=str(isbnname.get(self.isbn))
	print self.y
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
		
		xyz=str(isbndesc.get(self.isbn))	
		self.result="Rating of the book:\nBook ISBN : "+self.isbn+"  is  :  "+str(xxxx)+"  out of 5 \nOur Recommendation : "+self.result+"\nBook Name : "+self.y+"\nBook Category : "+xyz
		
		print(self.result) 
		self.textEditrating.setText(self.result)
		#self.textEdit2.setText()
		self.part2()
		
	else:
		self.result="OOPs !!!\nThe Searched Book is not In our Database.\nOr\nGive a correct ISBN."
		print(self.result) 
		self.textEditrating.setText(self.result)	
	
	
	
	
		
    def btnClick1(self):
    
    	self.listWidgetSimilarBooks.clear()
    	self.listWidgetCategory.clear()
    	self.listWidgetRating.clear()
    	self.textEditrating.clear()
    	self.bookname=str(self.textEditbookname.text())
    	self.bookname=self.bookname.lower()
    	self.textEditisbn.clear()
    	print self.bookname
    	
    	if(self.bookname == ""):
    		self.textEditrating.setText("OOPs ! \n Please Give a Book Name")
    	else :
    		self.googleBookName()
    	
    	
    def btnClick2(self):
    	self.listWidgetSimilarBooks.clear()
    	self.listWidgetCategory.clear()
    	self.listWidgetRating.clear()
    	self.textEditrating.clear()
    	self.isbn=str(self.textEditisbn.text())
    	self.textEditbookname.clear()
    	
    	print(self.isbn)
    	if(self.isbn == ""):
    		self.textEditrating.setText("OOPs ! \n Please Give a Book ISBN Number")
    	else :
    		self.googleIsbn()
    		


    def setupUi(self, Test):
    
    	self.createDict()
    	self.createclustercsv()
    	
    	
    	
    
        Test.setObjectName(_fromUtf8("Test"))
        Test.resize(1133, 638)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/StartPage/network.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Test.setWindowIcon(icon)
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Test.sizePolicy().hasHeightForWidth())
        Test.setSizePolicy(sizePolicy)
        Test.setMinimumSize(QtCore.QSize(1133, 638))
        Test.setMaximumSize(QtCore.QSize(1133, 638))
        font = QtGui.QFont()
        font.setKerning(True)
        Test.setFont(font)
        Test.setLayoutDirection(QtCore.Qt.LeftToRight)
        Test.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(Test)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 211, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btnBookname = QtGui.QPushButton(self.centralwidget)
        self.btnBookname.setGeometry(QtCore.QRect(10, 150, 85, 27))
        self.btnBookname.setObjectName(_fromUtf8("btnBookname"))
        ########################################################
        #self.createDict()
        
        self.btnBookname.clicked.connect(self.btnClick1)
        
        ########################################################
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 330, 74, 23))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.btnisbn = QtGui.QPushButton(self.centralwidget)
        self.btnisbn.setGeometry(QtCore.QRect(10, 280, 85, 27))
        self.btnisbn.setObjectName(_fromUtf8("btnisbn"))
        ########################################################
        
        self.btnisbn.clicked.connect(self.btnClick2)
        
        ########################################################
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.textEditrating = QtGui.QTextEdit(self.centralwidget)
        self.textEditrating.setGeometry(QtCore.QRect(10, 360, 381, 221))
        ########################################################
        
        
        
        
        ########################################################
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textEditrating.setFont(font)
        self.textEditrating.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEditrating.setObjectName(_fromUtf8("textEditrating"))
        self.textEditbookname = QtGui.QLineEdit(self.centralwidget)
        self.textEditbookname.setGeometry(QtCore.QRect(10, 110, 311, 31))
        self.textEditbookname.setObjectName(_fromUtf8("textEditbookname"))
        self.textEditisbn = QtGui.QLineEdit(self.centralwidget)
        self.textEditisbn.setGeometry(QtCore.QRect(10, 240, 311, 31))
        self.textEditisbn.setObjectName(_fromUtf8("textEditisbn"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 1111, 61))
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
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(1)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 70, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.comboBoxCategory = QtGui.QComboBox(self.centralwidget)
        self.comboBoxCategory.setGeometry(QtCore.QRect(350, 100, 221, 24))
        self.comboBoxCategory.setObjectName(_fromUtf8("comboBoxCategory"))
        self.comboBoxCategory.addItem(_fromUtf8(""))
        self.comboBoxCategory.addItem(_fromUtf8(""))
        self.comboBoxCategory.addItem(_fromUtf8(""))
        self.comboBoxCategory.addItem(_fromUtf8(""))
        ########################################################
        
        
        self.comboBoxCategory.currentIndexChanged.connect(self.selectionchange)
        
        
        ########################################################
        self.listWidgetCategory = QtGui.QListWidget(self.centralwidget)
        self.listWidgetCategory.setGeometry(QtCore.QRect(350, 130, 371, 181))
        self.listWidgetCategory.setObjectName(_fromUtf8("listWidgetCategory"))
        '''item = QtGui.QListWidgetItem()
        self.listWidgetCategory.addItem(item)'''
        ########################################################
        
        
        self.listWidgetCategory.itemClicked.connect(self.Clicked)
        
        
        
        ########################################################
        self.listWidgetSimilarBooks = QtGui.QListWidget(self.centralwidget)
        self.listWidgetSimilarBooks.setGeometry(QtCore.QRect(450, 360, 671, 221))
        self.listWidgetSimilarBooks.setObjectName(_fromUtf8("listWidgetSimilarBooks"))
        '''item = QtGui.QListWidgetItem()
        self.listWidgetSimilarBooks.addItem(item)'''
        ########################################################
        
        
        self.listWidgetSimilarBooks.itemClicked.connect(self.Clicked1)
        
        
        ########################################################
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 330, 191, 23))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 310, 1111, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(330, 70, 16, 241))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 60, 1111, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(740, 70, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.listWidgetRating = QtGui.QListWidget(self.centralwidget)
        self.listWidgetRating.setGeometry(QtCore.QRect(740, 130, 381, 181))
        self.listWidgetRating.setObjectName(_fromUtf8("listWidgetRating"))
        '''item = QtGui.QListWidgetItem()
        self.listWidgetRating.addItem(item)'''
        ########################################################
        
        
        self.listWidgetRating.itemClicked.connect(self.Clicked2)
        
        
        
        ########################################################
        
        self.comboBoxRating = QtGui.QComboBox(self.centralwidget)
        self.comboBoxRating.setGeometry(QtCore.QRect(740, 100, 221, 24))
        self.comboBoxRating.setObjectName(_fromUtf8("comboBoxRating"))
        self.comboBoxRating.addItem(_fromUtf8(""))
        self.comboBoxRating.addItem(_fromUtf8(""))
        self.comboBoxRating.addItem(_fromUtf8(""))
        ########################################################
        
        
        self.comboBoxRating.currentIndexChanged.connect(self.selectionchange1)
        
        
        ########################################################
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(720, 70, 16, 241))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(410, 320, 20, 261))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(10, 180, 321, 20))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        Test.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Test)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1133, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout_Us = QtGui.QMenu(self.menubar)
        self.menuAbout_Us.setObjectName(_fromUtf8("menuAbout_Us"))
        self.menuAdmin = QtGui.QMenu(self.menubar)
        self.menuAdmin.setObjectName(_fromUtf8("menuAdmin"))
        Test.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Test)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Test.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Test)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Test.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionClose = QtGui.QAction(Test)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionUndo = QtGui.QAction(Test)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionUpdate_System = QtGui.QAction(Test)
        self.actionUpdate_System.setObjectName(_fromUtf8("actionUpdate_System"))
        
        #self.actionUpdate_System.addAction(self.update)
        
        self.actionThis_Project = QtGui.QAction(Test)
        self.actionThis_Project.setObjectName(_fromUtf8("actionThis_Project"))
        self.menuFile.addAction(self.actionClose)
        self.menuAbout_Us.addAction(self.actionThis_Project)
        self.menuAdmin.addAction(self.actionUpdate_System)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAdmin.menuAction())
        self.menubar.addAction(self.menuAbout_Us.menuAction())

        self.retranslateUi(Test)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(_fromUtf8("activated()")), Test.close)
        QtCore.QObject.connect(self.actionUpdate_System, QtCore.SIGNAL(_fromUtf8("activated()")), self.updateSystem)
        QtCore.QObject.connect(self.actionThis_Project, QtCore.SIGNAL(_fromUtf8("activated()")), self.thisProject)
        QtCore.QMetaObject.connectSlotsByName(Test)

    def retranslateUi(self, Test):
        Test.setWindowTitle(_translate("Test", "Test", None))
        self.label_2.setText(_translate("Test", "Search By  Book Name", None))
        self.btnBookname.setText(_translate("Test", "Search..", None))
        self.label_3.setText(_translate("Test", "Rating :", None))
        self.btnisbn.setText(_translate("Test", "Search..", None))
        self.label_4.setText(_translate("Test", "Search By ISBN  ", None))
        self.textEditrating.setHtml(_translate("Test", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\"<\n"
"<html<<head<<meta name=\"qrichtext\" content=\"1\" /<<style type=\"text/css\"<\n"
"p, li { white-space: pre-wrap; }\n"
"</style<</head<<body style=\" font-family:\'Sans\'; font-size:12pt; font-weight:600; font-style:normal;\"<\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"<<br /<</p<</body<</html<", None))
        self.label.setText(_translate("Test", "    BOOK RECOMMENDATION SYSTEM", None))
        self.label_5.setText(_translate("Test", "Search By Category  ", None))
        self.comboBoxCategory.setItemText(0, _translate("Test", "Fiction", None))
        self.comboBoxCategory.setItemText(1, _translate("Test", "Indian Novels", None))
        self.comboBoxCategory.setItemText(2, _translate("Test", "Journals", None))
        self.comboBoxCategory.setItemText(3, _translate("Test", "Literature", None))
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
        self.label_7.setText(_translate("Test", "Search By Rating  ", None))
        __sortingEnabled = self.listWidgetRating.isSortingEnabled()
        self.listWidgetRating.setSortingEnabled(False)
        ############################################################
        
        
        '''item = self.listWidgetRating.item(0)
        item.setText(_translate("Test", "New Item", None))'''
        
        
        ############################################################
        self.listWidgetRating.setSortingEnabled(__sortingEnabled)
        self.comboBoxRating.setItemText(0, _translate("Test", "Top Rated", None))
        self.comboBoxRating.setItemText(1, _translate("Test", "Medium Rated", None))
        self.comboBoxRating.setItemText(2, _translate("Test", "Low Rated", None))
        self.menuFile.setTitle(_translate("Test", "File", None))
        self.menuAbout_Us.setTitle(_translate("Test", "About Us", None))
        self.menuAdmin.setTitle(_translate("Test", "Admin", None))
        self.toolBar.setWindowTitle(_translate("Test", "toolBar", None))
        self.actionClose.setText(_translate("Test", "Close", None))
        self.actionUndo.setText(_translate("Test", "Undo", None))
        self.actionUpdate_System.setText(_translate("Test", "Update System", None))
        self.actionThis_Project.setText(_translate("Test", "This Project", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Test = QtGui.QMainWindow()
    ui = Ui_Test()
    ui.setupUi(Test)
    Test.show()
    sys.exit(app.exec_())

