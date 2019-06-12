from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import filedialog
import random

# Set number of rows and columns
ROWS = 6
COLS = 5
tuiles=[]
 
print (  tuiles)
n=0
lignes=[]
table=[]
couls={}
names={}

FILETYPES = [ ("text files", "*.csv") ]
##-------------------------------------------------------------------------------------
#root.geometry("200x200")
fichier=""
def ouvrir():
    global peinture,fichier
    fichier=(filedialog.askopenfilename(filetypes=FILETYPES))
    print(fichier)
    
    return(fichier)
    
def lire (fichier):
    if (len(fichier) != 0):
        fichier= open( fichier,"r")
        print ("ouverture de ",fichier)
    else:
        fichier = open ("lunohodov_ral_standard.csv" , "r")
    n=0
    for line in fichier.readlines():
        n=n+1
        # Traiter la ligne et ainsi de suite ...
        #print("ligne=",n," ",line )
        #lignes.append(line )
        #if n>3:break
        lignes=[]
    #print("\nligne==",n,"  "ignes[0])
        k=0
        for Mo in line.split(','):
            #print ("mot",Mo)
            if k==2: 
                chaine=Mo[:-1]
                lignes.append(chaine)
            else:
                lignes.append(Mo )
            
            k+=1
        table.append(lignes)

def tables():
    k=0
    for i in range(len(table)):
        #P.insert('end',i,'\n' )
        ta=table[k]
        chaine=ta[2]
        #print ("-#",i, table[k],ta[1] )
        couls[i]=ta[1]
        names[i]= chaine[:-2]
        k+=1
    #print ("couls,names",couls,names)      
        
def hazard():
    c= randint(len[couls]-1)
    thecoul=couls[c]
    print ("hazard",c,thecoul)
    return thecoul
    
def initRect():
    hu= int
    wu=int
    
    wu = int(wi/COLS/10)
    hu = int(hi/ROWS/10)
    
    for row in range(ROWS):
        for col  in range(COLS):
            print("ligne= ",row,col ,wu,hu)
            ##newR=Label(CANV,col*co,row*ro,(col+1)*co,(row+1)*ro ,fill="grey")
            newR=Label(CANV, width=wu , height=hu, bg="grey", fg="grey"  )
            newR.grid(row=row, column=col, padx=1, pady=1)
            tuiles.append(newR)
    #print("tuiles",tuiles)    
 
#-----------------------------------------------------------------------------------------------
def recta():
    ##print(tuiles)
    for i in  tuiles :
        c=random.randint(0,len(couls)-1)
        thecoul=couls[c]
        theName=names[c]
        ##print ("tuiles",thecoul,theName,i)
        i.configure(bg=thecoul)
        i.configure(text=theName)
#    ----------------------------------------------------------------------------------------------- 
def callback(event):
    # Get rectangle diameters
    col_width = (CANV.winfo_width()/COLS)
    row_height = (CANV.winfo_height()/ROWS)
    # Calculate column and row number
    
    col = int(event.x/col_width)
    row = int(event.y/row_height)
        
    co=col_width
    ro=row_height
  
    # If the tile is not filled, create a rectangle
    if not tiles[row][col]:
        tiles[row][col] = CANV.create_rectangle(
            col*co, row*ro, (col+1)*co, (row+1)*ro, 
            fill="red",width=1,outline="white")
        
    # If the tile is filled, delete the rectangle and clear the reference
    else:
        CANV.delete(tiles[row][col])
        tiles[row][col] = None
               
#-----------------------------------------------------------------------------------------------
# Create the window, a canvas and the mouse click event binding
root = Tk()
b =Button (root, text = " ", command = recta,bg="red")
b.pack()
wi=800
hi=200
CANV = Canvas(root, width=wi, height=hi, borderwidth=5, background='lightgrey')
CANV.pack(padx=12,pady=12)

CANV.bind("<Button-1>", lambda x : recta())
#->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-

#fichier=ouvrir()
initRect()
 
lire("lunohodov_ral_standard.csv")
k=0
tables()
 

root.mainloop()
