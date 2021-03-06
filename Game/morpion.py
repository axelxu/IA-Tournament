import os

class Morpion :
    def __init__(self):
        self.hauteur = 3
        self.largeur = 3
        self.nb_joueurs = 2


    def initialisation(self, plateau):
        """Empty the plate and set the correct configuration"""
        for i in range(self.hauteur):
            for j in range(self.largeur):
                plateau.set_case(i,j,True, 0)


    def termine(self,plateau):
        """Returns True when a player has won or no more action is possible"""
        return(terminaison_morpion(plateau))


    def est_valide(self,plateau,action, num_tour):
        """Returns the boolean corresponding to "is the move action acceptable in plateau with respect to the games rules" """
        try :
            i,j = action.split()
        except :
            return False
        i, j = int(i), int(j)
        return(0<=i<self.hauteur and 0<=j<self.largeur and plateau.surface[i][j].vide)


    def next(self,plateau,action, num_tour):
        """Modify the plate with regard to an action"""
        i,j = action.split()
        i, j = int(i), int(j)
        plateau.set_case(i,j,False, 1+num_tour%self.nb_joueurs)


    def resultat(self,plateau):
        return("axel")


    def message(self, n_tour, joueurs):
        print(joueurs[n_tour%self.nb_joueurs]+ ", joues !")
        return joueurs[n_tour%self.nb_joueurs]+ ", joues !"

    THEME = {0: "/Images/morpion/empty2.gif", 1: "/Images/morpion/rond2.gif", 2: "/Images/morpion/croix3.gif"}

def terminaison_morpion(plateau) :
    for i in range(3) :
        if plateau.get_etat(i,0) == plateau.get_etat(i,1) == plateau.get_etat(i,2) and plateau.get_etat(i,0) != 0 :
            return(True)
    for i in range(3) :
        if plateau.get_etat(0,i) == plateau.get_etat(1,i) == plateau.get_etat(2,i) and plateau.get_etat(0,i) != 0 :
            return(True)
    if plateau.get_etat(0,0) == plateau.get_etat(1,1) == plateau.get_etat(2,2) and plateau.get_etat(0,0) != 0 :
        return True
    if plateau.get_etat(2,0) == plateau.get_etat(1,1) == plateau.get_etat(0,2) and plateau.get_etat(0,2) != 0 :
        return True
    for l in plateau.surface :
        for x in l :
            if x.vide :
                return False
    return True



