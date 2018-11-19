class Morpion : #Jeu test pour voir si ca maarche (pas vraiment un morpion)
    def __init__(self,nb_joueurs):
        self.hauteur = 3
        self.largeur = 3
        self.nb_joueurs = nb_joueurs
    def initialisation(self):
        pass
    def termine(self,plateau):
        return(terminaison_morpion(plateau))
    def est_valide(self,plateau,action):
        i,j,joueur=action.split()
        i, j = int(i), int(j)
        return(plateau.surface[i][j].vide)
    def next(self,plateau,action):
        i,j,joueur=action.split()
        i, j = int(i), int(j)
        plateau.set_case(i,j,False,joueur)
    def resultat(self,plateau):
        return("axel")

def terminaison_morpion(plateau) :
    compt = 0
    for l in plateau.surface :
        for x in l :
            if not(x.vide) :
                compt+=1
    return(compt>=3)
