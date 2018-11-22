from tkinter import *
import os
from PIL import Image, ImageTk
import Core.Core as c
import Game.morpion as m
import os
#ias = [zertyu,ertyui]
dir = os.getcwd()
import time

pile = []
tour_humain = True

def test_click(event):
    if mode.get() == 0 :
        global pile
        s = str(event.widget)
        action = s[-s[::-1].index("."):]
        print(action)
        i, j = action.split()
        if nom_du_jeu.get() in ["demineur", "morpion", "othello"]:
            agir(action)
        elif nom_du_jeu.get()=="puissance_4":
            agir(j+" "+str(num_tour%2 +1))
        else :
            pile.append(i+j)
            print(pile)
            if len(pile) == 2:
                agir(pile[0]+" "+pile[1])
                pile = []


    elif jeu.nb_joueurs == 1 and mode == 1:
        while not(partie.plateau.termine()):
            action = ias[0].jouer(partie.plateau)
            agir(action)
            time.sleep(0.1)

    elif jeu.nb_joueurs == 2 :
        if mode.get() == 1 :
            global pile
            s = str(event.widget)
            action = s[-s[::-1].index("."):]
            print(action)
            i, j = action.split()
            if nom_du_jeu.get() in ["demineur", "morpion", "othello"]:
                agir(action)
            elif nom_du_jeu.get() == "puissance_4":
                agir(j + " " + str(num_tour % 2 + 1))
            else:
                pile.append(i + j)
                print(pile)
                if len(pile) == 2:
                    agir(pile[0] + " " + pile[1])
                    pile = []

            action = ias[0].jouer(partie.plateau)
            agir(action)


        elif mode.get() == 2 :
            while not (partie.plateau.termine()):
                action = ias[0].jouer(partie.plateau)
                agir(action)
                time.sleep(0.2)
                if not (partie.plateau.termine())
                    action = ias[1].jouer(partie.plateau)
                    agir(action)
                    time.sleep(0.2)







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
                Label(liste_cases[-1],bg="#DCFDFF",image=THEME[x], name=str(i)+" "+str(j)).pack(expand=YES)
            else :
                Label(liste_cases[-1], bg="#DCFDFF", text = str(x), name=str(i)+" "+str(j)).pack(expand=YES)
    for i in range(h) :
        for j in range(l) :
            liste_cases[l*i+j].grid(column=j,row=i)
            liste_cases[l * i + j].winfo_children()[0].bind("<Button-1>", test_click)
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

def agir(action):
    global num_tour
    if not(partie.plateau.termine()):
        if partie.plateau.est_valide(action, num_tour):
            partie.plateau.next(action, num_tour)
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



def main():
    root = Tk()
    side = Frame(root)
    saisie = Frame(side)

    global mode
    global nom_du_jeu
    global jeu
    global choix
    mode = IntVar()
    nom_du_jeu = StringVar()
    nom_du_jeu.set("dames")
    jeu = importe(nom_du_jeu.get())
    top = Frame(side)
    def choix_joueurs(root):
        fond = Frame(root)
        if jeu.nb_joueurs == 1:
            vals = [0, 1]
            etiqs = ['Humain', 'IA']
            for i in range(2) :
                b = Radiobutton(fond, variable=mode, text=etiqs[i], value=vals[i])
                b.pack(side='left', expand=1)
        if jeu.nb_joueurs == 2:
            vals = [0, 1, 2]
            etiqs = ['Humain vs Humain', 'Humain vs IA', 'IA vs IA']
            for i in range(3) :
                b = Radiobutton(fond, variable=mode, text=etiqs[i], value=vals[i])
                b.pack(side='left', expand=1)

        return fond




    def parametres(root):
        fond = Frame(root)
        vals = ['dames', 'demineur', '2048', 'puissance_4', 'morpion', 'echecs', 'othello']
        etiqs = ['Dames', 'Démineur', '2048', 'Puissance 4', 'Morpion', 'Echecs', 'Othello']
        for i in range(7):
            b = Radiobutton(fond, variable=nom_du_jeu, text=etiqs[i], value=vals[i], command = lambda : changer_jeu(nom_du_jeu.get()))
            b.pack(side='left', expand=1)
        return fond

    settings = parametres(top)
    choix = choix_joueurs(saisie)
    global partie
    joueurs = ["Alice", "Bob"]
    partie = c.Partie(jeu, joueurs)
    settings.grid()
    choix.grid(row=4, column=0)
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
    global texte
    texte = StringVar()
    message = Label(saisie, textvariable = texte)
    message.grid(column=0, row = 2)
    action = StringVar(saisie)
    entree = Entry(saisie, textvariable=action, width=30)
    global plateau_graphique
    plateau_graphique = affichage_init(partie.plateau, THEME)

    def changer_jeu(nom_jeu):
        global choix
        global jeu
        global partie
        global plateau_graphique
        global THEME
        choix.destroy()
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
        choix = choix_joueurs(saisie)
        choix.grid(row=4, column=0)

    jouer = Button(saisie, text = "Jouer", command=lambda : agir(action.get()))
    top.grid(row = 0, column = 0)
    plateau_graphique.grid(row = 0, column = 0)
    entree.grid(column=0, row = 0)
    jouer.grid(column=0, row = 1)
    saisie.grid(row = 1, column = 0)
    side.grid(row = 0, column = 1)
    texte.set(partie.plateau.message(num_tour, partie.joueurs))


    root.mainloop()

