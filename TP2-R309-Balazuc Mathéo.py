from tkinter import*


fenetre1=Tk()
fenetre1.title('Exercice 1')

# ------------------------------------ Création de la barre de menu
def tabeffacer(): 
    tableau.delete(ALL)         # Effacement du tableau 
 
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
#------------------------------------------------ Fin de la création menu
    
    
can1 = Canvas(fenetre1, width =160, height =160) 
photo = PhotoImage(file ='pc.png') 
item = can1.create_image(280, 280, image =photo) 
can2 = Canvas(fenetre1, width =160, height =160) 
photo = PhotoImage(file ='routeur.png') 
item = can2.create_image(100, 100, image =photo) 
can3 = Canvas(fenetre1, width =160, height =160) 
photo = PhotoImage(file ='switch.png') 
item = can3.create_image(200, 200, image =photo)

# Mise en page à l'aide de la méthode 'grid' : 
can1.grid(row =1, column =1, rowspan =3, padx =[0,100], pady =5) 
can2.grid(row =10, column =1, rowspan =3, padx =[0,100], pady =5) 
can3.grid(row =20, column =1, rowspan =3, padx =[0,100], pady =5) 

fenetre1.mainloop()