class Partie :
    def __init__(self, Jeu, joueurs):
        self.joueurs = joueurs
        self.plateau = Plateau(Jeu)

    def launch(self):
        num_tour = 0
        self.plateau.initialisation()
        self.plateau.afficher()
        while not(self.plateau.termine()):
            self.plateau.message(num_tour, self.joueurs)
            action = input()
            while not(self.plateau.est_valide(action)):
                print("Valide svp")
                action = input()
            self.plateau.next(action, num_tour)
            self.plateau.afficher()
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
        self.initialisation = lambda : Jeu.initialisation(self)
        self.termine = lambda : Jeu.termine(self)
        self.est_valide = lambda action : Jeu.est_valide(self, action)
        self.next = lambda action, num_tour : Jeu.next(self, action, num_tour)
        self.resultat = Jeu.resultat
        self.message = Jeu.message

    def get_etat(self,i,j): #chope la valeur de tel case dans le plateau
        return(self.surface[i][j].etat)

    def set_case(self, i, j, vide, etat):
        self.surface[i][j] = Case((i,j),vide,etat)

    def afficher(self):
        t = [[] for i in range(len(self.surface))]
        ligne = 0
        longueur_maxi = 0
        for l in self.surface :
            for x in l:
                t[ligne].append(str(x.etat))
                longueur_maxi = max(longueur_maxi, len(str(x.etat)))
            ligne+=1
        for l in t :
            print("|".join(map(lambda x : x.ljust(longueur_maxi), l)))


def jouer():
    import Game.morpion as m
    jeu = m.Morpion()
    partie = Partie(jeu, ["axel","gab"])
    partie.launch()

def jouer_demineur():
    import Game.demineur as d
    jeu = d.Demineur()
    partie = Partie(jeu, ["toi"])
    partie.launch()

def jouer_2048():
    import Game.jeu_2048 as d
    jeu = d.Jeu_2048()
    partie = Partie(jeu, ["Joueur_1"])
    partie.launch()



def jouer_Othello():
    import Game.Othello as o
    jeu = o.Othello()
    partie = Partie(jeu, ["Joueur_1","joueur 2"])
    partie.launch()

jouer_Othello()
