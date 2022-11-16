from tkinter import*


fenetre1=Tk()
fenetre1.title('Exercice 1')


def ouvrir():
    patryck = PhotoImage(file='pc.png')
    item = can1.create_image(300, 300, image = patryck)
     
   
    can1.image = patryck
     
    can1.pack()

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
#------------------------------------------------ 

fenetre1.mainloop()