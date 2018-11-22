import random as rd
import Game.jeu_2048 as game
def plateau_to_grille(self,plateau):
    grille = [[plateau.get_etat(i, j) for j in range (self.hauteur) ] for i in range (self.largeur)]
    return(grille)

def play(partie) :
    mvmt = game.move_possible(plateau_to_grille(partie.plateau()))
    if mvmt[1] :
        return("b")
    elif mvmt[3] :
        return("d")
    else :
        return(rd.choice(["g","h"]))
pseudo="axel_le_bg"
