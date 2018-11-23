from Game.dames import Dames
from Core.Core import *


def test_terminaison():
    jeu = Dames()
    partie = Partie(jeu, ["a","b"])
    partie.plateau.initialisation()
    assert partie.plateau.termine() == False
    for i in range(jeu.hauteur):
        for j in range(jeu.largeur):
            partie.plateau.set_case(i,j,True,0)
    assert partie.plateau.termine() == True

def test_resultat():
    jeu = Dames()
    partie = Partie(jeu, ["a", "b"])
    partie.plateau.initialisation()
    assert partie.plateau.resultat(partie.plateau) == "axel"

def test_est_valide():
    jeu = Dames()
    partie = Partie(jeu, ["a", "b"])
    partie.plateau.initialisation()
    assert partie.plateau.est_valide("61 52", 0) == True
    assert partie.plateau.est_valide("00 11", 0) == False
    assert partie.plateau.est_valide("61 61", 0) == False
    assert partie.plateau.est_valide("30 41", 1) == True
    assert partie.plateau.est_valide("61 52", 1) == False

def text_next():
    jeu = Dames()
    partie = Partie(jeu, ["a", "b"])
    partie.plateau.initialisation()
    partie.plateau.next("61 52", 0)
    partie1 = Partie(jeu, ["a", "b"])
    partie1.plateau.initialisation()
    partie1.plateau.set_case(6,1,True,0)
    partie1.plateau.set_case(5, 2, False, 1)
    assert partie.plateau == partie1.plateau

def test_message():
    jeu = Dames()
    partie = Partie(jeu, ["a", "b"])
    partie.plateau.initialisation()
    assert partie.plateau.message(0,[]) == "Aux blancs de jouer"
    assert partie.plateau.message(1, []) == "Aux noirs de jouer"

