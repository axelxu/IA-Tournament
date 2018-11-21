class puissance_4():
    def _init_(self):
        self.largeur=7
        self.hauteur=6
        self.nb_joueurs=2

    def initialisation(self):
        pass

    def termine(self,plateau):
        return(terminaison_puissance_4(plateau))

    def est_valide(self,plateau,action):
        j, joueur= action.split()
        j= int(j)
        return(0<=j< self.largeur and plateau.surface[0][j].vide)

    def next(self,plateau,action):
        j,joueur= action.split()
        j=int(j)
        i= self.hauteur -1
        trouve=False #designe si on a trouvé une case vide dans la colonne
        while i>=0 and not trouve:
            if plateau.surface[i][j].vide:
                plateau.set_case(i,j,joueur)
                trouve= True
                plateau.surface[i][j].vide=False
            else:
                i+=1

    def message(self,n_tours, joueurs):
        print(joueurs[(n_tours) % self.nb_joueurs], ', A ton tour')

    #def terminaison_puissance_4(self,plateau):
      # termine=False
       #i=0
       #while 0<=i<=self.hauteur-5 and not termine:
           #meme_couleur= True
           #j=0
           #while meme_couleur and j<self.largeur-1:
               #if (not plateau.surface[i][j].vide) and (not plateau.surface[i][j + 1].vide) and not plateau.get_etat(i,j) == plateau.get_etat( i, j + 1):
                   #meme_couleur= False
                #j+=1
            #i+=1
           #if meme_couleur:
               termine= True
               gagnant=plateau.surface[i][0].etat

        #j=0
       #while 0<=j<=self.largeur and not termine:
           #meme_couleur= True
           #i=0
           #while meme_couleur and j<self.hauteur-1:
              #if (not plateau.surface[i][j].vide) and (not plateau.surface[i][j+1].vide):
                   #if not plateau.get_etat(i,j)==plateau.get_etat(i,j+1):
                      # meme_couleur= False
                #i+=1
            #j+=1


















