import random as rd


class Demineur :
    def __init__(self):
        self.hauteur = 20
        self.largeur = 20
        self.nb_joueurs = 1


    def initialisation(self, plateau):
        """Empty the plate and set the correct configuration"""
        demineur_initialisation(plateau)


    def termine(self, plateau):
        """Returns True when a player has won or no more action is possible"""
        return terminaison_demineur(plateau)


    def est_valide(self, plateau, action, num_tour):
        """Returns the boolean corresponding to "is the move action acceptable in plateau with respect to the games rules" """
        i, j = map(int, action.split())
        return i in range(20) and j in range(20) and plateau.surface[i][j].etat == 9

    def next(self, plateau, action, num_tour):
        """Modify the plate with regard to an action"""
        i, j = map(int, action.split())
        demineur_suivant(i, j, plateau)

    def resultat(self, plateau):
        return demineur_resultat(plateau)


    def message(self, a,b ):
        print("Entrer une case : i j")
        return "Entrer une case : i j"

    THEME = {0 : "/Images/demineur/devoilee_vide.gif",
             1 : "/Images/demineur/un.gif",
             2 : "/Images/demineur/deux.gif",
             3 : "/Images/demineur/trois.gif",
             4 : "/Images/demineur/quatre.gif",
             5 : "/Images/demineur/cinq.gif",
             6 : "/Images/demineur/six.gif",
             7 : "/Images/demineur/sept.gif",
             8 : "/Images/demineur/huit.gif",
             9 : "/Images/demineur/inconnue.gif"}

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
    for i in range(20):
        for j in range(20):
            plateau.set_case(i, j, True, 0)

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

    return matrix, vector, set_cases


def arg_max(t):
    m = max(t)
    for i in range(len(t)):
        if t[i] == m:
            return i


def pivot_gauss(matrix, vector):
    m = matrix
    v = vector
    n = len(m)
    p = len(m[0])

    h = 0
    k = 0

    while h <= n-1 and k <= p-1:
        i_max = arg_max([m[i][k] for i in range(h, n)])
        if m[i_max][k] == 0:
            k += 1
        else:
            m[h], m[i_max] = m[i_max], m[h]
            v[h], v[i_max] = v[i_max], v[h]
            for i in range(h+1, n):
                f = m[i][k]/m[h][k]
                m[i][k] = 0
                for j in range(k+1, p):
                    m[i][j] = m[i][j] - m[h][j] * f
                v[i] = v[i] - v[h] * f
            h += 1
            k += 1

    return m, v


def choix_case_ia(plateau):
    liste_mines = []
    matrix, vector, set_cases = construire_matrice(plateau)
    m, v = pivot_gauss(matrix, vector)
    n, p = len(m), len (m[0])
    liste_proba = [0]*p
    plateau_init = [[9]*20]*20
    
    if [[plateau.surface[i][j].etat for i in range(20)] for j in range(20)] == plateau_init:
        return (0, 0)
    
    for k in range(n):
        s = sum(m[k])
        if s == v[k]:
            for q in range(p):
                if m[k][q] == 1 and not set_cases[q] in liste_mines:
                    liste_mines.append(set_cases[q])
                    liste_proba[q] = 1
        else:
            upper_bound = sum([1 for x in m[k] if x == 1])
            lower_bound = sum([-1 for x in m[k] if x == -1])

            if not s in [upper_bound, lower_bound]:
                for q in range(p):
                    liste_proba[q] += m[k][q] * v[k] / s

            elif s == upper_bound:
                for q in range(p):
                    if m[k][q] == 1 and not set_cases[q] in liste_mines:
                        liste_mines.append(set_cases[q])
                        liste_proba[q] = 1
                    if m[k][q] == -1:
                        liste_proba[q] = 0

            elif s == lower_bound:
                for q in range(p):
                    if m[k][q] == -1 and not set_cases[q] in liste_mines:
                        liste_mines.append(set_cases[q])
                        liste_proba[q] = 1
                    if m[k][q] == 1:
                        liste_proba[q] = 0

    l = [x for x in liste_proba if x != 1]
    
    if len(l) == 0:
        return rd.choice(set_cases)
    else:
        return set_cases[liste_proba.index(min(l))]
