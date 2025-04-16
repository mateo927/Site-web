def fusion(tab1:list[int],tab2:list[int])->list[int]:
    """
    >>> fusion([3, 5], [2, 5])
    [2, 3, 5, 5]

    >>> fusion([-2, 4], [-3, 5, 10])
    [-3, -2, 4, 5, 10]

    >>> fusion([4], [2, 6])
    [2, 4, 6]

    >>> fusion([], [])
    []
    
    >>> fusion([1, 2, 3], [])
    [1, 2, 3]
    
    """

    liste_trier=[]
    indice_de_tab1=0
    indice_de_tab2=0
    while not len(liste_trier)==len(tab1)+len(tab2):
        if indice_de_tab1==len(tab1):
            liste_trier.append(tab2[indice_de_tab2])
            indice_de_tab2+=1
        elif indice_de_tab2==len(tab2):
            liste_trier.append(tab1[indice_de_tab1])
            indice_de_tab1+=1
        elif tab1[indice_de_tab1]<=tab2[indice_de_tab2]:
            liste_trier.append(tab1[indice_de_tab1])
            indice_de_tab1+=1
        else:
            liste_trier.append(tab2[indice_de_tab2])
            indice_de_tab2+=1

    return liste_trier

romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500,"M":1000}

def traduire_romain(nombre):
    """ 
    >>> traduire_romain("XIV")
    14

    >>> traduire_romain("CXLII")
    142

    >>> traduire_romain("MMXXIV")
    2024

    Renvoie l'écriture décimale du nombre donné en chiffres
    romains 

    """

    if len(nombre) == 1:
        return romains[nombre[0]] 
    elif romains[nombre[0]] >=  romains[nombre[1]]: 
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:])-romains[nombre[0]]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
