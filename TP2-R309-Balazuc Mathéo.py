from tkinter import*
from PIL import Image, ImageTk
import tkinter as tk

fenetre1=Tk()
fenetre1.title('Exercice 1 - Balazuc Mathéo')

fenetre1.geometry("900x750")

canvas = Canvas(fenetre1, width=700, height=500, bg="white")
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

def create_image():
    image = ImageTk.PhotoImage(Image.open('routeur.png'))
    img = canvas.create_image(150, 80, anchor=NW, image=image)

                                #Création de la barre de menu
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
 

#Boutton afficher PC
def affichepc():
    
    image = tk.PhotoImage(file = "pc.png")
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
    
#Boutton afficher SWITCH
def afficheswitch():
  
    image = tk.PhotoImage(file = "switch.png")
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

#Boutton afficher Routeur
def afficherouteur():
  
    image = tk.PhotoImage(file = "routeur.png")
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


fenetre1.mainloop()