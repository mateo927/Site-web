#uv run -m algos.graphe
from structures.graphe import graphe_no
from structures.lineaires import file
from structures.lineaires import pile

def bsf_graphe_no(s:str , g: graphe_no.graphe):
    f=file.creer()
    file.enfiler(f,s)
    deja_enfiler=[s]
    while not file.est_vide(f):
        tmp=file.defiler(f)
        print(tmp)
        for v in graphe_no.get_voisins(tmp,g):
            if v not in deja_enfiler:
                file.enfiler(f,v)
                deja_enfiler.append(v)
                
def dfs(depart: str, g: graphe_no.graphe)->list:
    p=pile.creer()
    pile.empiler(p,depart)
    deja_empiler=[depart]
    while not pile.est_vide(p):
        tmp=pile.empiler(p)
        for v in graphe_no.get_voisins(tmp,g):
            if v not in deja_empiler:
                pile.empiler(p,v)
                deja_empiler.append(v)
    return deja_empiler
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    from structures.graphe import dessin
 
    g = graphe_no.creer()
    graphe_no.set_arete("A", "B", g)
    graphe_no.set_arete("B", "C", g)
    graphe_no.set_arete("C", "D", g)
    graphe_no.set_arete("D", "E", g)
    graphe_no.set_arete("E", "F", g)
    graphe_no.set_arete("F", "A", g)
    graphe_no.set_arete("A", "C", g)
    graphe_no.set_arete("E", "C", g)
    dessin.genere_image(g)
    bsf_graphe_no("A",g)
    dfs("A",g)
    
    