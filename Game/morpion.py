class Morpion :
    def __init__(self):
        self.hauteur = 3
        self.largeur = 3
    def initialisation(self):
        pass
    def termine(self,plateau):
        return(terminaison_morpion(plateau))
    def est_valide(self,plateau,action):
        i,j,joueur=action.split()
        i, j = int(i), int(j)
        return(0<=i<self.hauteur and 0<=j<self.largeur and plateau.surface[i][j].vide)
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