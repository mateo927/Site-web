def recherche(elt:int,tab:list[int])->int:
    """
    >>> recherche(1, [2, 3, 4]) # renvoie None
    >>> recherche(1, [10, 12, 1, 56])
    2
    >>> recherche(50, [1, 50, 1])
    1
    >>> recherche(15, [8, 9, 10, 15])
    3
    
    """
    for element in range(len(tab)):
        if tab[element]==elt:
            return element
    return 

def insere(tab, a):
    """
    >>> insere([1, 2, 4, 5], 3)
    [1, 2, 3, 4, 5]
    >>> insere([1, 2, 7, 12, 14, 25], 30)
    [1, 2, 7, 12, 14, 25, 30]
    >>> insere([2, 3, 4], 1)
    [1, 2, 3, 4]
    >>> insere([], 1)
    [1]


    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [ a ] + tab # nouveau tableau contenant a 
                        # suivi des éléments de tab
    i = 0
    while i < len(tab) and a > tab[i]: 
        tab_a[i] = tab[i] 
        tab_a[i+1] = a
        i = i + 1
    return tab_a

if __name__ == "__main__":
    import doctest
    doctest.testmod()
