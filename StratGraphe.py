from game import *

def est_terminal(etat):
    return est_gagnant(etat) != 0 or coups_possibles(etat) == []

def calculer_strategie():
    dico = dict()
    def aux(etat):
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
            elif categories[0] > 0:
                dico[etat] = (0, coups_prochains[0])
            else:
                dico[etat] = (3 - etat[0], coups_prochains[3 - etat[0]])
    aux(init()) # on commence à l'état initial
    return dico
