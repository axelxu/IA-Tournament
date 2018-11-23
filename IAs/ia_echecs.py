import random as rd

def jouer(plateau, num_tour):
    """Returns a valid move in plateau"""
    rdi1 = list(range(plateau.Jeu.hauteur))
    rd.shuffle(rdi1)
    rdi2 = list(range(plateau.Jeu.hauteur))
    rd.shuffle(rdi2)
    rdj1 = list(range(plateau.Jeu.largeur))
    rd.shuffle(rdj1)
    rdj2 = list(range(plateau.Jeu.largeur))
    rd.shuffle(rdj2)
    for i1 in rdi1:
        for j1 in rdj1:
            for i2 in rdi2:
                for j2 in rdj2:
                    action = str(i1) + str(j1) + " " + str(i2) + str(j2)
                    if plateau.est_valide(action, num_tour):
                        return action
