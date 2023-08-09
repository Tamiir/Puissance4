from game import *
"""
def score2(etat,humain):
    if est_terminal(etat):
        if est_gagnant(etat) == humain:
            return 42 - etat[2] #etat[2] est le nombre de coups joués
        elif coups_possibles(etat) == [] :
            return 0
        else :    
            return etat[2] - 42
    else :
        return max([score2(jouer_coup(etat,coup),humain) for coup in coups_possibles(etat)])+1
    
def score(etat,me):
    dico = dict()
    def aux(etat):
        if etat in dico:
            return dico[etat]
        else:
            res=0
            if est_terminal(etat):
                if est_gagnant(etat) == me:
                    res = 42 - etat[2] #etat[2] est le nombre de coups joués
                elif coups_possibles(etat) == [] :
                    res = 0
                else :    
                    res = etat[2] - 42
            else :
                res = max([aux(jouer_coup(etat,coup)) for coup in coups_possibles(etat)])

        dico[etat] = res
        return res
    
    return aux(etat)
"""
def score(etat,me):
    dico = dict()
    
    def aux(etat):
        (joueur,_,coups) = etat
        if me==1:
            (nbme,nbautre) = coups
        else:
            (nbautre,nbme) = coups
        if etat in dico:
            return dico[etat]
        else:
            res=0
            if est_terminal(etat):
                if coups_possibles(etat) == [] :
                    res = 0
                elif est_gagnant(etat) == me :
                    res = 22 - nbme
                else:
                    res = nbautre - 22
            else:
                if joueur == me :
                    res = max([aux(jouer_coup(etat,coup)) for coup in coups_possibles(etat)])
                else:
                    res = min([aux(jouer_coup(etat,coup)) for coup in coups_possibles(etat)])

        dico[etat] = res
        return res
    
    return aux(etat)

"""
print(score((1,((2,2,1,3,3,0,0),
                (1,1,2,3,3,0,0),
                (2,2,1,3,3,0,0),
                (1,1,2,3,3,0,0),
                (2,2,1,2,2,1,0),
                (1,1,2,1,1,1,2),), (17,16)),
                1))
"""                
"""
print(score((1,((3,3,3,0,0,0,0),
                (3,3,3,0,0,0,0),
                (3,3,3,0,0,0,0),
                (3,3,3,0,0,0,0),
                (3,3,3,3,3,3,3),
                (3,3,3,3,3,3,3),), 26),
                1))"""

#display(partie_combi("2252576253462244111563365343671351441"))
print(score(partie_combi("2252576253462244111563365343671351441"),1))
# on doit trouver -1

#display(partie_combi("7422341735647741166133573473242566"))
print(score(partie_combi('7422341735647741166133573473242566'),1))
# on doit trouver 1

#display(partie_combi("65214673556155731566316327373221417"))
print(score(partie_combi('65214673556155731566316327373221417'),1))
# on doit trouver -1