# coding: utf8
from Game.demineur import *
from Core.Core import *
import pytest

def test_terminaison_demineur():
    plateau = Plateau()
    plateau.surface = [[Case((i, j), False, 9) for i in range(20)] for j in range(20)]
    assert terminaison_demineur(plateau)

    plateau.surface[0][0].vide = True
    assert not terminaison_demineur(plateau)

    plateau.surface = [[Case((i, j), True, 0) for i in range(20)] for j in range(20)]
    plateau.surface[0][0] = Case((0, 0), False, 9)
    assert terminaison_demineur(plateau)


def test_demineur_resultat():
    plateau = Plateau()
    plateau.surface = [[Case((i, j), False, 9) for i in range(20)] for j in range(20)]
    assert terminaison_demineur(plateau) == "Gagné"

    plateau.surface = [[Case((i, j), True, 0) for i in range(20)] for j in range(20)]
    plateau.surface[0][0] = Case((0, 0), False, 9)
    assert terminaison_demineur(plateau) == "Gagné"

    plateau.surface[0][0].etat = 0
    assert not terminaison_demineur(plateau) == "Gagné"


def test_decompte():
    1


