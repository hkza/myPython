from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import filedialog

# Set number of rows and columns
ROWS = 6
COLS = 5

# Create a grid of None to store the references to the tiles
#   _ Ignore the index
tiles = [[x for x in range(COLS)] for _ in range(ROWS)]
tuiles=[x for x in range(COLS*ROWS)]
print (tiles, tuiles)
n=0
lignes=[]
 
table=[]


FILETYPES = [ ("text files", "*.csv") ]
##-------------------------------------------------------------------------------------
#root.geometry("200x200")
fichier=""
def ouvrir():
    global peinture,fichier
    #BufferedReader = askopenfile(parent=root,mode='rb',title='Choisir un fichier', filetypes=[("csv", '*.csv')])
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
        print("ligne=",n," ",line )
        #lignes.append(line )
        if n>3:break
        lignes=[]
    #print("\nligne==",n,"  ", lignes[0])
        
        for Mo in line.split(','):
            #print ("mot",Mo)
            lignes.append(Mo )
        table.append(lignes)

    print("",table)
    ##S=sorted(set(lignes))
    ##print("\n",len(sorted(set(lignes))),S)

    for i in table:
        #P.insert('end',i,'\n' )
        print ("\\",i[1],i[2])
    
#-----------------------------------------------------------------------------------------------
def recta():
    co = (CANV.winfo_width()/COLS)
    ro = (CANV.winfo_height()/ROWS)
    
    tiles = [[None for _ in range(COLS)] for _ in range(ROWS)]
    k=0
    for row in range(COLS):
        for col  in range(ROWS):
            tuiles[k] = CANV.create_rectangle(
            col*co,row*ro,(col+1)*co, (row+1)*ro,
            fill="olive",width=1,outline="white")
            k+=1
    print(tuiles)
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
            fill="olive",width=1,outline="white")
        
    # If the tile is filled, delete the rectangle and clear the reference
    else:
        CANV.delete(tiles[row][col])
        tiles[row][col] = None
#-----------------------------------------------------------------------------------------------
# Create the window, a canvas and the mouse click event binding
root = Tk()
CANV = Canvas(root, width=300, height=300, borderwidth=5, background='lightgrey')
CANV.pack(padx=12,pady=12)

CANV.bind("<Button-1>", lambda x : recta())

fichier=ouvrir()
lire(fichier)
k=0
couls={}
names={}
for i in range(len(table)):
        #P.insert('end',i,'\n' )
        ta=table[k]
        chaine=ta[2]
        print ("--",i, table[k],ta[1] )
        couls[i]=ta[1]
        names[i]= chaine[:-2]
        k+=1
print ("couls,names",couls,names)
        
##for i in table:
        ###P.insert('end',i,'\n' )
        ##print ("\\",i[1],i[2])


root.mainloop()
