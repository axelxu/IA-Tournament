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
            plateau.set_case(0,i,False, piece+"N")

    def termine(self,plateau):
        """Returns True when a player has won or no more action is possible"""

        return echec_et_mat(plateau, 0) or echec_et_mat(plateau, 1)


    def est_valide(self,plateau,action, num_tour):
        """Returns the boolean corresponding to "is the move action acceptable in plateau with respect to the games rules" """
        dep,arr = action.split()
        try :
            id, jd = int(dep[0]), int(dep[1])
            ia, ja = int(arr[0]), int(arr[1])
        except :
            return False
        print(ia, ja, id, jd)
        dans_le_plateau = 0<=ia<self.hauteur and 0<=ja<self.largeur and 0<=id<self.hauteur and 0<=jd<self.largeur
        if not(dans_le_plateau):
            return False
        piece = plateau.get_etat(id, jd)
        non_vide = not(plateau.est_vide(id, jd))
        if not(non_vide):
            return False
        if dep ==arr:
            return False
        if not(plateau.est_vide(ia, ja)) and plateau.get_etat(ia, ja)[1]== piece[1]:
            return False
        if piece[1]!=["B","N"][num_tour%2]:
            return False
        if not(plateau.est_vide(ia, ja)) and plateau.get_etat(ia, ja)[0]=="R":
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
        return("Echec et mat")


    def message(self, n_tour, joueurs):
        s = "Aux "+["blancs", "noirs"][n_tour%self.nb_joueurs]+" de jouer"
        print(s)
        return s
    THEME = {}
    THEME[""] = "/Images/echecs/empty.gif"
    for couleur in "NB":
        for piece in ["T", "C", "F", "R", "D", "P"]:
            THEME[piece+couleur] = "/Images/echecs/"+piece+couleur+".gif"


def case_attaquee(plateau, ia,ja,camp):
    for i in range(8):
        for j in range(8):
            if not(plateau.est_vide(i,j)) and plateau.get_etat(i,j)[0]!="R" and plateau.get_etat(i,j)[1] == camp and accessible(plateau, plateau.get_etat(i,j)[0], (i,j), (ia,ja)):
                print("debug", ia, ja, i, j)
                return True
    return False

def trouver_roi(plateau):
    pos = [(),()]
    for i in range(8):
        for j in range(8):
            if plateau.get_etat(i,j) == "RB":
                pos[0] = (i,j)
            if plateau.get_etat(i,j) == "RN":
                pos[1] = (i,j)

    return pos

def echec_et_mat(plateau, camp):
    position = trouver_roi(plateau)[camp]
    i,j = position
    dep = [(-1,-1), (-1,0), (-1, 1), (0,-1), (0,1), (1, -1), (1, 0), (1, 1)]
    for d in dep :
        di, dj = d
        if plateau.est_valide(str(i)+str(j)+" "+str(i+di)+str(j+dj),camp):
            if not(case_attaquee(plateau, i+di, j+dj, ["B", "N"][1-camp])):
                return False
    return case_attaquee(plateau, i, j, ["B", "N"][1-camp])


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
                    return all(plateau.est_vide(id-k, jd-k) for k in range(1, id-ia))
                if jd < ja :
                    return all(plateau.est_vide(id-k, jd+k) for k in range(1, id-ia))
            if id < ia:
                if jd > ja :
                    return all(plateau.est_vide(id+k, jd-k) for k in range(1, ia-id))
                if jd < ja :
                    return all(plateau.est_vide(id+k, jd+k) for k in range(1, ia-id))

    elif piece == "D":
        return accessible(plateau, "F", depart, arrivee) or accessible(plateau, "T", depart, arrivee)

    elif piece == "R":
        couleur = plateau.get_etat(id, jd)[1]
        return abs(id-ia)<=1 and abs(jd-ja)<=1 and not(case_attaquee(plateau, ia, ja, "B" if couleur == "N" else "N"))

    elif piece == "P":
        if plateau.get_etat(id, jd)[1]=="N":
            if ja == jd and ia == id+1 and plateau.est_vide(ia,ja):
                return True

            if id == 1 and plateau.est_vide(id+1, jd) and ia == id+2 and plateau.est_vide(ia,ja):
                return True

            if ja == jd-1 and ia == id+1:
                return not(plateau.est_vide(ia,ja)) and plateau.get_etat(ia, ja)[1]=="B"
            if ja == jd+1 and ia == id+1:
                return not(plateau.est_vide(ia,ja)) and plateau.get_etat(ia, ja)[1]=="B"

        if plateau.get_etat(id, jd)[1] == "B":
            if ja == jd and ia == id - 1 and plateau.est_vide(ia, ja):
                return True

            if id == 6 and plateau.est_vide(id - 1, jd) and ia == id - 2 and plateau.est_vide(ia, ja):
                return True

            if ja == jd - 1 and ia == id - 1:
                return not (plateau.est_vide(ia, ja)) and plateau.get_etat(ia, ja)[1] == "N"
            if ja == jd + 1 and ia == id - 1:
                return not (plateau.est_vide(ia, ja)) and plateau.get_etat(ia, ja)[1] == "N"

        return False