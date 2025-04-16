def multiplication (n1:int,n2:int)->int:
    """
    >>> multiplication(3, 5)
    15
    >>> multiplication(-4, -8)
    32
    >>> multiplication(-2, 6)
    -12
    >>> multiplication(-2, 0)
    0
    
    """
    if n1==0 :
        return 0
    elif n2==0:
        return 0
    
    elif n1<0 and n2<0:
        n1=-n1
        nombre=n1
        base=n1
        n2=-n2
        for _ in range(n2-1):
            nombre+=base
        return nombre

    elif n1<0 and n2>0:
        n1=-n1
        nombre=n1
        base=n1
        for _ in range(n2-1):
            nombre+=base
        return -nombre
    
    elif n1>0 and n2<0:
        n2=-n2
        nombre=n1
        base=n1
        for _ in range(n2-1):
            nombre+=base
        return -nombre
    
    elif n1>0 and n2>0:
        nombre=n1
        base=n1
        for _ in range(n2-1):
            nombre+=base
        return nombre
        





def chercher(tab, x, i, j):
    '''
    >>> chercher([1, 5, 6, 6, 9, 12], 1, 0, 5)
    0
    >>> chercher([1, 5, 6, 6, 9, 12], 9, 0, 5)
    4
    >>> chercher([1, 5, 6, 6, 9, 12], 6, 0, 5)
    2
    >>> chercher([1], 0, 0, 0)
    >>> chercher([1], 1, 0, 0)
    0

    Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.
    '''

    if i > j:
        return None
    m = (i + j) // 2
    if tab[m] < x: 
        return chercher(tab, x, m + 1, j) 
    elif tab[m] > x:
        return chercher(tab, x, i, m - 1) 
    else:
        return m

if __name__ =="__main__":
    import doctest
    doctest.testmod()
