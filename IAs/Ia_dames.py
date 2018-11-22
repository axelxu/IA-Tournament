import random as rd

def jouer(plateau, num_tour):
    """Returns a valid move in plateau"""
    joueur = num_tour%2 +1
    rdi = list(range(plateau.Jeu.hauteur))
    rd.shuffle(rdi)
    rdj = list(range(plateau.Jeu.largeur))
    rd.shuffle(rdj)
    for i in rdi:
        for j in rdj:
            for di,dj in [(-2,-2), (-2,2), (2,-2), (2,2)]:
                action = str(i)+str(j)+" "+str(s(i+di))+str(s(j+dj))
                if plateau.est_valide(action, num_tour):
                    return action

    for i in rdi:
        for j in rdj:
            for di,dj in [(-1,-1), (-1,1), (1,-1), (1,1)]:
                action = str(i)+str(j)+" "+str(s(i+di))+str(s(j+dj))
                if plateau.est_valide(action, num_tour):
                    return action

def s(x):
    return max(0,x)