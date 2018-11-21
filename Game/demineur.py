import random as rd


class Demineur :
    def __init__(self):
        self.hauteur = 20
        self.largeur = 20
    def initialisation(self, plateau):
        demineur_initialisation(plateau)
    def termine(self, plateau):
        return terminaison_demineur(plateau)
    def est_valide(self, plateau, action):
        i, j = map(int, action.split())
        return i in range(20) and j in range(20) and plateau.surface[i][j].etat == 9
    def next(self, plateau, action, num_tour):
        i, j = map(int, action.split())
        demineur_suivant(i, j, plateau)
    def resultat(self, plateau):
        return demineur_resultat(plateau)
    def message(self, a,b ):
        print("Entrer une case : i j")
        return "Entrer une case : i j"

def terminaison_demineur(plateau):
    liste_cachees = []
    liste_piegees = []

    for i in range(20):
        for j in range(20):
            Case = plateau.surface[i][j]
            if not Case.vide:
                if Case.etat in range(9):
                    return True
                liste_piegees.append(Case)
            if Case.etat == 9:
                liste_cachees.append(Case)
    return liste_cachees == liste_piegees


def decompte(i, j, plateau):
    cases_visitees = []

    def decompte_aux(i, j, plateau):
        cases_visitees.append(plateau.surface[i][j])
        nombre_mines = 0
        for k1 in [i-1, i, i+1]:
            for k2 in [j-1, j, j+1]:
                if k1 in range(20) and k2 in range (20):
                    if not plateau.surface[k1][k2].vide:
                        nombre_mines += 1
        plateau.surface[i][j].etat = nombre_mines
        if nombre_mines == 0:
            for k1 in [i-1, i, i+1]:
                for k2 in [j-1, j, j+1]:
                    if k1 in range(20) and k2 in range (20):
                        if not plateau.surface[k1][k2] in cases_visitees :
                            decompte_aux(k1, k2, plateau)
    decompte_aux(i, j, plateau)


def demineur_suivant(i, j, plateau):
    decompte(i, j, plateau)


def demineur_initialisation(plateau):
    liste_cases = [(i, j) for i in range(20) for j in range(20)]
    liste_cases.pop(0)
    liste_cases.pop(0)
    liste_cases.pop(3)
    liste_cases.pop(3)
    for i in range(20) :
        for j in range(20) :
            plateau.surface[i][j].etat = 9 #9 => la case n'est pas encore révélée

    for k in range(40):
        i, j = rd.choice(liste_cases)
        plateau.surface[i][j].vide = False
        liste_cases.pop(liste_cases.index((i, j)))


def demineur_resultat(plateau):
    for i in range(20):
        for j in range(20):
            Case = plateau.surface[i][j]
            if (Case.vide == False) and Case.etat in range(9):
                    return "Perdu"
    return "Gagné"


def construire_matrice(plateau):
    voisinages = {}
    liste_cases_connues = []
    for i in range(20):
        for j in range(20):
            if plateau.surface[i][j].etat in range(1, 9):
                liste_cases_connues.append((i, j))
    n = len(liste_cases_connues)

    liste_cases_inconnues = []
    for (i, j) in liste_cases_connues:
        liste = []
        for k1 in [i-1, i, i+1]:
            for k2 in [j-1, j, j+1]:
                if k1 in range(20) and k2 in range (20) and plateau.surface[k1][k2].etat == 9:
                    liste_cases_inconnues.append((k1,k2))
                    liste.append((k1, k2))
        voisinages[(i, j)] = liste

    set_cases = list(set(liste_cases_inconnues))
    matrix = [[0]*len(set_cases) for i in range(len(liste_cases_connues))]
    vector = [plateau.surface[i][j].etat for (i, j) in liste_cases_connues]

    for (k, (i, j)) in enumerate(liste_cases_connues):
        for case in voisinages[(i, j)] :
            matrix[k][set_cases.index(case)] = 1

    return matrix, vector







