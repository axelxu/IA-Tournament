import os

class Echec :
    def __init__(self):
        self.hauteur = 8
        self.largeur = 8
        self.nb_joueurs = 2


    def initialisation(self, plateau):
        """Empty the plate and set the correct configuration"""
        for i in range(8):
            for j in range(8):
                plateau.set_case(i, j, True, "")
        for i, piece in enumerate(["T", "C", "F", "D", "R", "F", "C", "T"]):
            plateau.set_case(7,i, False, piece+"B")
            plateau.set_case(6, i, False, "PB")
            plateau.set_case(1, i, False, "PN")
        for i, piece in enumerate(["T", "C", "F", "R", "D", "F", "C", "T"]):
            plateau.set_case(0,i,False, piece+"N")

    def termine(self,plateau):
        """Returns True when a player has won or no more action is possible"""
        return(terminaison_morpion(plateau))


    def est_valide(self,plateau,action, num_tour):
        """Returns the boolean corresponding to "is the move action acceptable in plateau with respect to the games rules" """
        dep,arr = action.split()
        id, jd = int(dep[0]), int(dep[1])
        ia, ja = int(arr[0]), int(arr[1])
        print(ia, ja, id, jd)
        dans_le_plateau = 0<=ia<self.hauteur and 0<=ja<self.largeur and 0<=id<self.hauteur and 0<=jd<self.largeur
        if not(dans_le_plateau):
            return False
        piece = plateau.get_etat(id, jd)
        non_vide = not(plateau.est_vide(id, jd))
        if not(non_vide):
            return False
        arrivee_accessible = accessible(plateau,piece[0], (id, jd), (ia, ja))
        print(arrivee_accessible)
        return arrivee_accessible


    def next(self,plateau,action, num_tour):
        """Modify the plate with regard to an action"""
        dep,arr = action.split()
        id, jd = int(dep[0]), int(dep[1])
        ia, ja = int(arr[0]), int(arr[1])
        plateau.set_case(ia, ja, False, plateau.get_etat(id, jd))
        plateau.set_case(id,jd,True, "")



    def resultat(self,plateau):
        return("axel")


    def message(self, n_tour, joueurs):
        s = "Aux "+["blancs", "noirs"][n_tour%self.nb_joueurs]+" de jouer"
        print(s)
        return s
    THEME = {}
    THEME[""] = "/Images/echecs/empty.gif"
    for couleur in "NB":
        for piece in ["T", "C", "F", "R", "D", "P"]:
            THEME[piece+couleur] = "/Images/echecs/"+piece+couleur+".gif"
def terminaison_morpion(plateau) :
    return False


def accessible(plateau,piece, depart, arrivee):

    id, jd = depart
    ia, ja = arrivee
    print(piece)
    if piece == "C":
        return (id-ia, jd-ja) in [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

    elif piece == "T":
        if id == ia :
            if ja < jd :
                return all(plateau.est_vide(ia, j) for j in range(ja+1, jd))
            else :
                return all(plateau.est_vide(ia, j) for j in range(jd+1, ja))
        elif ja == jd :
            if ia < id :
                return all(plateau.est_vide(i, ja) for i in range(ia+1, id))
            else :
                return all(plateau.est_vide(i, jd) for i in range(id+1, ia))
        return False

    elif piece == "F":
        if abs(id-ia) == abs(jd - ja):
            if id > ia:
                if jd > ja :
                    return all(plateau.est_vide(id+k, jd+k) for k in range(1, ia-id))
                if jd < ja :
                    return all(plateau.est_vide(id+k, jd-k) for k in range(1, ia-id))
            if id < ia:
                if jd > ja :
                    return all(plateau.est_vide(id-k, jd+k) for k in range(1, id-ia))
                if jd < ja :
                    return all(plateau.est_vide(id-k, jd-k) for k in range(1, id-ia))

    elif piece == "D":
        return accessible(plateau, "F", depart, arrivee) or accessible(plateau, "T", depart, arrivee)

    elif piece == "R":
        return abs(id-ia)<=1 and abs(jd-ja)<=1

    elif piece == "P":
        #couleur = plateau.get_etat(id, jd)
        return True