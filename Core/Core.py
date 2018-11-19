class Partie :
    def __init__(self, Jeu, joueurs):
        self.joueurs = joueurs
        self.plateau = Plateau(Jeu)

    def launch(self):
        self.plateau.initialisation()
        while not(self.plateau.termine()):
            action = input()
            while not(self.plateau.valide(action)):
                action = input()
            self.plateau = self.plateau.next(action)
        print(self.plateau.resultat)


class Case:#on crée la classe case qu'on ajoutera dans nos matrices
    def __init__(self,coordonees,vide,etat):
        self.coordonees = coordonees
        self.vide = vide
        self.etat = etat

class Plateau : #on crée la matrice des cases
    def __init__(self,Jeu):
        self.Jeu=Jeu
        self.surface = [[Case((i,j),True,0) for j in range(Jeu.largeur)] for i in range(Jeu.hauteur)]
        self.termine = lambda : Jeu.termine(self.plateau)
        self.est_valide = lambda action : Jeu.est_valide(self.plateau, action)
        self.next = lambda action : Jeu.next(self.plateau, action)
        self.resultat = Jeu.resultat

    def get_etat(self,i,j): #chope la valeur de tel case dans le plateau
        return(self.surface[i][j].etat)

    def set_case(self, i, j, vide, etat):
        self.surface[i][j] = Case((i,j),vide,etat)



