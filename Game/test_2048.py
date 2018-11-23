from Game.jeu_2048 import *
from Core.Core import *


def grille_plateau(jeu,grille) :
    h=jeu.hauteur
    l=jeu.largeur
    plateau=Plateau(jeu)
    for i in range(h) :
        for j in range(l) :
            plateau.set_case(i,j,True,grille[i][j])
    return(plateau)


def test_move_possible():
    plateau=Plateau(Jeu_2048())
    plateau=grille_plateau(plateau.Jeu,[[2, 2, 2, 2], [4, 8, 8, 16], [0, 8, 0, 4], [4, 8, 16, 32]])
    assert plateau.est_valide("h",0)
    assert plateau.est_valide("d",0)
    assert plateau.est_valide("g",0)
    assert plateau.est_valide("b",0)
    plateau = grille_plateau(plateau.Jeu,[[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 16], [16, 8, 4, 2]])
    assert not plateau.est_valide("h",0)
    assert not plateau.est_valide("d",0)
    assert not plateau.est_valide("g",0)
    assert not plateau.est_valide("b",0)
