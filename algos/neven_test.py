#uv run -m algos.graphe
#from random import randint
#from structures.graphe import graphe_no
#from structures.lineaires import file
#from structures.lineaires import pile



#def bsf_graphe_no(s:str , g: graphe_no.graphe):
    #f=file.creer()
    #file.enfiler(f,s)
    #deja_enfiler=[s]
#    while not file.est_vide(f):
#        tmp=file.defiler(f)
#        print(tmp)
#        for v in graphe_no.get_voisins(tmp,g):
#            if v not in deja_enfiler:
#                file.enfiler(f,v)
#                deja_enfiler.append(v)
                
#def dfs(depart: str, g: graphe_no.graphe)->list:
#    p=pile.creer()
#    pile.empiler(p,depart)
#    deja_empiler=[depart]
#    while not pile.est_vide(p):
#        tmp=pile.empiler(p)
#        for v in graphe_no.get_voisins(tmp,g):
#            if v not in deja_empiler:
#                pile.empiler(p,v)
#                deja_empiler.append(v)
 #   return deja_empiler


#def genere_aleatoire(nb_sommets:int, densite:float)->graphe_no.graphe:
 #   g=graphe_no.creer()
#    liste_connexions=[()]
#    for i in range(nb_sommets):
#        graphe_no.ajouter_sommet(str(i),g)
#    nombre_aretes=int(densite*nb_sommets*(nb_sommets-1)/2)
#    for _ in range(nombre_aretes):
#        lst=graphe_no.sommets(g)
#        s1=lst[randint(0,len(lst)-1)]
#        s2=lst[randint(0,len(lst)-1)]
#        while s1==s2 or (s1,s2) in liste_connexions or (s2,s1) in liste_connexions:
#            s1=lst[randint(0,len(lst)-1)]
#        graphe_no.set_arete(s1,s2,g)
#        liste_connexions.append((s1,s2))
#    return g


#if __name__ == "__main__":                           
#    import doctest
#    doctest.testmod()

#    from structures.graphe import dessin
# 
#    g = genere_aleatoire(10, 0.5)
#    dessin.genere_image(g)





    
    