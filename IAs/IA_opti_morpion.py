import random as rd

def jouer(plateau, n):
    """Returns a valid move in plateau"""
    choix = jouer_partiel(plateau)
    return str(choix[0])+" "+str(choix[1])

def jouer_partiel(plateau) :
    l=[]
    for i in range(3) :
        for j in range(3) :
            l.append(plateau.est_vide(i,j))
    if all(l) :
        return(0,0)
    test=0
    for i in range(3) :
        for j in range(3) :
            if not plateau.est_vide(i,j) :
                test+=1
    if test == 2 :
        ennemi=[]
        for i in range(3) :
            for j in range(3) :
                if (i,j) != (0,0) and not plateau.est_vide(i,j) :
                    ennemi=[i,j]
        if ennemi[0] == 0 :
            return(2,0)
        else :
            return(0,2)
    if test == 4 :
        if plateau.get_etat(0,0) == plateau.get_etat(0,2) and plateau.est_vide(0,1) :
            return(0,1)
        elif plateau.get_etat(0,0) == plateau.get_etat(2,0) and plateau.est_vide(1,0) :
            return(1,0)
        elif plateau.get_etat(0,0) == plateau.get_etat(0,2) and plateau.est_vide(1,0) :
            return(2,0)
        elif plateau.get_etat(0,0) == plateau.get_etat(0,2) and plateau.est_vide(1,2) :
            return(2,2)
        elif plateau.get_etat(0,0) == plateau.get_etat(2,0) and plateau.est_vide(0,1) :
            return(0,2)
        elif plateau.get_etat(0,0) == plateau.get_etat(2,0) and plateau.est_vide(2,1) :
            return(2,2)
    if test == 6 :
        if plateau.get_etat(0,0) == plateau.get_etat(0,2) == plateau.get_etat(2,2) and plateau.est_vide(1,1) :
            return(1,1)
        elif plateau.get_etat(0,0) == plateau.get_etat(0,2) == plateau.get_etat(2,2) and plateau.est_vide(1,2) :
            return(1,2)
        elif plateau.get_etat(0,0) == plateau.get_etat(0,2) == plateau.get_etat(2,0) and plateau.est_vide(1,1) :
            return(1,1)
        elif plateau.get_etat(0,0) == plateau.get_etat(0,2) == plateau.get_etat(2,0) and plateau.est_vide(1,0) :
            return(1,0)
        elif plateau.get_etat(0,0) == plateau.get_etat(2,0) == plateau.get_etat(2,2) and plateau.est_vide(1,1) :
            return(1,1)
        elif plateau.get_etat(0,0) == plateau.get_etat(2,0) == plateau.get_etat(2,2) and plateau.est_vide(2,1) :
            return(2,1)
        elif plateau.get_etat(0,0) == plateau.get_etat(0,2) == plateau.get_etat(2,0) and plateau.est_vide(0,1) :
            return(0,1)
    else :
        l=[]
        for i in range(3) :
            for j in range(3) :
                if plateau.est_vide(i,j) :
                    l.append((i,j))
        return(rd.choice(l))
