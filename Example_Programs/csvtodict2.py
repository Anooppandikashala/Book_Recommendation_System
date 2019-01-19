#!/usr/bin/env python
#
# [SNIPPET_NAME: CSV to Dictionary]
# [SNIPPET_CATEGORIES: csv]
# [SNIPPET_DESCRIPTION: Read a CSV file to a dictionary of dictionaries]
# [SNIPPET_AUTHOR: Bruno Girin <brunogirin@gmail.com>]
# [SNIPPET_LICENSE: GPL]

# This snippet demonstrates how to read a CSV file into a dictionary of
# dictionaries in order to be able to query it easily.
# The full documentation for the csv module is available here:
# http://docs.python.org/library/csv.html
#
# The data used in the companion csv2dict.csv file was taken from here:
# http://www.trainweb.org/tubeprune/Statistics.htm
# See, you can even learn some interesting facts about the London Underground
# network while learning Python.

#
# First things first, we need to import the csv module
# Also import sys to get argv[0], which holds the name of the script
#
import csv
import sys
# Derive the name of the CSV file from the name of the script and initialise
# the headers list and content dictionary
#csvFile = sys.argv[0].replace('.py', '.csv')
headers = None
content = {}



#print('Reading file %s' % csvFile)
csvFile="/home/anoop/Desktop/PythonProject/DataSet/BXCSVDump/aabbccdd.csv"
reader=csv.reader(open(csvFile))
for row in reader:
    if reader.line_num == 1:
        """
        If we are on the first line, create the headers list from the first row
        by taking a slice from item 1  as we don't need the very first header.
        """
        headers = row[1:]
    else:
        """
        Otherwise, the key in the content dictionary is the first item in the
        row and we can create the sub-dictionary by using the zip() function.
        We also know that the stabling entry is a comma separated list of names
        so we split it into a list for easier processing.
        """
#       content[row[0]] = dict(zip(headers, row[1:]))
#	content[row[0]] = dict(zip(row[1:]))
#	content[row[0]] = dict(zip(headers, row[1:2]))
	ddd=row[1]
	content[row[0]] = ddd
        """content[row[0]]['ISBN'] = [s.strip() for s in content[row[0]]['Book-Title'].split(',')]"""

# We can know get to the content by using the resulting dictionary, so to see
# the list of lines, we can do:
print "\nList of lines"
print content.keys()
# To see the list of statistics available for each line
key='The Mummies of Urumchi'
x=content.has_key(key)
if(x):
	print("Found")
	print(content.get(key))
else:
	print("not found")
'''
print("dictionary values:")
print(content)
fff=content.items()
for i,j in fff:
	print(i,j)
#print(content.keys(),content.values())
#for j in content.values():
abc1=[]
abc2=[]
for i in content.keys():
	abc1.append(i)
for j in content.values():
	abc2.append(j)
print("First:")
print(abc1)

print("Second:")
print(abc2)

print "\nAvailable statistics for each line"
print headers


print "\nDictionary"
print content'''
# To see any statistic for a line, we can just request it by name
#print "\nPeak hourly train frequency for the Piccadilly line"
#print content['ISBN']['Book-Title']
# Or we can use list comprehensions to filter the list
'''print "\nThe list of lines that have Earl's Court as a control centre"
print [k for k, v in content.items() if v['Control Centre'] == 'Earls Court']
print "\nThe list of lines that have Hammersmith as one of their stabling stations"
print [k for k, v in content.items() if 'Hammersmith' in v['Stabling']]
'''
