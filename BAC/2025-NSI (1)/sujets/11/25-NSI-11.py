

def parcours_largeur(arbre: tuple[tuple, int, tuple] | None) -> list[int]:
    '''
    >>> arbre = ( ( (None, 1, None), 2, (None, 3, None) ), 4, ( (None, 5, None), 6, (None, 7, None) ) )
    >>> parcours_largeur(arbre)
    [4, 2, 6, 1, 3, 5, 7]
    '''
    if arbre is None:
        return []
    file = [arbre]
    parcours = []
    while file:
        
        noeud = file.pop(0)
        parcours.append(noeud[1])
        
        if noeud[0] is not None:
            file.append(noeud[0])
        if noeud[2] is not None:
            file.append(noeud[2])
    return parcours


def somme_max(tab):
    '''
    >>> somme_max([1, 2, 3, 4, 5])
    15
    >>> somme_max([1, 2, -3, 4, 5])
    9
    >>> somme_max([1, 2, -2, 4, 5])
    10
    >>> somme_max([1, -2, 3, 10, -4, 7, 2, -5])
    18
    '''
    n = len(tab)
    sommes_max = [0]*n
    sommes_max[0] = tab[0]
    # on calcule la plus grande somme se terminant en i
    for i in range(1,n):
        if tab[i] + sommes_max[i-1] >= tab[i]:
            sommes_max[i] = tab[i] + sommes_max[i-1]
        else:
            sommes_max[i] = tab[i]
    # on en déduit la plus grande somme de celles-ci
    maximum = 0
    for i in range(1, n):
        if sommes_max[i] > sommes_max[maximum]  :
            maximum = i
    return sommes_max[maximum]


if __name__ == "__main__":
    import doctest
    doctest.testmod()