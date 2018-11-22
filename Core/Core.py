class Partie :
    """Contains a suppelementary level of meta-information about the game"""
    def __init__(self, Jeu, joueurs):
        self.joueurs = joueurs
        self.plateau = Plateau(Jeu)

    def launch(self):
        """Initialize and allows user to run a game in Console"""
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


class Case:
    """Basic component of plate"""
    def __init__(self,coordonees,vide,etat):
        self.coordonees = coordonees
        self.vide = vide
        self.etat = etat

class Plateau :
    """Basically containing a matrix of tiles plus the current function of the game"""
    def __init__(self,Jeu):
        self.Jeu=Jeu
        self.surface = [[Case((i,j),True,0) for j in range(Jeu.largeur)] for i in range(Jeu.hauteur)]
        self.initialisation = lambda : Jeu.initialisation(self)
        self.termine = lambda : Jeu.termine(self)
        self.est_valide = lambda action, num_tour : Jeu.est_valide(self, action, num_tour)
        self.next = lambda action, num_tour : Jeu.next(self, action, num_tour)
        self.resultat = Jeu.resultat
        self.message = Jeu.message

    def get_etat(self,i,j):
        """Returns the value of the attribute etat of the tile (i,j) of Plateau"""
        return(self.surface[i][j].etat)

    def set_case(self, i, j, vide, etat):
        """Set the value of the attribute etat of the tile (i,j) of Plateau at etat"""
        self.surface[i][j] = Case((i,j),vide,etat)

    def est_vide(self,i,j):
        """Returns True if the tile (i,j) is empty, else False"""
        return self.surface[i][j].vide

    def afficher(self):
        """Prints in console a fancy plate"""
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
    """Short function to quick lauch a game"""
    import Game.morpion as m
    jeu = m.Morpion()
    partie = Partie(jeu, ["axel","gab"])
    partie.launch()

def jouer_demineur():
    """Short function to quick lauch a game"""
    import Game.demineur as d
    jeu = d.Demineur()
    partie = Partie(jeu, ["toi"])
    partie.launch()

def jouer_2048():
    """Short function to quick lauch a game"""
    import Game.jeu_2048 as d
    jeu = d.Jeu_2048()
    partie = Partie(jeu, ["Joueur_1"])
    partie.launch()

def jouer_Othello():
    """Short function to quick lauch a game"""
    import Game.Othello as o
    jeu = o.Othello()
    partie = Partie(jeu, ["Joueur_1","Joueur_2"])
    partie.launch()
