from tkinter import *
import os
from PIL import Image, ImageTk
import Core.Core as c
import Game.morpion as m
import os

dir = os.getcwd()
def affichage_init(plateau, THEME = {}) :
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
            liste_cases.append(Frame(background,bg="#DCFDFF",height=400/h,width=400/l, bd=1, relief = SOLID))
            x = graphical_grid[i][j]
            if THEME :
                Label(liste_cases[-1],bg="#DCFDFF",image=THEME[x]).pack(expand=YES)
            else :
                Label(liste_cases[-1], bg="#DCFDFF", text = str(x)).pack(expand=YES)
    for i in range(h) :
        for j in range(l) :
            liste_cases[l*i+j].grid(column=j,row=i)
    return principal

def update(principal,plateau, THEME = {}) :
    k=0
    for background in principal.winfo_children():
        for case in background.winfo_children():
            for label in case.winfo_children():
                x = plateau.get_etat(k//plateau.Jeu.largeur,k%plateau.Jeu.largeur)
                if THEME :
                    label.config(image=THEME[x])
                else :
                    label.config(text = str(x))
                k+=1
    principal.update()

def importe(nom):

    if nom == "dames":
        from Game.dames import Dames
        return Dames()
    elif nom == "echecs":
        from Game.echecs import Echec
        return Echec()
    elif nom == "morpion":
        from Game.morpion import Morpion
        return Morpion()
    elif nom == "puissance_4":
        from Game.jeu_puissance_4 import puissance_4
        return puissance_4()
    elif nom == "demineur":
        from Game.demineur import Demineur
        return Demineur()
    elif nom == "2048":
        from Game.jeu_2048 import Jeu_2048
        return Jeu_2048()
    elif nom == "othello":
        from Game.Othello import Othello
        return Othello()
    else :
        print("Choisis un jeu qui existe...")

def main():
    root = Tk()
    saisie = Frame(root)
    global nom_du_jeu
    global jeu
    nom_du_jeu = StringVar()
    nom_du_jeu.set("dames")
    jeu = importe(nom_du_jeu.get())

    def parametres(root, jeu):
        fond = Frame(root)
        vals = ['dames', 'demineur', '2048', 'puissance_4', 'morpion', 'echecs', 'othello']
        etiqs = ['Dames', 'Démineur', '2048', 'Puissance 4', 'Morpion', 'Echecs', 'Othello']
        for i in range(7):
            b = Radiobutton(fond, variable=nom_du_jeu, text=etiqs[i], value=vals[i], command = lambda : changer_jeu(nom_du_jeu.get()))
            b.pack(side='left', expand=1)
        return fond

    settings = parametres(saisie, nom_du_jeu.get())

    global partie
    joueurs = ["Alice", "Bob"]
    partie = c.Partie(jeu, joueurs)
    settings.grid(row = 3, column = 0)
    partie.plateau.initialisation()
    partie.plateau.afficher()

    global num_tour
    num_tour = 0
    global THEME
    THEME = {}
    try :
        for clef, valeur in partie.plateau.Jeu.THEME.items():
            photo = PhotoImage(file = dir+valeur)#ImageTk.PhotoImage(image)
            THEME[clef] = photo
    except :
        print("Pas de Thème configuré")
    print(THEME)

    texte = StringVar()
    message = Label(saisie, textvariable = texte)
    message.grid(column=0, row = 2)
    action = StringVar(saisie)
    entree = Entry(saisie, textvariable=action, width=30)
    global plateau_graphique
    plateau_graphique = affichage_init(partie.plateau, THEME)

    def agir():
        global num_tour
        if not(partie.plateau.termine()):
            if partie.plateau.est_valide(action.get(), num_tour):
                partie.plateau.next(action.get(), num_tour)
                update(plateau_graphique, partie.plateau, THEME)
                texte.set(partie.plateau.message(num_tour, partie.joueurs))
                partie.plateau.afficher()
                num_tour += 1
            else :
                texte.set(partie.plateau.message(num_tour, partie.joueurs)+"\nLe coup entré n'est pas  valide")
        else :
            texte.set(partie.plateau.resultat(partie.plateau))
        if partie.plateau.termine() :
            texte.set(partie.plateau.resultat(partie.plateau))

        print(entree.get())

    def changer_jeu(nom_jeu):
        global jeu
        global partie
        global plateau_graphique
        global THEME
        plateau_graphique.destroy()
        jeu = importe(nom_jeu)
        partie = c.Partie(jeu, joueurs)
        partie.plateau.initialisation()
        THEME = {}
        try:
            for clef, valeur in partie.plateau.Jeu.THEME.items():
                photo = PhotoImage(file=dir + valeur)  # ImageTk.PhotoImage(image)
                THEME[clef] = photo
        except:
            print("Pas de Thème configuré")
        print(THEME)
        plateau_graphique = affichage_init(partie.plateau, THEME)
        plateau_graphique.grid(row = 0, column = 0)
        partie.plateau.afficher()
    jouer = Button(saisie, text = "Jouer", command=agir)

    plateau_graphique.grid(row = 0, column = 0)
    entree.grid(column=0, row = 0)
    jouer.grid(column=0, row = 1)
    saisie.grid(row = 0, column = 1)
    texte.set(partie.plateau.message(num_tour, partie.joueurs))


    root.mainloop()

