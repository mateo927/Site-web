class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit

a = Noeud(1, Noeud(4, None, None),Noeud(0, None,Noeud(7, None, None)))

def taille(abr:Noeud)->int:
    '''

    >>> taille(a)
    4
    >>> taille(None)
    0
    >>> taille(Noeud(1, None, None))
    1
    
    '''
    
    if abr is None:
        return 0 
    
    elif abr.droit is None:
        return 1+taille(abr.gauche)
    
    elif abr.gauche is None:
        return 1+taille(abr.droit)
    
    return 1+taille(abr.droit)+taille(abr.gauche)

def hauteur(abr:Noeud)->int:
    ''' 
    >>> hauteur(a)
    2
    >>> hauteur(None)
    -1
    >>> hauteur(Noeud(1, None, None))
    0
    '''
    if abr is None:
        return -1
    
    elif abr.droit is None:
        return 1+hauteur(abr.gauche)
    
    elif abr.gauche is None:
        return 1+hauteur(abr.droit)
    
    return 1+max(hauteur(abr.droit),hauteur(abr.gauche))

    



def ajoute(indice, element, tab):
    '''
    >>> ajoute(1, 4, [7, 8, 9])
    [7, 4, 8, 9]
    >>> ajoute(3, 4, [7, 8, 9])
    [7, 8, 9, 4]
    >>> ajoute(0, 4, [7, 8, 9])
    [4, 7, 8, 9]

    Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab.'''
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = tab[i] 
    tab_ins[indice] = element
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = tab[i-1] 
    return tab_ins


if __name__ =="__main__":
    import doctest
    doctest.testmod()