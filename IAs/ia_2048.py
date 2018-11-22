import random as rd
import Game.jeu_2048 as game

def jouer(plateau, num_tour) :
    mvmt = plateau.est_valide()
    for action in ["b","d","g","h"]:
        if plateau.est_valide(action) :
            return action

