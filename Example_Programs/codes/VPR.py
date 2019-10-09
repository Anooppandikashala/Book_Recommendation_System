from collections import defaultdict
import numpy as np

class vpr(object):
	def analysis(self,ratinglist):
		len=len(ratinglist)
		if (len!=0):
			var=
			sum1=0
			for i in range(len):
				sum1=sum1+ratinglist[i]
			avg=sum1/len
			return avg
		else:
			return 0
			
			
			
'''from collections import defaultdict

L = [1,2,45,55,5,4,4,4,4,4,4,5456,56,6,7,67]
d = defaultdict(int)
for i in L:
    d[i] += 1
result = max(d.iteritems(), key=lambda x: x[1])
print result[0]	'''		
