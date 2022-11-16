from tkinter import*


fenetre1=Tk()
fenetre1.title('Exercice 1')


def tabeffacer(): 
    tableau.delete(ALL)         # effacement du tableau 
 
# creation de la barre de menu
menuDraweasy = Menu(fenetre1)
 
# creation du menu fichier
fichier = Menu(menuDraweasy)
menuDraweasy.add_cascade(label="Fichier",menu=fichier)                 # on crée une barre de menu
fichier.add_command(label="Quitter", command=fenetre1.destroy)         # on ajoute une option au menu

# creation du menu eplacer
deplacer = Menu(menuDraweasy)
menuDraweasy.add_cascade(label="Déplacer",menu=deplacer)
deplacer.add_command(label="Déplacer cet item", command=lambda : tabdeplacer()) 
 
# creation du menu effacer
effacer = Menu(menuDraweasy)
menuDraweasy.add_cascade(label="Effacer",menu=effacer)
effacer.add_command(label="Effacer tout", command=lambda : tabeffacer())        
 
# afficher le menu
fenetre1.config(menu=menuDraweasy)
    
    
fenetre1.mainloop()