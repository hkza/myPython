import collections
from tkinter import *
import os
 
import operator

root = Tk()
 
alpha=[chr(i)*3 for i in range(ord("a"),ord("z")+1)]
print ("alpha",alpha)
indiceVoyelles=[]
for l in 0,4,8,14,20:
        indiceVoyelles.append(l)
print ("indice des voyelles\n",indiceVoyelles)
#------------------------------------------------------------------------------------------
def sep(x):
    a=75-int(len(x))
    #print (a)
    return("-"*a+x+"-"*5)
#------------------------------------------------------------------------------------------
def A():
    
    print (sep("alphabet"))
    
    te= "\nindi=[]\n for i in range(5,9):\n\tindi.append(i)"
    t.delete('1.0',END)
    t.insert('1.0',te)
    
    indi=[]
    for i in range(5,9):
        indi.append(i)
    print (indi)
    
    indi.insert(1,33)
    print (indi, indi[1])
 
    ##




#------------------------------------------------------------------------------------------
def B():
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
def C():
    
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


def D():
    
    ##tulple
    indi=(9,9,9)
    indi=0,4,8,14,20
    for i in range(len(indi)):
        print ("tulple",indi[i])
    print (indi)

 #------------------------------------------------------------------------------------------
def query_checkbuttons( ):
    print("Mode",CHECKED.get())
    return(CHECKED.get())
 #------------------------------------------------------------------------------------------
def go():
    import os
    os.system('cls||clear')
    exec(query_checkbuttons()+"()")
    return()
 #------------------------------------------------------------------------------------------
MODES = [
("Monochrome", "A"),
("Grayscale", "B"),
("True color", "C"),
("Color separation", "D"),
]
CHECKED = StringVar()
CHECKED.set("L") # initialize

b =Button (root, text = "go", command = go,bg="red")
b.pack(side=LEFT)
t = Text(root, width=60 , height=10, bg="darkblue", fg="white" ,font ="courier" )
t.pack()


for text, mode in MODES:
        b = Radiobutton(root,text=text,variable=CHECKED,value=mode,command=query_checkbuttons)
        b.pack(anchor=W)

root.mainloop()
 
