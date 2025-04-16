
def recherche(tab:list[int],n:int)-> int:
    '''>>> recherche([2, 3, 4 , 5, 6], 5)
    3
    >>> recherche([2, 3, 4, 6, 7], 5) # renvoie None
    
    '''
    gauche=0
    droite=len(tab)
    resultat=droite//2
  
    for _ in range(len(tab)):
        if tab[resultat]<n:
            gauche=resultat
            resultat = droite//gauche+1
 
        elif tab[resultat]>n:
            droite=resultat
            resultat = droite//gauche+1

        elif tab[resultat]==n:
            return resultat
    return 



alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet'''
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    '''
    >>> cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4)
    'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
    >>> cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5)
    'BONJOUR A TOUS. VIVE LA MATIERE NSI !'

    
    Renvoie le message codé par la méthode de César
    pour le decalage donné'''
    resultat = ''
    for c in message: 
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c)+decalage) % 26 
            resultat = resultat + alphabet[indice]
        else:
            resultat = resultat + c
    return resultat


if __name__ == "__main__":
    import doctest
    doctest.testmod()
