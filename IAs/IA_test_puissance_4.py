import random as rd
import Game.jeu_2048 as game
def jouer(plateau) :
    l=[]
    for j in range(6) :
        if plateau.est_vide(-1,j) :
            l.append(j)
    return(rd.choice(l))


