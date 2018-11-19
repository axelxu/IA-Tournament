class Morpion :
    def __init__(self):
        self.hauteur = 3
        self.largeur = 3
    def initialisation(self):
        pass
    def termine(self,plateau):
        return(terminaison_morpion(plateau))
    def Est_Valide(self,plateau,action):
        i,j,joueur=action
        a,b,c=plateau[i][j]
        return(b)
    def Next(self,plateau,action):
        i,j,joueur=action
        plateau.set_case(i,j,joueur)
    def resultat(self,plateau):
        return("a()xel")

def terminaison_morpion(plateau) :
    compt = 0
    for l in plateau :
        for x in l :
            a,b,c = x
            if b :
                compt+=1
    return(compt>=3)
