
def moyenne(notes=list[tuple[float,int]])->float:
    """
    >>> moyenne([(15.0,2),(9.0,1),(12.0,3)])
    12.5

    """
    notes_tt=0
    coef=0
    for element in notes:
        notes_tt+= element[0]*element[1]
        coef+=element[1]
    return notes_tt/coef



def ligne_suivante(ligne):
    '''Renvoie la ligne suivant ligne du triangle de Pascal'''
    ligne_suiv = [ligne[0]] 
    for i in range(1,len(ligne)): 
        ligne_suiv.append(ligne[i]+ligne[i-1])
    ligne_suiv.append(ligne[len(ligne)-1]) 
    return ligne_suiv

def pascal(n):
    '''
    >>> ligne_suivante([1, 3, 3, 1])
    [1, 4, 6, 4, 1]
    >>> pascal(2)
    [[1], [1, 1], [1, 2, 1]]
    >>> pascal(3)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    
    Renvoie le triangle de Pascal de hauteur n
    
    '''
    triangle = [ [1] ]
    for k in range(n): 
        ligne_k = ligne_suivante(triangle[k]) 
        triangle.append(ligne_k)
    return triangle

if __name__ == "__main__":
    import doctest
    doctest.testmod()
