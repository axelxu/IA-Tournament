class Case:#on crée la classe case qu'on ajoutera dans nos matrices
    def __init__(self,coordonees,vide,etat):
        self.coordonees = coordonees
        self.vide = vide
        self.etat = etat

class plateau : #on crée la matric des cases
    def __init__(self,Jeu):
        plateau.Jeu=Jeu
        plateau.surface=[[Case((i,j),True,0) for j in range(Jeu.largeur)] for i in range(Jeu.hauteur)]

    def get_valeur(self,i,j): #chope la valeur de tel case dans le plateau
        return(plateau.surface[i][j])
    def set_case(self,i,j,vide,etat):
        plateau.surface[i][j] = Case((i,j),vide,etat)

