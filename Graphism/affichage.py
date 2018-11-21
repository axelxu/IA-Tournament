from tkinter import *
from PIL import Image
import os
root=Tk()
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
            Label(liste_cases[-1],bg="#DCFDFF",image=photo).pack(expand=YES)
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
                label.config(text = str(x))
                k+=1
    principal.update()


dir=os.getcwd()
cercle=open(dir+"\\Images\\morpion\\cercle.png")
photo=PhotoImage(file=dir+"\\Images\\morpion\\cercle.png")


