from Game.jeu_puissance_4 import puissance_4
from Core.Core import *

def test_terminaison():
    jeu = puissance_4()
    partie = Partie(jeu, ["a","b"])
    partie.plateau.initialisation()
    assert partie.plateau.termine() == False
    for i in range(jeu.hauteur):
        for j in range(jeu.largeur):
            partie.plateau.set_case(i,j,False,1)
    assert partie.plateau.termine() == True

def test_est_valide():
    jeu = puissance_4()
    partie = Partie(jeu, ["a", "b"])
    partie.plateau.initialisation()
    assert partie.plateau.est_valide("0 1", 0) == True
    assert partie.plateau.est_valide("100 2", 0) == False
    for i in range(jeu.hauteur):
        for j in range(jeu.largeur):
            partie.plateau.set_case(i,j,False,1)
    assert partie.plateau.est_valide("1 1", 0) == False


def test_next():
    jeu = puissance_4()
    partie = Partie(jeu, ["a", "b"])
    partie.plateau.initialisation()
    partie.plateau.next("0 1", 0)
    partie1 = Partie(jeu, ["a", "b"])
    partie1.plateau.initialisation()
    partie1.plateau.set_case(5,0,False,1)

def test_message():
    jeu = puissance_4()
    partie = Partie(jeu, ["a", "b"])
    partie.plateau.initialisation()
    assert partie.plateau.message(0,["a", "b"]) == "a, A ton tour"
    assert partie.plateau.message(1, ["a", "b"]) == "b, A ton tour"


def test_resultat():
    jeu = puissance_4()
    partie = Partie(jeu, ["a", "b"])
    partie.plateau.initialisation()
    assert partie.plateau.resultat(partie.plateau) == -1