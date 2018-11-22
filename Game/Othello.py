import copy

class Othello :
    def __init__(self):
        self.hauteur = 8
        self.largeur = 8
        self.nb_joueurs = 2


    def initialisation (self,plateau):
        """Empty the plate and set the correct configuration"""
        plateau.set_case(4,4,False, 1)
        plateau.set_case(3,3,False, 1)
        plateau.set_case(3,4,False, 2)
        plateau.set_case(4,3,False, 2)

    def termine(self, plateau):
        """Returns True when a player has won or no more action is possible"""
        if len(get_empty_tiles_positions(self,plateau)) == 0 :
            return (True)
        else :
            return (False)

    def next(self, plateau, action, num_tour):
        """Modify the plate with regard to an action"""
        i,j = action.split()
        i, j = int(i), int(j)
        plateau.set_case(i,j,False, 1+num_tour%self.nb_joueurs)
        grille = plateau_to_grille(plateau)
        conversion_haut(i,j,grille)
        conversion_bas(i,j,grille)
        conversion_droite(i,j,grille)
        conversion_gauche(i,j,grille)
        grille_to_plateau(grille, plateau)

    def est_valide(self,plateau,action,num_tour):
        i,j = action.split()
        i, j = int(i), int(j) #on commence à 0
        print(plateau.surface[i][j].vide)
        if not (0<=i<self.hauteur and 0<=j<self.largeur and plateau.surface[i][j].vide) :
           print("invalide direct")
           return(False)

        plateau.set_case(i,j,False, 1+num_tour%self.nb_joueurs)
        grille = plateau_to_grille(self,plateau)
        A = copy.deepcopy (grille)
        conversion_haut(i,j,A)
        conversion_bas(i,j,A)
        conversion_droite(i,j,A)
        conversion_gauche(i,j,A)
        print("valide : ",not (A == grille))
        return(not (A == grille))


    def message(self, n_tour, joueurs):
        print(joueurs[n_tour%self.nb_joueurs]+ ", joues !")
        return joueurs[n_tour%self.nb_joueurs]+ ", joues !"

    def resultat(self,plateau):
        j1 = 0
        for i in range (self.hauteur) :
            for j in range (self.largeur) :
                if int(plateau.get_etat(self,i,j)) == 1 :
                    j1 += 1
        if j1 > 32 :
            print("J1 a gagné")
        else :
            print("J2 a gagné" )

def plateau_to_grille(self,plateau):
    grille = [[plateau.get_etat(i, j) for j in range (self.hauteur) ] for i in range (self.largeur)]
    return(grille)

def grille_to_plateau(self,grille,plateau):
    for i in range (self.hauteur) :
        for j in range (self.largeur) :
            vide = grille[i][j] == 0
            plateau.set_case(i,j,vide,grille[i][j])

def get_empty_tiles_positions(self,plateau):
    empty_tiles=[]

    for i in range (self.hauteur):
       for j in range (self.largeur):
            if plateau.surface[i][j].vide :
                empty_tiles.append((i,j))
    return(empty_tiles)

#def etoile_grille(grid,ligne,colonne):
#   n = len(grid)
#    right = grid[ligne][colonne:]
#    left = grid[ligne][:colonne + 1]
#    up, down = [],[]
#    for i in range (n):
#        if i <= ligne :
#            up.append(grid[i][colonne])
#        if i >= ligne :
#            down.append(grid[i][colonne])


#   return(left, right, up, down)

#def inversion(ligne):
#    inv=[]
#    n=len(ligne)
#    for i in range (n):
#        inv.append(ligne[n-i-1])
#    return(inv)

#def inversion_grille (grid):
#    inv=[]
#    for row in grid :
#        inv.append(inversion(row))
#    return(inv)

def transposee(grid):
    n=len(grid)
    transp=[]
    for i in range (n):
        transp.append([0]*n)
    for i in range (n):
        for j in range (n):
            transp[i][j]=grid[j][i]
    return(transp)

def conversion_haut (i,j,grille):
    ligne = i
    joueur = grille[i][j]
    t=[2,1]
    adversaire = t[joueur-1]
    print(ligne > 0 and grille[ligne-1][j] == adversaire)
    while ligne > 0 and grille[ligne-1][j] == adversaire :
        ligne = ligne - 1
    if ligne > 0 and grille[ligne-1][j] == joueur :
        for l in range (ligne, i):
            grille[l][j] = joueur

    return(grille)

def conversion_bas (i,j,grille):
    ligne = i
    joueur = grille[i][j]
    t=[2,1]
    adversaire = t[joueur-1]
    while ligne < len(grille) and grille[ligne+1][j] == adversaire :
        ligne = ligne + 1

    if ligne < len(grille) and grille[ligne+1][j] == joueur :
        for l in range (ligne, i):
            grille[l][j]==joueur
    return(grille)

def conversion_gauche (i,j,grille):
    tr = transposee(grille)
    conv = conversion_haut(j,i,tr)
    return(conv)

def conversion_droite (i,j,grille):
    tr = transposee(grille)
    conv = conversion_bas(j,i,tr)
    return(conv)


grille = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,2,0,0,0],[0,0,0,2,1,0,0,0],[0,0,0,0,2,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

print(grille)
print(conversion_haut(5,4,grille))

