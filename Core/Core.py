class Partie :
    def __init__(self, Jeu, joueurs):
        self.joueurs = joueurs
        self.plateau = Plateau(Jeu)

    def launch(self):
        num_tour = 0
        self.plateau.initialisation()
        while not(self.plateau.termine()):
            self.plateau.message(num_tour, self.joueurs)
            action = input()
            while not(self.plateau.est_valide(action)):
                print("Valide svp")
                action = input()
            self.plateau.next(action, num_tour)
            num_tour += 1
        print(self.plateau.resultat(self.plateau))


class Case:#on crée la classe case qu'on ajoutera dans nos matrices
    def __init__(self,coordonees,vide,etat):
        self.coordonees = coordonees
        self.vide = vide
        self.etat = etat

class Plateau : #on crée la matrice des cases
    def __init__(self,Jeu):
        self.Jeu=Jeu
        self.surface = [[Case((i,j),True,0) for j in range(Jeu.largeur)] for i in range(Jeu.hauteur)]
        self.initialisation = Jeu.initialisation
        self.termine = lambda : Jeu.termine(self)
        self.est_valide = lambda action : Jeu.est_valide(self, action)
        self.next = lambda action, num_tour : Jeu.next(self, action, num_tour)
        self.resultat = Jeu.resultat
        self.message = Jeu.message

    def get_etat(self,i,j): #chope la valeur de tel case dans le plateau
        return(self.surface[i][j].etat)

    def set_case(self, i, j, vide, etat):
        self.surface[i][j] = Case((i,j),vide,etat)


def jouer():
    import Game.morpion as m
    jeu = m.Morpion()
    partie = Partie(jeu, ["axel","gab"])
    partie.launch()
