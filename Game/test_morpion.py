from Game.morpion import *
from Core.Core import *

def test_terminaison_morpion() :
    plateau=Plateau(Morpion())
    for i in range(3) :
        plateau.surface = [[Case((i,j),True,0)for i in range(3)]for j in range(3)]
        for j in range(3) :
            plateau.set_case(i,j,False,1)
        assert terminaison_morpion(plateau)
        for j in range(3) :
            plateau.set_case(j,i,False,1)
        assert terminaison_morpion(plateau)
    plateau.surface = [[Case((i,j),True,0)for i in range(3)]for j in range(3)]
    for i in range(3) :
         plateau.set_case(i,i,False,1)
    assert terminaison_morpion(plateau)
    plateau.surface = [[Case((i,j),True,0)for i in range(3)]for j in range(3)]
    for i in range(3) :
         plateau.set_case(i,2-i,False,1)
    assert terminaison_morpion(plateau)
    plateau.surface = [[Case((i,j),True,0)for i in range(3)]for j in range(3)]
    assert not terminaison_morpion(plateau)

