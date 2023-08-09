from game import *
from numpy import save,load

def calculer_strategie():
    dico = dict()
    compteur = 0
    def aux(etat):
        nonlocal compteur
        if etat not in dico:
            if est_terminal(etat):
                dico[etat] = (est_gagnant(etat),None)
                return
            categories = [0, 0, 0]
            coups_prochains={0:None, 1:None, 2:None}
            for coup in coups_possibles(etat):
                etat_suivant = jouer_coup(etat, coup)
                aux(etat_suivant)
                categories[dico[etat_suivant][0]] += 1
                coups_prochains[dico[etat_suivant][0]] = coup
            if categories[etat[0]] > 0:
                dico[etat] = (etat[0], coups_prochains[etat[0]])
                compteur += 1
                print(compteur)
            elif categories[0] > 0:
                dico[etat] = (0, coups_prochains[0])
                compteur += 1
                print(compteur)
            else:
                dico[etat] = (3 - etat[0], coups_prochains[3 - etat[0]])
                compteur += 1
                print(compteur)
    aux(init()) # on commence à l'état initial
    return dico

def play(humain):
    d = calculer_strategie()
    etat = init()
    display(etat)
    while coups_possibles(etat) != [] and est_gagnant(etat) == 0:
        joueur = etat[0]
        grille = etat[1]
        if joueur == humain:
            print("Your turn.")
            while True:
                s = input("> ")
                if s not in ['0','1','2','3','4','5','6','7']:
                    print("Colonne non comprise.")
                    continue
                x = int(s)
                if grille[0][x] != 0:
                    print("Colonne pleine.")
                    continue
                coup = x
                break
        else: # joueur == 2
            coup = d[etat][1]
            assert coup != []
        print(f"Joueur {joueur} joue en {coup}")
        etat = jouer_coup(etat, coup)
        display(etat)
    print("Fin de partie")
    vainqueur = est_gagnant(etat)
    if vainqueur == 0:
        print("Match nul")
    else:
        print(f"Le vainqueur est {vainqueur}.")

# play(1) for you to start,
# play(2) for the computer to start.
#play(1)