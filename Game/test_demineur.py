
from Game.demineur import *
from Core.Core import *


def test_terminaison_demineur():
    plateau = Plateau(Jeu = Demineur)
    plateau.surface = [[Case((i, j), False, 9) for i in range(20)] for j in range(20)]
    assert terminaison_demineur(plateau)

    plateau.surface[0][0].vide = True
    assert not terminaison_demineur(plateau)

    plateau.surface = [[Case((i, j), True, 0) for i in range(20)] for j in range(20)]
    plateau.surface[0][0] = Case((0, 0), False, 9)
    assert terminaison_demineur(plateau)


test_terminaison_demineur()


def test_demineur_resultat():
    plateau = Plateau(Jeu = Demineur)
    plateau.surface = [[Case((i, j), False, 9) for i in range(20)] for j in range(20)]
    assert demineur_resultat(plateau) == "Gagné"

    plateau.surface = [[Case((i, j), True, 0) for i in range(20)] for j in range(20)]
    plateau.surface[0][0] = Case((0, 0), False, 9)
    assert demineur_resultat(plateau) == "Gagné"

    plateau.surface[0][0].etat = 0
    assert not demineur_resultat(plateau) == "Gagné"


def test_decompte():
    plateau = Plateau(Jeu = Demineur)
    plateau.surface = [[Case((i, j), True, 9) for i in range(20)] for j in range(20)]
    decompte(0, 0, plateau)
    assert plateau.surface[0][0].etat == 0
    assert plateau.surface[19][19].etat == 0

    plateau.surface = [[Case((i, j), True, 9) for i in range(20)] for j in range(20)]
    plateau.surface[1][0].vide = False
    decompte(0, 0, plateau)
    assert plateau.surface[0][0].etat == 1


def test_demineur_initialisation():
    plateau = Plateau(Jeu = Demineur)
    demineur_initialisation(plateau)
    assert all([plateau.surface[i][j].vide for i in range(2) for j in range(2)])
    assert plateau.Jeu.largeur == plateau.Jeu.longueur == 20
    assert len([plateau.surface[i][j] for i in range(20) for j in range(20) if not plateau.surface[i][j].vide]) == 40


def test_construire_matrice():
    plateau = Plateau(Jeu = Demineur)
    plateau.surface = [[Case((i, j), True, 9) for i in range(20)] for j in range(20)]
    plateau.surface[0][0].etat = 1
    plateau.surface[1][0].etat = 1
    m, v, s = construire_matrice(plateau)
    assert len(m) == 2 and len(m[0]) == 4 and v == [1, 1]


def test_arg_max():
    t = [1,2,3]
    assert arg_max(t) == 2


def test_pivot_gauss():
    m = [[1, 1], [1, 1]]
    v = [1, 1]
    assert pivot_gauss(m, v) == [[0, 0.0], [1, 1]], [0.0, 1]


def test_choix_case_ia():
    plateau = Plateau(Jeu = Demineur)
    plateau.surface = [[Case((i, j), True, 0) for i in range(20)] for j in range(20)]

    plateau.surface[2][0].etat = 1
    for i in range(2):
        plateau.surface[i][1].etat = 9
        plateau.surface[i][0].etat = 1

    assert choix_case_ia(plateau) == (0, 1)


