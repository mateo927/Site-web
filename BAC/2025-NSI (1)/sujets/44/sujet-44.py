coeur = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]




def moyenne(notes:list[tuple[float,float]])->float|None:
    '''
    >>> moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)])
    9.142857142857142
    >>> moyenne([(3, 0), (5, 0)])
    '''
    
    numerateur=0
    denominateur=0
    for notes_coef in notes:
        numerateur+=notes_coef[0]*notes_coef[1]
        denominateur+=notes_coef[1]
    
    if denominateur == 0:
        return None
    
    return numerateur/denominateur

def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par 
        un "*" , les 0 par une espace " " '''
    for ligne in dessin:
        affichage = ''
        for col in ligne:
            if col == 1:
                affichage = affichage + "*"
            else:
                affichage = affichage + " "
        print(affichage)


def liste_zoom(liste_depart,k):
    '''
    >>> liste_zoom([1,2,3],3)
    [1, 1, 1, 2, 2, 2, 3, 3, 3]
    
    renvoie une liste contenant k fois chaque élément de
    liste_depart
    '''
    liste_zoomee = [] 
    for elt in liste_depart : 
        for i in range(k):
            liste_zoomee.append(elt)
    return liste_zoomee

def dessin_zoom(grille,k):
    '''
    renvoie une grille où les lignes sont zoomées k fois 
    ET répétées k fois
    '''
    grille_zoomee=[]
    for ligne in grille:
        ligne_zoomee = liste_zoom(ligne,k) 
        for i in range(k):
            grille_zoomee.append(ligne_zoomee) 
    return grille_zoomee

if __name__ == "__main__":
    import doctest
    doctest.testmod()