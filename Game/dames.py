import os

class Dames :
    def __init__(self):
        self.hauteur = 10
        self.largeur = 10
        self.nb_joueurs = 2


    def initialisation(self, plateau):
        """Empty the plate and set the correct configuration"""
        for i in range(self.hauteur):
            for j in range(self.largeur):
                plateau.set_case(i,j,True, 0)
        for i in range(4):
            for j in range(self.largeur):
                if (i+j)%2 :
                    plateau.set_case(i, j, False, 2)
                if (j+self.hauteur-1-i)%2:
                    plateau.set_case(self.hauteur-1-i, j, False, 1)

    def termine(self,plateau):
        """Returns True when a player has won or no more action is possible"""
        return False

    def est_valide(self, plateau, action, num_tour):
        """Returns the boolean corresponding to "is the move action acceptable in plateau with respect to the games rules" """
        dep, arr = action.split()
        id, jd = int(dep[0]), int(dep[1])
        ia, ja = int(arr[0]), int(arr[1])
        print(ia, ja, id, jd)
        dans_le_plateau = 0 <= ia < self.hauteur and 0 <= ja < self.largeur and 0 <= id < self.hauteur and 0 <= jd < self.largeur
        if not (dans_le_plateau):
            return False
        piece = plateau.get_etat(id, jd)
        if piece != num_tour%2 +1 :
            return False
        non_vide = not (plateau.est_vide(id, jd))
        arr_vide = plateau.est_vide(ia, ja)
        if not (non_vide) or not(arr_vide):
            return False
        arrivee_accessible = accessible(plateau, piece, (id, jd), (ia, ja))
        print(arrivee_accessible)
        return arrivee_accessible

    def next(self, plateau, action, num_tour):
        """Modify the plate with regard to an action"""
        dep, arr = action.split()
        id, jd = int(dep[0]), int(dep[1])
        ia, ja = int(arr[0]), int(arr[1])
        plateau.set_case(ia, ja, False, plateau.get_etat(id, jd))
        plateau.set_case(id, jd, True, 0)
        if abs(jd-ja) == 2:
            plateau.set_case((ia+id)//2, (ja+jd)//2, True, 0)

    def resultat(self, plateau):
        """Return the winner for a 2 players game"""
        return ("axel")

    def message(self, n_tour, joueurs):
        """Allows the game to communicate with user"""
        s = "Aux " + ["blancs", "noirs"][n_tour % self.nb_joueurs] + " de jouer"
        print(s)
        return s

    THEME = {} #THEME is a collection of images to display instead of numbers in the grid
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
