
class puissance_4:
    def __init__(self):
        self.largeur=7
        self.hauteur=6
        self.nb_joueurs=2
        self.THEME=THEME

    def initialisation(self,plateau):
        """Empty the plate and set the correct configuration"""
        for i in range(self.hauteur):
            for j in range(self.largeur):
                plateau.set_case(i,j,True, 0)

    def termine(self,plateau):
        """Returns True when a player has won or no more action is possible"""
        return(self.terminaison_puissance_4(plateau)[0])

    def est_valide(self,plateau,action, num_tour):
        """Returns the boolean corresponding to "is the move action acceptable in plateau with respect to the games rules" """
        try :
            j, joueur= action.split()
            j= int(j)
            return(0<=j< self.largeur and plateau.surface[0][j].vide)
        except:
            return(False)

    def next(self,plateau,action,num_tour):
        """Modify the plate with regard to an action"""
        j,joueur= action.split()
        j=int(j)
        i= self.hauteur-1
        trouve=False #designe si on a trouvé une case vide dans la colonne
        while i>=0 and not trouve:
            if plateau.surface[i][j].vide:
                plateau.set_case(i,j,True,int(joueur))
                trouve= True
                plateau.surface[i][j].vide=False
            else:
                i-=1

    def message(self,n_tours, joueurs):
        return joueurs[(n_tours) % self.nb_joueurs]+ ', A ton tour'


    def terminaison_puissance_4(self,plateau):
        termine=False
        gagnant=-1
        for i in range(1,self.hauteur):# teste l'alignement suivant une ligne
            for j in range(1,self.largeur-3):
                if not (plateau.surface[i][j].vide and plateau.surface[i][j+1].vide and plateau.surface[i][j+2].vide and plateau.surface[i][j+3].vide):
                    c=plateau.get_etat(i,j)
                    if plateau.get_etat(i,j+1)==c and plateau.get_etat(i,j+2)==c and plateau.get_etat(i,j+3)==c:
                        termine= True
                        gagnant=c
                        break
            if termine:
                break
        if not termine:
            for j in range(1,self.largeur):#teste l'alignement suivant une colonne
                for i in range(1,self.hauteur-3):
                    if not (plateau.surface[i][j].vide and plateau.surface[i+1][j].vide and plateau.surface[i+2][j].vide and plateau.surface[i+3][j].vide):
                        c=plateau.get_etat(i,j)
                        if plateau.get_etat(i+1,j)==c and plateau.get_etat(i+2,j)==c and plateau.get_etat(i+3,j)==c:
                            termine= True
                            gagnant=c
                            break
                if termine:
                    break
        elif not termine:
            for i in range(1,self.hauteur-3):#teste l'alignement suivant une diagonale
                for j in range (1,self.largeur-3):
                    c= plateau.get_etat(i,j)
                    if not(plateau.surface[i][j].vide and plateau.surface[i+1][j+1].vide and plateau.surface[i+2][j+2].vide and plateau.surface[i+3][j+3].vide):
                        if plateau.get_etat(i+1,j+1)==c and plateau.get_etat(i+2,j+2)==c and plateau.get_etat(i+3,j+3)==c:
                            termine =True
                            gagnant=c
                            break
                if termine:
                    break
        elif not termine:
            for i in range(3,self.hauteur):#teste l'alignement suivant une diagonale gauche
                for j in range(3, self.largeur):
                    c= plateau.get_etat(i,j)
                    if not (plateau.surface[i][j].vide and plateau.surface[i-1][j-1].vide and plateau.surface[i-2][j-2].vide and plateau.surface[i-3][j-3].vide):
                        if plateau.get_etat(i-1,j-1)==c and plateau.get_etat(i-2,j-2)==c and plateau.get_etat(i-3,j-3)==c:
                            termine =True
                            gagnant=c
                            break
        else:
            nombre_colonne_remplie=0
            for j in range(self.largeur):
                if not plateau.surface[0][j].vide:
                    nombre_colonne_remplie+=1
            if nombre_colonne_remplie==self.largeur:#teste si la grille est pleine
                termine=True
                gagnant= 'partie nulle'

        return(termine,gagnant)

    def resultat(self,plateau):
        return (self.terminaison_puissance_4(plateau)[1])

THEME = {0 : "/Images/puissance4/vide.gif", 1 : "/Images/puissance4/rond_jaune.gif", 2 : "/Images/puissance4/rond_rouge.gif" }















