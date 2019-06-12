import collections
import operator

def sep(x):
    a=75-int(len(x))
    #print (a)
    return("-"*a+x+"-"*5)
#------------------------------------------------------------------------------------------
indi=[]
for i in range(5,9):
    indi.append(i)
print (indi)
indi.insert(1,33)
print (indi)

a=ord("a")
z=ord("z")+1


print (sep("alphabet"))
alpha=[chr(i)*3 for i in range(a,z)]
print ("alpha",alpha)

#------------------------------------------------------------------------------------------
indiceVoyelles=[]
for l in 0,4,8,14,20:
        indiceVoyelles.append(l)
print ("indice voyelles\n",indiceVoyelles)

#------------------------------------------------------------------------------------------
vo={}
voy={}
print (sep("liste des voyelles avec leur indice"))
for l in indiceVoyelles:
        vo[l]=alpha[l]
print ("normal \n",vo)
print ("liste des voyelles avec leur indice classé par ordre croisant ")
voy = sorted(vo.items(), key=operator.itemgetter(0))
 
print ("sorted\n",voy)
 
 
 #------------------------------------------------------------------------------------------
print (sep("enumerate indiceVoyelles"))
vo={}
for l,m in enumerate(indiceVoyelles):
    print ("enumerate",l,m)
    vo[l]=alpha[m]
print ("enumerate indiceVoyelles\n",vo)
    


##indi={}
##for i in range(5,9):
    ##indi.insert(i)
##print (indi)



##tulple
indi=(9,9,9)
indi=0,4,8,14,20
for i in range(len(indi)):
    print ("tulple",indi[i])
print (indi)

 
