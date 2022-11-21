from tkinter import*
from PIL import Image, ImageTk

fenetre1=Tk()
fenetre1.title('Exercice 1 - Balazuc Mathéo')

fenetre1.geometry("900x750")

canvas = Canvas(fenetre1, width=900, height=700, bg="white")
canvas.pack(pady=20)

image = ImageTk.PhotoImage(Image.open('routeur.png'))
img = canvas.create_image(150, 80, anchor=NW, image=image)

def left(e):
   x = -20
   y = 0
   canvas.move(img, x, y)

def right(e):
   x = 20
   y = 0
   canvas.move(img, x, y)

def up(e):
   x = 0
   y = -20
   canvas.move(img, x, y)

def down(e):
   x = 0
   y = 20
   canvas.move(img, x, y)

def move(e):
   global image
   image = ImageTk.PhotoImage(Image.open('routeur.png'))
   img = canvas.create_image(e.x, e.y, image=image)

canvas.bind("<B1-Motion>", move)


                                #Création de la barre de menu
def tabeffacer(): 
    canvas.delete(ALL)         # Effacement du tableau 
 
                                # Création de la barre de menu
menuDraweasy = Menu(fenetre1)
 
                                # Création du menu fichier
fichier = Menu(menuDraweasy)
menuDraweasy.add_cascade(label="Fichier",menu=fichier)                 # On crée une barre de menu
fichier.add_command(label="Quitter", command=fenetre1.destroy)         # On ajoute une option au menu

                                                            # Création du menu déplacer
deplacer = Menu(menuDraweasy)
menuDraweasy.add_cascade(label="Déplacer",menu=deplacer)
deplacer.add_command(label="Déplacer cet item", command=lambda : tabdeplacer()) 
 
                                                                    # Création du menu effacer
effacer = Menu(menuDraweasy)
menuDraweasy.add_cascade(label="Effacer",menu=effacer)
effacer.add_command(label="Effacer tout", command=lambda : tabeffacer())        
 
                                                                # Afficher le menu
fenetre1.config(menu=menuDraweasy)
 

fenetre1.mainloop()