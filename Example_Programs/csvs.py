import os
import csv
import sys
headers = None
content = {}
cntlist=[]
csvFile="./NewDataSet/full/bookname.csv"
reader1= csv.reader(open(csvFile))
for row in reader1:
	#print row[0]
	if reader1.line_num > 1:
		cntlist.append(row[0])

print cntlist	

'''
csvFile="./NewDataSet/full/isbnandname.csv"
flag=os.path.exists(csvFile)
if(not flag):#to check existing path or not?
	print("Give proper path")
	
#csv.reader(open(csvFile))
reader1= csv.reader(open(csvFile))
for row in reader1:
	if reader1.line_num == 1:
		headers = row[1:]
	else:
		ddd=row[1]
		content[row[0]] = ddd
print content
key='9788171673407'
x=content.has_key(key)
if(x):
	print content.get(key)'''
