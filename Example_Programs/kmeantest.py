
from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
from scipy.cluster.vq import kmeans, vq, whiten

import csv




class cluster(object):
    def KMEANS(self):
	    # clusters
	    K = 3

	    data_arr = []
	    meal_name_arr = []
            f1=open("./NewDataSet/Cluster_dataset/toprated.txt","w")
            f2=open("./NewDataSet/Cluster_dataset/medrated.txt","w")
            f3=open("./NewDataSet/Cluster_dataset/lowrated.txt","w")
	    with open('./NewDataSet/Cluster_dataset/clusterisbnrate.csv', 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
		    if reader.line_num != 1:
		    	'''for x in row[2:]:
		    		print x'''
		    	data_arr.append([float(x) for x in row[1:]])
		    	meal_name_arr.append([row[0]])
	    
	    data = vstack( data_arr )
	    print "data  :"
	    print data
	    meal_name = vstack(meal_name_arr)

	    # normalization
	    data = whiten(data)

	    # computing K-Means with K (clusters)
	    centroids, distortion = kmeans(data,3)
	    print "distortion = " + str(distortion)
	    

	    # assign each sample to a cluster
	    cntr=[]
	    print ("Centroids:")
	    print centroids
	    cntr=centroids
	    print ("Cntr  :")
	    print cntr
	    print "--------------------------------------------------------"
	    #centroids=cntr.sort()
	    #idx,_ = vq(data,centroids)
	    #print centroids.sort()
	    
	    
	    print "---------------------------------------------------------"
	    
	    idx,_ = vq(data,centroids)#vq=vector quantization
	    print "idx:"
	    print idx
	    print"-----------------------------------------------------------"

	    '''# some plotting using numpy's logical indexing
	    plot(data[idx==0,0], data[idx==0,1],'ob',
		 data[idx==1,0], data[idx==1,1],'or',
		 data[idx==2,0], data[idx==2,1],'og')'''

	    print meal_name
	    print data
	    
	    for i in range(K):
	    	print centroids[i]*3
	    	#print round(centroids[i])

	    print "max value:"
	    max1=max(centroids)
	    
	    print "min value:"
	    min1=min(centroids)
	    toprated=[]
	    lowrated=[]
	    medrated=[]
	    for i in range(K):
		result_names = meal_name[idx==i, 0]

		print "================================="
		vv= round(centroids[i])
		print vv
		name=""
		print "Cluster " + str(i+1)
		for name1 in result_names:
		    name=name1
		    print name1
		    
		    '''if(i== 0) :
		    	f1.write(name)
		    elif (i==1):
		    	f2.write(name)
		    elif (i==2):
		    	f3.write(name)'''
		    	
		    if (centroids[i]==max1):
		    	#for name1 in result_names:
		    	toprated.append(name)
		    	name=name1+"\n"
		    	f1.write(name)
		    elif(centroids[i]==min1):
		    	lowrated.append(name)
		    	name=name1+"\n"
		    	f3.write(name)
		    else:
		    	medrated.append(name)
		    	name=name1+"\n"
		    	f2.write(name)
	    f1.close()
	    f2.close()
	    f3.close()
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
	    

	    
	    



