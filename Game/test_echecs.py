from Game.echecs import Echec
from Core.Core import *

def test_terminaison():
    jeu = Echec()
    partie = Partie(jeu, ["a","b"])
    partie.plateau.initialisation()
    assert partie.plateau.termine() == False
    for i in range(jeu.hauteur):
        for j in range(jeu.largeur):
            partie.plateau.set_case(i,j,True,0)
    partie.plateau.set_case(0,0,False, "RN")
    partie.plateau.set_case(5, 5, False, "RB")
    partie.plateau.set_case(0, 1, False, "TB")
    partie.plateau.set_case(1, 0, False, "TB")
    partie.plateau.set_case(1, 1, False, "DB")
    assert partie.plateau.termine() == True

def test_est_valide():
    jeu = Echec()
    partie = Partie(jeu, ["a", "b"])
    partie.plateau.initialisation()
    assert partie.plateau.est_valide("60 50", 0) == True
    assert partie.plateau.est_valide("60 40", 0) == True
    assert partie.plateau.est_valide("71 50", 0) == True
    assert partie.plateau.est_valide("62 33", 0) == False
    assert partie.plateau.est_valide("10 20", 1) == True
    assert partie.plateau.est_valide("61 52", 1) == False

def test_next():
    jeu = Echec()
    partie = Partie(jeu, ["a", "b"])
    partie.plateau.initialisation()
    partie.plateau.next("60 50", 0)
    partie1 = Partie(jeu, ["a", "b"])
    partie1.plateau.initialisation()
    partie1.plateau.set_case(6,0,True,'')
    partie1.plateau.set_case(5,0,False,'PB')

def test_message():
    jeu = Echec()
    partie = Partie(jeu, ["a", "b"])
    partie.plateau.initialisation()
    assert partie.plateau.message(0,[]) == "Aux blancs de jouer"
    assert partie.plateau.message(1, []) == "Aux noirs de jouer"


def test_resultat():
    jeu = Echec()
    partie = Partie(jeu, ["a", "b"])
    partie.plateau.initialisation()
    assert partie.plateau.resultat(partie.plateau) == "Echec et mat"