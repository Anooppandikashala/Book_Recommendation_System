#!/usr/bin/env python
 
import csv
import sys
import pprint
 
# Function to convert a csv file to a list of dictionaries.  Takes in one variable called "variables_file"
 
def csv_dict_list(variables_file):
     
    # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs
 
    reader = csv.DictReader(open(variables_file, 'rb'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    return dict_list
 
# Calls the csv_dict_list function, passing the named csv
csvfile="/home/anoop/Desktop/PythonProject/DataSet/BXCSVDump/aabbcc.csv"
device_values = csv_dict_list(csvfile)

# Prints the results nice and pretty like
#print(device_values[]"2005018"])
#pprint.pprint(device_values)
key=2005018
x=dict_list.has_key(key)
if(x):
    print dict_list.get(key)
