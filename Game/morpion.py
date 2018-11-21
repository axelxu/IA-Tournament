class Morpion :
    def __init__(self):
        self.hauteur = 3
        self.largeur = 3
        self.nb_joueurs = 2

    def initialisation(self, plateau):
        pass


    def termine(self,plateau):
        return(terminaison_morpion(plateau))


    def est_valide(self,plateau,action):
        i,j = action.split()
        i, j = int(i), int(j)
        return(0<=i<self.hauteur and 0<=j<self.largeur and plateau.surface[i][j].vide)


    def next(self,plateau,action, num_tour):
        i,j = action.split()
        i, j = int(i), int(j)
        plateau.set_case(i,j,False, 1+num_tour%self.nb_joueurs)


    def resultat(self,plateau):
        return("axel")


    def message(self, n_tour, joueurs):
        print(joueurs[n_tour%self.nb_joueurs], ", joues !")


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



