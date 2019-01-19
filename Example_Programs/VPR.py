from collections import defaultdict
import numpy as np
class vpr(object):
	def sumfunc(self,num):
		return num 
     
	def sumlist(self, mylist, sumfunc):
        	sum = 0
        	for i in mylist:
            		sum = sum + self.sumfunc(i)
        	return sum
     
    	def mean(self,mylist):
        	meanval = 0
     
        	if(len(mylist) == 0):
           		return 0
        	else:
           		meanval = self.sumlist(mylist,self.sumfunc)/len(mylist)
           	return meanval
	def variance(self,mylist):
    
        	mymean = self.mean(mylist)
        	mylen = len(mylist)
        	temp = 0
        
        	for i in range(mylen):
        		temp += (mylist[i] - mymean) * (mylist[i] - mymean) 
        	return temp / mylen
        	
	def analysis(self,ratinglist):
		threshold=2
		l=len(ratinglist)
		if (l!=0):
			var=self.variance(ratinglist)
			if(var>threshold):
				avg=self.mean(ratinglist)
				return avg
			else:
				d = defaultdict(float)
				for i in ratinglist:
    					d[i] += 1
				result = max(d.iteritems(), key=lambda x: x[1])
				maxrate=result[0]
				return maxrate
		else:
			return 0
			
			
'''a=vpr()
L=[0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25]
print(a.analysis(L))'''
