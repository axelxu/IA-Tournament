import random as rd
import Game.jeu_2048 as game
def jouer(plateau, num_tour) :
    l=[]
    for j in range(7) :
        if plateau.est_vide(0,j) :
            l.append(j)
    return(str(rd.choice(l))+" "+str(num_tour%2+1))


