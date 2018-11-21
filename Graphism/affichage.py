from tkinter import *
import os
from PIL import Image
import Core.Core as c
import Game.morpion as m
import os

dir = os.getcwd()
def affichage_init(plateau) :
    l=plateau.Jeu.largeur
    h=plateau.Jeu.hauteur
    liste_cases = [] #stock les cases
    principal = Frame()
    graphical_grid=[[0 for j in range(l)]for i in range(h) ] #stock les valeurs
    for i in range(h) :
        for j in range(l) :
            graphical_grid[i][j]=plateau.get_etat(i,j)
    background = Frame(principal,bg="#C0EDAC",height=400,width=400)
    background.grid()
    for i in range(h) :
        for j in range(l) :
            liste_cases.append(Frame(background,bg="#DCFDFF",height=400/h,width=400/l, bd=2, relief = SOLID))
            x = graphical_grid[i][j]
            #Label(liste_cases[-1],bg="#DCFDFF",image=PhotoImage(file=dir+m.THEME[x])).pack(expand=YES)
            Label(liste_cases[-1], bg="#DCFDFF", text = str(x)).pack(expand=YES)
    for i in range(h) :
        for j in range(l) :
            liste_cases[h*i+j].grid(column=j,row=i)
    return principal

def update(principal,plateau) :
    k=0
    for background in principal.winfo_children():
        for case in background.winfo_children():
            for label in case.winfo_children():
                x = plateau.get_etat(k//plateau.Jeu.largeur,k%plateau.Jeu.largeur)
                #label.config(image=PhotoImage(file=dir+m.THEME[x]))
                label.config(text = str(x))
                k+=1
    principal.update()


def init_fenetre(plateau):
    root = Tk()
    plateau_graphique = affichage_init(plateau)
    plateau_graphique.grid()
    actualiser = Button(root, command = update())
    root.mainloop()

def entree(root, partie, num_tour):
    action = input()
    if not (partie.plateau.est_valide(action)):
        root.after(10, entree)
    return action

def changer_texte(label, texte):
    label.configure(text = texte)

def main(jeu, joueurs):
    partie = c.Partie(jeu, joueurs)
    partie.plateau.initialisation()
    partie.plateau.afficher()

    global num_tour
    num_tour = 0
    root = Tk()
    texte = StringVar()
    message = Label(root, textvariable = texte)
    message.grid(column=1)
    action = StringVar(root)
    entree = Entry(root, textvariable=action, width=30)


    def agir():
        global num_tour
        if not(partie.plateau.termine()):
            if partie.plateau.est_valide(action.get()):
                partie.plateau.next(action.get(), num_tour)
                update(plateau_graphique, partie.plateau)
                texte.set(partie.plateau.message(num_tour, partie.joueurs))
                partie.plateau.afficher()
                num_tour += 1
            else :
                texte.set(partie.plateau.message(num_tour, partie.joueurs)+" Le coup entré n'est pas  valide")
        else :
            texte.set(partie.plateau.resultat(partie.plateau))
        if partie.plateau.termine() :
            texte.set(partie.plateau.resultat(partie.plateau))

        print(entree.get())

    jouer = Button(root, text = "Jouer", command=agir)





    #entree.bind("<Return>", agir)

    plateau_graphique = affichage_init(partie.plateau)
    plateau_graphique.grid(row = 0, column = 0)
    entree.grid(column=1)
    jouer.grid(column=1)



    root.mainloop()

