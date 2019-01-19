a="sfdgdg gfhf g tyrhfhgf jh.$hfgfyrthfgbfthrn fyhtfghf bvhgftrhgfb sfdtrg.$trhyfuthyfthryterfdgt."
x=len(a)
print x
s=[]
j=0
strs=""
for i in range(x):
	if(a[i]!="$" and i!=(x-1)):
		#print a[i]
		strs=strs+a[i]
	else:
		print strs
		s.append(strs)
		strs=""
print s
f=len(s)
print f
for i in range(f):
	print s[i] 
