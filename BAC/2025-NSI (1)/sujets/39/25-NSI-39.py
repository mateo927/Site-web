from flask.config import T


def moyenne(tab:list[int])->float:
    '''
    >>> moyenne([5,3,8])
    5.333333333333333
    >>> moyenne([1,2,3,4,5,6,7,8,9,10])
    5.5
    '''
    
    assert not tab == [],"il faut une liste non vide"
    total_coef=0
    total_points=0
    for element in tab:
        total_points+=element
        total_coef+=1
    return total_points/total_coef



def tri(tab):
    '''
    >>> tab = [0,1,0,1,0,1,0,1,0]
    >>> tri(tab)
    >>> tab
    [0, 0, 0, 0, 0, 1, 1, 1, 1]


    tab est un tableau d'entiers contenant des 0 et des 1.
    La fonction trie ce tableau en plaçant tous les 0 à gauche'''
    i = 0 # premier indice de la zone non triée 
    j = len(tab)-1 # dernier indice de la zone non triée 
    while i < j:
        if tab[i] == 0:
            i = i+1
        else:
            valeur = tab[j] 
            tab[j] = tab[i] 
            tab[i] = valeur
            j = j-1


if __name__ == "__main__":
    import doctest 
    doctest.testmod()