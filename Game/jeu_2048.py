import random as rd
import copy

class Jeu_2048 :
    def __init__(self):
        self.hauteur = 4
        self.largeur = 4
        self.nb_joueurs = 1

    def initialisation(self, plateau):
        grille = init_game(4)
        grille_to_plateau(self, grille,plateau)

    def termine(self, plateau):
        grille = plateau_to_grille(self, plateau)
        return (is_game_over(grille))

    def est_valide(self,plateau,action):
        grille = plateau_to_grille(self, plateau)
        A = copy.deepcopy(grille)
        if action == "h" :
            A = move_grid_up(A)
        elif action == "b" :
            A = move_grid_down(A)
        elif action == "g" :
            A = move_grid_left(A)
        elif action == "d" :
            A = move_grid_right(A)

        if A != grille and (action in ["h", "b", "g", "d"]):
            return(True)

        else :
            return(False)


    def next(self, plateau, action, num_tour):
        grille = plateau_to_grille(self, plateau)
        if action == "h" :
            grille = move_grid_up(grille)
        elif action == "b" :
            grille = move_grid_down(grille)
        elif action == "g" :
            grille = move_grid_left(grille)
        elif action == "d" :
            grille = move_grid_right(grille)
        grille = grid_add_new_tile(grille)
        grille_to_plateau(self, grille,plateau)

    def resultat (self, plateau):
        result = 0
        for i in range (self.hauteur):
            for j in range (self.largeur):
                result += plateau.get_etat(i, j)
        return ("Ton score est :",result)

    def message(self, n_tours, joueurs):
        return "haut : h    bas : b     gauche : g      droite : d"

    THEME = {}
    THEME[0] = "/Images/2048/0.gif"
    for i in range(1, 18):
        THEME[2 ** i] = "/Images/2048/" + str(i) + ".gif"

    #Transformations

def plateau_to_grille(self,plateau):
    grille = [[plateau.get_etat(i, j) for j in range (self.hauteur) ] for i in range (self.largeur)]
    return(grille)

def grille_to_plateau(self,grille,plateau):
    for i in range (self.hauteur) :
        for j in range (self.largeur) :
            vide = grille[i][j] == 0
            plateau.set_case(i,j,vide,grille[i][j])



    #Anciennes fonctions
def create_grid(n):
    grid=[]
    for i in range (n):
        grid.append([])
        for j in range (n):
            grid[-1].append(' ')
    return grid

def grid_add_new_tile_at_position(game_grid,x,y):
    game_grid[x][y]=2
    return(game_grid)



def get_all_tiles(game_grid):
    tiles=[]
    for ligne in game_grid :
        for tile in ligne :
            if tile == ' ':
                tile = 0
            tiles.append(tile)
    return(tiles)

def get_value_new_tile():
    n=rd.randint(1,10)
    if n == 10 :
        return(4)
    else :
        return(2)

def get_empty_tiles_positions(game_grid):
    empty_tiles=[]
    for x in range (len(game_grid)):
       for y in range (len(game_grid)):
            if game_grid[x][y]==' ':
                game_grid[x][y]=0
            if game_grid[x][y]==0 :
                empty_tiles.append((x,y))
    return(empty_tiles)

def grid_get_value(grid,x,y):
    return(grid[x][y])

def get_new_position(grid):
    empty_tiles=get_empty_tiles_positions(grid)
    (x,y)=rd.choice(empty_tiles)
    return(x,y)

def grid_add_new_tile(game_grid):
    x,y=get_new_position(game_grid)

    val=get_value_new_tile()
    game_grid[x][y]=val
    return(game_grid)

def init_game(n):
    game_grid=create_grid(n)
    grid1=grid_add_new_tile(game_grid)
    grid2=grid_add_new_tile(grid1)
    return(grid2)





def move_row_left(ligne):
    n=len(ligne)
    for j in range (1,n):
        stop = 0
        colonne = j
        while stop == 0 :
            if colonne >0 and ligne[colonne-1]==ligne[colonne] :
                ligne[colonne-1] = -2*ligne[colonne]
                ligne[colonne]=0
                stop=1

            elif colonne>0 and ligne[colonne-1]==0 :
                ligne[colonne-1]=ligne[colonne]
                ligne[colonne]=0
                colonne=colonne-1
            else :
                stop=1

    for i in range (n) :
        if ligne[i]<0 :
            ligne[i]= -ligne[i]
    return(ligne)

def inversion(ligne):
    inv=[]
    n=len(ligne)
    for i in range (n):
        inv.append(ligne[n-i-1])
    return(inv)

def move_row_right(ligne):
    inverse=inversion(ligne)

    return(inversion(move_row_left(inverse)))

def transposee(grid):
    n=len(grid)
    transp=[]
    for i in range (n):
        transp.append([0]*n)
    for i in range (n):
        for j in range (n):
            transp[i][j]=grid[j][i]
    return(transp)

def move_grid_left(grid):
    for row in grid :
        row = move_row_left(row)

    return(grid)
def move_grid_right(grid):
    grid_right=[]
    for row in grid :
        row = move_row_right(row)
        grid_right.append(row)
    return(grid_right)

def move_grid_up(grid):
    transp=transposee(grid)
    transp=move_grid_left(transp)
    return(transposee(transp))

def move_grid_down(grid):
    transp=transposee(grid)

    transp=move_grid_right(transp)

    return(transposee(transp))


def move_grid(grid,direction):
    if direction == "up":
        return(move_grid_up(grid))
    if direction == "down":
        return(move_grid_down(grid))
    if direction == "right":
        return(move_grid_right(grid))
    if direction == "left":
        return(move_grid_left(grid))

def is_grid_full(grid):
    for row in grid :
        if 0 in row :
            return False
    return True

#Ordre = haut bas gauche droite
def move_possible(grille):
    moves=[True,True,True,True]
    A=copy.deepcopy(grille)
    B=copy.deepcopy(grille)
    C=copy.deepcopy(grille)
    D=copy.deepcopy(grille)
    a=move_grid_up(A)
    b=move_grid_down(B)
    c=move_grid_left(C)
    d=move_grid_right(D)
    if  a== grille :
        moves[0] = False
    if b == grille :
        moves[1] = False
    if c == grille :
        moves[2] = False
    if d == grille :
        moves[3] = False
    return(moves)

def is_game_over(grid):
    return(move_possible(grid) == [False, False, False, False])

