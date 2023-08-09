def init():
    return (1, ((0,0,0,0,0,0,0),
                (0,0,0,0,0,0,0),
                (0,0,0,0,0,0,0),
                (0,0,0,0,0,0,0),
                (0,0,0,0,0,0,0),
                (0,0,0,0,0,0,0),))

def coups_possibles(etat):
    grille = etat[1]
    res =[]
    for i in range(7):
        if grille[0][i] == 0 :
            res.append(i)
    return res

def est_gagnant(etat):
    grille = etat[1]

    #victoire en ligne
    for ligne in range(6):
        for j in range(3):
            if grille[ligne][j] == grille[ligne][j+1] == grille[ligne][j+2] == grille[ligne][j+3] and grille[ligne][j] != 0:
                print('victoire en ligne joueur ',grille[ligne][j])
                return grille[ligne][j]
            
    #victoire en colonne
    for colonne in range(7):
        for j in range(3):
            if grille[j][colonne] == grille[j+1][colonne] == grille[j+2][colonne] == grille[j+3][colonne] and grille[j][colonne] != 0:
                print('victoire en colonne joueur ',grille[j][colonne])
                return grille[j][colonne]
            
    #victoire en diagonal
    for ligne in range(3,6):
        for colonne in range(4):
            if grille[ligne][colonne] == grille[ligne-1][colonne+1] == grille[ligne-2][colonne+2] == grille[ligne-3][colonne+3] and grille[ligne][colonne] != 0:
                return grille[ligne][colonne]
    
    #victoire contre-diago
    for ligne in range(3):
        for colonne in range(4):
            if grille[ligne][colonne] == grille[ligne+1][colonne+1] == grille[ligne+2][colonne+2] == grille[ligne+3][colonne+3] and grille[ligne][colonne] != 0:
                return grille[ligne][colonne]

    #pas de victoire        
    return 0

def jouer_coup(etat,coup):
    (joueur,grille)=etat
    nv_joueur = 3 - joueur 
    def ligne_coup(grille,coup):
        for i in range(6):
            if grille[5-i][coup] == 0:
                return 5-i
    ligne = ligne_coup(grille,coup)
    print('LIGNE ',ligne)
    nv_grille = tuple( 
        (
        tuple ((joueur if i == ligne and j == coup else grille[i][j] for j in range(7)))
        for i in range(6)
        )
    )
    return (nv_joueur, nv_grille)