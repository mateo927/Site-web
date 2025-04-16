from re import A


def couples_consecutifs(tab:list[int])->list[tuple[int]]:
    '''
    >>> couples_consecutifs([1, 4, 3, 5])
    []
    >>> couples_consecutifs([1, 4, 5, 3])
    [(4, 5)]
    >>> couples_consecutifs([1, 1, 2, 4])
    [(1, 2)]
    >>> couples_consecutifs([7, 1, 2, 5, 3, 4])
    [(1, 2), (3, 4)]
    >>> couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7])
    [(1, 2), (2, 3), (-5, -4)]
    
    '''
    
    liste_sortie=[]
    for ele in range (len(tab)):
        if tab[ele]-1==tab[ele-1]:
            liste_sortie.append((tab[ele-1],tab[ele]))
    return liste_sortie


def colore_comp1(M, i, j, val):
    '''
    >>> M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
    >>> colore_comp1(M, 2, 1, 3)
    >>> M
    [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]
    
    '''
    if M[i][j] != 1:
        return

    M[i][j] = val

    if i-1 >= 0: # propage en haut
        colore_comp1(M, i-1, j, val)
    if i+1 < len(M): # propage en bas 
        colore_comp1(M, i+1, j, val) 
    if j-1 >= 0: # propage à gauche 
        colore_comp1(M, i, j-1, val)
    if j+1 < len(M[0]) : # propage à droite 
        colore_comp1(M, i, j+1, val)

if __name__ == "__main__":
    import doctest 
    doctest.testmod()

