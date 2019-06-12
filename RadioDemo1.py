from tkinter import *

root = Tk()
chk=[]
style={}
b="toto"

 
# Champ d'entrée contenant un petit zoneTXT :
texte="La programmation, c'est génial"
zoneTXT = Entry(root, width =30, font ="Arial 12")
zoneTXT.insert(END, texte)
zoneTXT.pack(padx =8, pady =8)

# Nom français et nom technique des quatre styles de police :
styleFr =["Normal", "Gras", "Italique", "Gr+It"]
styleTk =["normal", "bold", "italic"  , "bold italic"]

zipped = zip(styleFr, styleTk)
for i,j in zipped:
        style[i]=j
  
print("style",style)

# Le style actuel est mémorisé dans un 'objet-variable' Tkinter ;
CHOIX_POLICE = StringVar()
CHOIX_POLICE.set(styleTk[0])

# Création des quatre 'boutons radio' :

def changePolice( ):
        """Remplacement du style de la police actuelle"""
        
        police = "Arial 15 " + CHOIX_POLICE.get()
        text= "c'est génial en "+police
        zoneTXT.delete(0, END)
        zoneTXT.configure(font =police)
        zoneTXT.insert(END, text)


for n in range(4):
        bout = Radiobutton(root,
               text = styleFr[n],
               variable = CHOIX_POLICE,
               value = styleTk[n],
               command = changePolice)
        bout.pack(side =LEFT, padx =5)


root.mainloop()
