from tkinter import*
from PIL import Image, ImageTk
import tkinter as tk
import random

fenetre1=Tk()
fenetre1.title('R309 - TP2 - Balazuc Mathéo')

fenetre1.geometry("1500x900")

canvas = Canvas(fenetre1, width=1000, height=500, bg="white")
canvas.pack(pady=20)

def left(e):
   x = -20
   y = 0
   canvas.move(image1,image2, x, y)

def right(e):
   x = 20
   y = 0
   canvas.move(image1,image2, x, y)

def up(e):
   x = 0
   y = -20
   canvas.move(image1,image2, x, y)

def down(e):
   x = 0
   y = 20
   canvas.move(image1,image2, x, y)

def move(e):
   global image1
   image1 = ImageTk.PhotoImage(Image.open('pc.png'))  
   canvas.create_image(e.x, e.y, anchor=NW, image=image1)
 


###############################################################Dessiner un ligne clic droit au debut de la position souhaitez et clic droit à la fin de la position souhaitez

def clic(event):
    canvas.delete(tk.ALL)

def draw_line(e):
   x, y = e.x, e.y
   if canvas.old_coords:
      x1, y1 = canvas.old_coords
      canvas.create_line(x, y, x1, y1, width=5)
   canvas.old_coords = x, y
canvas.old_coords = None

canvas.bind('<ButtonPress-2>', draw_line)               #Clic droit

canvas.bind("<B1-Motion>", move)                        #Clic gauche
#canvas.bind('<Button-3>', clic)

###############################################################Création de la barre de menu
def tabeffacer(): 
    tableau.delete(ALL)         # Effacement du tableau 
 
                                # Création de la barre de menu
menuDraweasy = Menu(fenetre1)
 
                                # Création du menu fichier
fichier = Menu(menuDraweasy)
menuDraweasy.add_cascade(label="Quitter",menu=fichier)                 # On crée une barre de menu
fichier.add_command(label="Quitter le programme", command=fenetre1.destroy)         # On ajoute une option au menu

                                                            # Création du menu déplacer
deplacer = Menu(menuDraweasy)
menuDraweasy.add_cascade(label="Déplacer",menu=deplacer)
deplacer.add_command(label="Déplacer un objet", command=canvas.move) 
 
                                                                    # Création du menu effacer
effacer = Menu(menuDraweasy)
menuDraweasy.add_cascade(label="Effacer",menu=effacer)
effacer.add_command(label="Effacer le tableau", command=canvas.destroy)        
 
                                                                # Afficher le menu
fenetre1.config(menu=menuDraweasy)

############################################################### Lien images 

image1 = tk.PhotoImage(file = "pc.png")
image2 = tk.PhotoImage(file = "switch.png")
image3 = tk.PhotoImage(file = "routeur.png")

############################################################### Bouton affichage



#########################Boutton afficher PC
def affichepc():
    canvas.create_image (random.randint(50,160),random.randint(60,125),image = image1)  
    imageLabel.configure(image = image)
    imageLabel.image = image

frame = tk.Frame(fenetre1)
frame.pack()

button = tk.Button(frame,
                   text="Afficher PC",
                   command=affichepc)
button.pack(side=tk.LEFT)

imageLabel = tk.Label(frame)
imageLabel.pack(side=tk.LEFT)
    
#########################Boutton afficher SWITCH
def afficheswitch():
  
    canvas.create_image (random.randint(50,160),random.randint(60,125),image = image2)
    imageLabel.configure(image = image)
    imageLabel.image = image

frame = tk.Frame(fenetre1)
frame.pack()

button = tk.Button(frame,
                   text="Afficher SWITCH",
                   command=afficheswitch)
button.pack(side=tk.LEFT)

imageLabel = tk.Label(frame)
imageLabel.pack(side=tk.LEFT)

################################Boutton afficher Routeur
def afficherouteur():
  
    canvas.create_image (random.randint(50,160),random.randint(60,125),image = image3)
    imageLabel.configure(image = image)
    imageLabel.image = image

frame = tk.Frame(fenetre1)
frame.pack()

button = tk.Button(frame,
                   text="Afficher ROUTEUR",
                   command=afficherouteur)
button.pack(side=tk.LEFT)

imageLabel = tk.Label(frame)
imageLabel.pack(side=tk.LEFT)

###############################Indication pour dessiner une ligne 
def afficheligne():
   frame = tk.Frame(fenetre1)
   frame.pack()

button = tk.Button(frame,
                   text="Clique DROIT de votre souris pour dessiner une LIGNE",
                   command=afficheligne)
button.pack(side=tk.LEFT)

imageLabel = tk.Label(frame)
imageLabel.pack(side=tk.LEFT)

fenetre1.mainloop()