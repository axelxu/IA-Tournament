def construire_matrice(plateau):
    """Met le problème sous forme matricielle."""
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
                    liste_cases_inconnues.append((k1, k2))
                    liste.append((k1, k2))
        voisinages[(i, j)] = liste

    set_cases = list(set(liste_cases_inconnues))
    matrix = [[0]*len(set_cases) for i in range(n)]
    vector = [plateau.surface[i][j].etat for (i, j) in liste_cases_connues]

    for (k, (i, j)) in enumerate(liste_cases_connues):
        for case in voisinages[(i, j)] :
            matrix[k][set_cases.index(case)] = 1

    return matrix, vector, set_cases


def arg_max(t):
    """Retourne l'indice du maximum de t."""
    m = max(t)
    for i in range(len(t)):
        if t[i] == m:
            return i


def pivot_gauss(matrix, vector):
    """Applique la méthode du pivot de Gauss au système matrix, vector."""
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
    """Retourne une case choisie par l'ia."""
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
