import os

class Dames :
    def __init__(self):
        self.hauteur = 10
        self.largeur = 10
        self.nb_joueurs = 2


    def initialisation(self, plateau):
        for i in range(4):
            for j in range(self.largeur):
                if (i+j)%2 :
                    plateau.set_case(i, j, False, 2)
                if (j+self.hauteur-1-i)%2:
                    plateau.set_case(self.hauteur-1-i, j, False, 1)

    def termine(self,plateau):
        return False

    def est_valide(self, plateau, action, num_tour):
        dep, arr = action.split()
        id, jd = int(dep[0]), int(dep[1])
        ia, ja = int(arr[0]), int(arr[1])
        print(ia, ja, id, jd)
        dans_le_plateau = 0 <= ia < self.hauteur and 0 <= ja < self.largeur and 0 <= id < self.hauteur and 0 <= jd < self.largeur
        if not (dans_le_plateau):
            return False
        piece = plateau.get_etat(id, jd)
        non_vide = not (plateau.est_vide(id, jd))
        if not (non_vide):
            return False
        arrivee_accessible = accessible(plateau, piece, (id, jd), (ia, ja))
        print(arrivee_accessible)
        return arrivee_accessible

    def next(self, plateau, action, num_tour):
        dep, arr = action.split()
        id, jd = int(dep[0]), int(dep[1])
        ia, ja = int(arr[0]), int(arr[1])
        plateau.set_case(ia, ja, False, plateau.get_etat(id, jd))
        plateau.set_case(id, jd, True, 0)
        if abs(jd-ja) == 2:
            plateau.set_case((ia+id)//2, (ja+jd)//2, True, 0)

    def resultat(self, plateau):
        return ("axel")

    def message(self, n_tour, joueurs):
        s = "Aux " + ["blancs", "noirs"][n_tour % self.nb_joueurs] + " de jouer"
        print(s)
        return s

    THEME = {}
    for i in range(3):
            THEME[i] = "/Images/dames/" + str(i) + ".gif"

    def terminaison_morpion(plateau):
        return False

def accessible(plateau, piece, depart, arrivee):

    id, jd = depart
    ia, ja = arrivee
    if piece == 1 : #blanc
        if abs(ja-jd) == 1:
            return id-ia == 1
        elif abs(ja-jd) == 2:
            if id - ia == 2:
                return plateau.get_etat((ia+id)//2, (ja+jd)//2)==2

    if piece == 2 : #noir
        if abs(ja-jd) == 1:
            return id-ia == -1
        elif abs(ja-jd) == 2:
            if id - ia == -2:
                return plateau.get_etat((ia+id)//2, (ja+jd)//2)==1
    return False