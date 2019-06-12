#import tkinter as tk # this is the preferred import for tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.filedialog import askopenfile
 
##-------------------------------------------------------------------------------------
root = Tk()

root.title('lire un fichier texte')

##root.minsize(200,100)
##root.configure(background='grey')

  
##P = Text(root, height=2, width=30,wrap=WORD)
##P.pack()
##P.insert(END, "Just a text Widget\nin two lines\n")
 

#top= Toplevel()
label = Label(root, text='coucou')
label.pack()

  
P = Text(root, height=20, width=30,wrap=WORD)
P.pack()
P.insert(END, "Just a text Widget\nin two lines\n")

msg = Message(root, text="du baratin pour le message")
msg.pack()

button = Button(root, text="Dismiss", command=root.destroy)
button.pack()

n=0
lignes=[]
tableauMots=[]
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
   
##-------------------------------------------------------------------------------------
def ouvrir_():
    n=0
    lignes=[]
    tableauMots=[]
    x = filedialog.askopenfilename()
    print(x)
    return(x)
##-------------------------------------------------------------------------------------
win = Canvas( width=200, height=100,bg="lightblue")#inactif
#win.pack()

Label(text="choisir un fichier texte").pack(side=TOP)
#placer les boutons dans un frame
f=Frame(width=200,height=50,bg="gold")
#frame1.configure(background='gold')
 
Button ( text = " ", command = ouvrir,bg="red").pack( )

#Button.configure(background='gold')
#frame1.pack()
#separator = Frame(height=2, bd=1 )
#separator.pack(fill=X, padx=5, pady=5)

win.pack()
win.create_text(50,10,fill="darkblue",
                font="Times 8 italic  ",
                text="Click the bubbles that are multiples of two.")
win.update
    

##-------------------------------------------------------------------------------------
ouvrir()
 
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
    P.insert('end',i,'\n' )
    print ("\\",i[1],i[2])
 

        
#fichier = open(x, "r")
print (fichier.read())
fichier.close()


mainloop()
