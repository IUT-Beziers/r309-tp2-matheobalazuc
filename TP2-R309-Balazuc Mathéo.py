from tkinter import*
from PIL import Image, ImageTk
import tkinter as tk
import random

fenetre1=Tk()
fenetre1.title('Exercice 1 - Balazuc Mathéo')

fenetre1.geometry("1500x900")

canvas = Canvas(fenetre1, width=1000, height=500, bg="white")
canvas.pack(pady=20)

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
   image1 = ImageTk.PhotoImage(Image.open('pc.png'))  
   img1 = canvas.create_image(150, 80, anchor=NW, image=image1)
  # image = ImageTk.PhotoImage(Image.open('pc.png'))
   #img1 = canvas.create_image(e.x, e.y, image=image1)

   #img2 = canvas.create_image(e.x, e.y, image=image2)
    
   #img3 = canvas.create_image(e.x, e.y, image=image3)




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

def create_image():
    image1 = ImageTk.PhotoImage(Image.open('pc.png'))
    #img1 = canvas.create_image(150, 80, anchor=NW, image=image1)

    image2 = ImageTk.PhotoImage(Image.open('switch.png'))
    #img2 = canvas.create_image(150, 80, anchor=NW, image=image2)
    
    image3 = ImageTk.PhotoImage(Image.open('routeur.png'))
    #img3 = canvas.create_image(150, 80, anchor=NW, image=image3)

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
 
image1 = tk.PhotoImage(file = "pc.png")
image2 = tk.PhotoImage(file = "switch.png")
image3 = tk.PhotoImage(file = "routeur.png")


#Boutton afficher PC
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
    
#Boutton afficher SWITCH
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

#Boutton afficher Routeur
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


fenetre1.mainloop()