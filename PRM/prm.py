import numpy as np
import sys
import matplotlib.pyplot as plt
import random
import math
from collections import deque

def main():

	valid_theta_arr = np.zeros(shape=(2000,2))
	the_list = []
	visit ={}
	valid_theta_list =[]
	invalid_theta_list =[]
	flags=1
	xy = np.zeros(shape=(2000,2))#matrix
	mat= np.zeros(shape=(2000,2))
	vtheta1 =[]
	xmat=[]
	ymat=[]
	vtheta2=[]
	itheta1 =[]
	itheta2=[]
	validc=0
	invalidc=0
	
	
	
	def BFS(adj):
		
		lenc =0
		predec = [-1]*len(adj)
		queue = deque()
		queue.append(0)
		v = ["U"]*len(adj)
		v[0] = "V"
		while(len(queue)!=0):
			val = queue.popleft()
			

			for i in range(0,len(adj)):
				if(adj[val][i] == 1 and v[i] == "U"):
					predec[i] = val
					v[i] = "V"
					lenc=lenc+1
					queue.append(i)
		print "lenc"
		print lenc
		return predec

	#f = open('prm.txt', 'r+b')
	
	
	mat[0][0]=math.radians(45)
	mat[0][1]=math.radians(-45)
	the_list= [math.degrees(mat[0][0]),math.degrees(mat[0][1])]
	valid_theta_list.append(the_list)
	
	for i in range(1,1999):
			mat[i][0]=math.radians(random.randrange(0,180))
			mat[i][1]=math.radians(random.randrange(-180,180))


	for T in range(0,2000):

		xy[T][0] = math.cos(mat[T][0])+math.cos(mat[T][0]+mat[T][1])
		xy[T][1] = math.sin(mat[T][0])+math.sin(mat[T][0]+mat[T][1])
		if (
		(xy[T][0] > 1 and xy[T][1] > 1) or 
		(xy[T][0] <-1 and xy[T][1] > 1) or
		(xy[T][0] < 0  and xy[T][1] < 0) or
		(xy[T][0] > 0 and xy[T][1] <0 )
		):	
			#the_list= [math.degrees(mat[T][0]),math.degrees(mat[T][1])]
			#the_list.append(mat[T][1])
			validc=validc+1
			itheta1.append(math.degrees(mat[T][0]))
			itheta2.append(math.degrees(mat[T][1]))
			s = str(T)+" Sample ("+str(math.degrees(mat[T][0]))+","+str(math.degrees(mat[T][1]))+") is rejected"+"\n"
			#f.write(s)
			#invalid_theta_list.append(the_list)
		else:
			the_list= [math.degrees(mat[T][0]),math.degrees(mat[T][1])]
			#the_list.append(mat[T][1])
			invalidc= invalidc+1
			vtheta1.append(math.degrees(mat[T][0]))
			vtheta2.append(math.degrees(mat[T][1]))
			s =str(T)+ " Sample ("+str(math.degrees(mat[T][0]))+","+str(math.degrees(mat[T][1]))+") is accepeted"+"\n"
			#f.write(s)
			valid_theta_list.append(the_list)
			
   	#for each theta check for the radius else interpolation
   	#print valid_theta_list
   	mat[1999][0]=math.radians(135)
	mat[1999][1]=math.radians(45)
	the_list= [math.degrees(mat[1999][0]),math.degrees(mat[1999][1])]
	valid_theta_list.append(the_list)

	print valid_theta_list

   	adj = np.zeros(shape=(len(valid_theta_list),len(valid_theta_list)))

   	for i in range(0,len(valid_theta_list)):

   		oldt1 = valid_theta_list[i][0]
   		oldt2= valid_theta_list[i][1]

   		for j in range(0,len(valid_theta_list)):
   			if (j!=i):
   				newt1 = valid_theta_list[j][0]
   				newt2 =	valid_theta_list[j][1]

   				d1 = newt1-oldt1
   				d2 = newt2-oldt2

   				dist = math.sqrt(math.pow(d1,2)+math.pow(d2,2))
   				#print dist
   				#x2 = cos theta1 + cos(theta1+theta2)
				#y2 = sin theta1 + sin(theta1+theta2)
   				if(dist<15):
   					xold = math.cos(math.radians(oldt1))+math.cos(math.radians(oldt1)+math.radians(oldt2))
					yold= math.sin(math.radians(oldt1))+math.sin(math.radians(oldt1)+math.radians(oldt2))
					xnew = math.cos(math.radians(newt1))+math.cos(math.radians(newt1)+math.radians(newt2))
					ynew= math.sin(math.radians(newt1))+math.sin(math.radians(newt1)+math.radians(newt2))
					x_inc = math.fabs(xnew-xold)/10
					y_inc = math.fabs(ynew-yold)/10
					flags=1
					for z in range(0,10):
						xold= xold+x_inc
						yold= yold+y_inc
						if (
							
						(xold > 1 and yold > 1) or
						(xold < -1 and yold > 1) or 
						(xold < 0 and yold < 0) or
						(xold > 0 and yold < 0)
						):
							flags =0
							break
						
					if(flags==1):
						adj[i][j]=1



	#print adj
	print len(adj)
	print "adj length"
	pred = BFS(adj)
	#print pred
	t = len(pred)-1
	p = []
	p.append(t)
	while(t!=0):
		p.append(pred[t])
		t = pred[t]
	p.reverse()
	
	print p
	
	for i in p:
		print valid_theta_list[i][0]
		print valid_theta_list[i][1]
		xmat.append(valid_theta_list[i][0])
		ymat.append(valid_theta_list[i][1])

	plt.plot(itheta1,itheta2,'rx')
	plt.plot(vtheta1,vtheta2,'g.')
	plt.plot(xmat,ymat)
	plt.show()
	
	#print "length of the shortest path from source to the destination"
	#print number
			

if __name__ == '__main__':
    main()



 