import numpy as np
import sys
import matplotlib.pyplot as plt
import random

def main():
    valid_theta_arr = np.zeros(shape=(2000,2))
    the_list = []
    tree_list =[]
    tree_init =[]

    
    
        #print small
        #print "small"
        #print len(tree_list)
        
        

    pred =[]
    mat= np.zeros(shape=(2000,2))
    tree_init= [45,-45]
    tree_list.append(tree_init)
    min_arr = {}
    the_new_list =[]
    poslist=[]
    xy = np.zeros(shape=(2000,2))#matrix
   
    for i in range(0,2000):

        while (tree_list[len(tree_list)-1][0]!=math.radians(135) or tree_list[len(tree_list)-1][1]!=math.radians(45)):
                x=np.random.rand(1)
                
                if x<=0.1:
                    #tree_list[i][0]=135
                    #tree_list[i][1]=45
                    x=math.radians(135)
                    y=math.radians(45)
                    the_list= [math.degrees(x),math.degrees(y)]
                    oldt1 = math.degrees(x)
                    oldt2 = math.degrees(y)
                    d3 = oldt1-(45)
                    d4 = oldt2-(-45)
                    
                    small = math.sqrt(math.pow(d3,2)+math.pow(d4,2))
                    pos=0
                    for k in range(0,len(tree_list)):
                        newt1 = (tree_list[k][0])
                        newt2 = (tree_list[k][1])
                        d1= newt1-oldt1
                        d2= newt2-oldt2
                        element = math.sqrt(math.pow(d1,2)+math.pow(d2,2))
                        #print element
                        if(element<small):
                            small = element
                            pos =k
                            
                    #print pos
                    internewt1=(tree_list[pos][0])
                    internewt2= (tree_list[pos][1])
                    #poslist =[internewt1,internewt2]
                    d6 = oldt1-internewt1
                    d7 = oldt2-internewt2
                    xold = math.cos(math.radians(oldt1))+math.cos(math.radians(oldt1+oldt2))
                    yold= math.sin(math.radians(oldt1))+math.sin(math.radians(oldt1+oldt2))
                    xnew = math.cos(math.radians(internewt1))+math.cos(math.radians(internewt1+internewt2))
                    ynew= math.sin(math.radians(internewt1))+math.sin(math.radians(internewt1+internewt2))
                    x_inc = (xnew-xold)/10
                    y_inc = (ynew-yold)/10
                    flags5 =1
                    for z in range(0,10):
                        xold= xold+x_inc
                        yold= yold+y_inc
                        if (
                            
                        (xold > 1 and yold > 1) or
                        (xold < -1 and yold > 1) or 
                        (xold < 0 and yold < 0) or
                        (xold > 0 and yold < 0)
                         ):
                            flags5 =0
                            break
                        
                    if(flags5==1):
                        tree_list.append(the_list)
                        # pred.append(the_list)
                        poslist=[len(tree_list)-1,pos]
                        pred.append(poslist)

                   
                else:
                    a=math.radians(random.uniform(0,180))
                    b=math.radians(random.uniform(-180,180))
                    the_list= [math.degrees(a),math.degrees(b)]
                    #this has goal state values
                    xy[i][0] = math.cos(a)+math.cos(a+b)
                    xy[i][1] = math.sin(a)+math.sin(a+b)
                    if (
                    (xy[i][0] > 1 and xy[i][1] > 1) or
                    (xy[i][0] < -1 and xy[i][1] > 1) or 
                    (xy[i][0] < 0 and xy[i][1] < 0) or
                    (xy[i][0] > 0 and xy[i][1] < 0)
                    ):  
                        break

                    else:
                      
                        oldt1 = math.degrees(a)
                        oldt2 = math.degrees(b)
                        d3 = oldt1-(45)
                        d4=oldt2-(-45)
                        
                        small = math.sqrt(math.pow(d3,2)+math.pow(d4,2))
                        pos=0
                        for k in range(0,len(tree_list)):
                            newt1 = (tree_list[k][0])
                            newt2 = (tree_list[k][1])  
                            d1= newt1-oldt1
                            d2= newt2-oldt2
                            element = math.sqrt(math.pow(d1,2)+math.pow(d2,2))
                            #print element
                            if(element<small):
                                small = element
                                pos =k
                        #print pos
                        internewt1= (tree_list[pos][0])
                        internewt2= (tree_list[pos][1])
                        #poslist =[internewt1,internewt2]
                        d6 = oldt1-internewt1#random one -posone 
                        d7 = oldt2-internewt2
                        xold = math.cos(math.radians(oldt1))+math.cos(math.radians(oldt1+oldt2))
                        yold= math.sin(math.radians(oldt1))+math.sin(math.radians(oldt1+oldt2))
                        xnew = math.cos(math.radians(internewt1))+math.cos(math.radians(internewt1+internewt2))
                        ynew= math.sin(math.radians(internewt1))+math.sin(math.radians(internewt1+internewt2))
                        x_inc = (xnew-xold)/10
                        y_inc = (ynew-yold)/10
                        flags3 =1
                        for z in range(0,10):
                            xold= xold+x_inc
                            yold= yold+y_inc
                            if (
                            
                            (xold > 1 and yold > 1) or
                            (xold < -1 and yold > 1) or 
                            (xold < 0 and yold < 0) or
                            (xold > 0 and yold < 0)
                            ):
                                flags3 =0
                                break
                        
                        if(flags3==1):
                            tree_list.append(the_list)
                            #pred.append()
                            poslist=[len(tree_list)-1,pos]
                            pred.append(poslist)
                            #pred.append()
                       # predecessr array has random number and pos 
    #print tree_list

    #print pred
    
    print pred
    p=[]
    #print len(pred)
    y=pred[len(pred)-1][0]
    z=pred[len(pred)-1][1]
    print pred[len(pred)-1][0]
    p.append(y)
    #p.append(z)
    a =pred[len(pred)-1][1]
    while (x!=0):
        x= pred[a-1][1]
        m = pred[a-1][0]
        a=x
        p.append(m)
        #p.append(x)
        print x

    print p
    p.reverse()
    xmat=[]
    ymat=[]
    for i in p:
        xmat.append(tree_list[i][0])
        ymat.append(tree_list[i][1])
    #plt.plot(tree_list,pred,'rx')
    #plt.plot(pred,pred,'g.')
    plt.plot(xmat,ymat)
    plt.show()
if __name__ == '__main__':
    main()