#uv run -m algos.fourmi.fourmi
from random import randint 
import random
type matrice[T] = list[list[T]]
type chemin = list[int]


def init_pheromones(nb_sommets: int,tau_initial: float=1.0) -> matrice[float]:
    """Initialise la matrice des phéromones à tau_initial. 
    tau_initial est la contribution en phéromones de chaque arête"""
    matrice=[[tau_initial for _ in range (nb_sommets)] for _ in range(nb_sommets)]
    for i in range (nb_sommets):
        matrice[i][i]=0.0
    return matrice
    
    


def calculer_visibilite(graphe: matrice[float]) -> matrice[float]:
    """Renvoie la matrice de visibilité.
    La visibilité de chaque arête est l'inverse de la distance    """
    lst=[]
    matrice=[]
    for ele in graphe:
        for i in ele:
            if i==0:
                lst.append(0)
            else:
                lst.append(1/i)
        matrice.append(lst)
        lst=[]
    return matrice
            
            

def get_graphe_exemple() -> matrice[float]:
    return [
        [0, 2, 9, 10],
        [2, 0, 6, 4],
        [9, 6, 0, 8],
        [10, 4, 8, 0]
    ]

def prochain_sommet(pheromones: matrice[float], visibilite: matrice[float],sommet_courant: int,inexplore: list[int],alpha: float, beta: float) -> int:
    """Renvoit le prochain sommet au hasard en fonction de l attractivité des chemins.Notre fourmi est quand même plus intelligente qu'une fourmi classique, elle ne va pas aux endroits déjà visités.        
    >>> random.seed(54)    
    >>> g = get_graphe_exemple()    
    >>> n = len(g) 
    >>> prochain_sommet(init_pheromones(n), calculer_visibilite(g), 0, list(range(n)), 1, 2)    
    1 
    """
    proba=[]
    somme=0
    for i in inexplore:
        tmp=pheromones[sommet_courant][i]**alpha*visibilite[sommet_courant][i]**beta
        somme+=tmp
        proba.append(tmp)
    probatotal=[i/somme for i in proba]

    return random.choices(inexplore,weights=probatotal)




def parcours_fourmi( graphe: matrice[float],pheromones: matrice[float],visibilite: matrice[float],alpha: float, beta: float) -> tuple[chemin, float]:
    """    Simule le parcours d'une seule fourmi choisissant au hasard un sommet de départ inexploré.    
    Renvoie le chemin ainsi que la longueur de ce chemin.    
    >>> random.seed(54)    
    >>> g = get_graphe_exemple()    
    >>> n = len(g)    
    >>> parcours_fourmi(g, init_pheromones(n), calculer_visibilite(g), 1, 2)   
    ([1, 0, 2, 3, 1], 23)    
    """
    distance=0
    parcours=[]
    inexplore=[i for i in range(len(graphe))]
    sommet_courant=randint(0,len(graphe)-1)
    parcours.append(sommet_courant)
    inexplore.remove(sommet_courant)
    sommet_suivant=prochain_sommet(pheromones,visibilite,sommet_courant,inexplore,alpha,beta)

    while sommet_suivant!=[]:
        sommet_suivant=sommet_suivant[0]
        if sommet_suivant in inexplore:
            inexplore.remove(sommet_suivant)
        distance += graphe[sommet_courant][sommet_suivant]
        parcours.append(sommet_suivant)
        sommet_suivant = prochain_sommet(pheromones, visibilite, sommet_courant, inexplore, alpha, beta)
        
    return parcours,distance





def simuler_colonie(graphe: matrice[float],pheromones: matrice[float],visibilite: matrice[float],nb_fourmis: int,alpha: float, beta: float)-> tuple[list[chemin], list[float]]:
    """Simule le parcours de nb_fourmis fourmis d'une colonie lancées l'une après l'autre dans le graphe.
    Renvoie la liste des cyles obtenus, ainsi que la liste des distances correspondantes 
    >>> random.seed(54)     
    >>> g = get_graphe_exemple()    
    >>> n = len(g)    
    >>> simuler_colonie(g, init_pheromones(n), calculer_visibilite(g), 5, 1, 2)    
    ([[1, 0, 2, 3, 1], [3, 1, 0, 2, 3], [3, 2, 1, 0, 3], [1, 0, 3, 2, 1], [0, 1, 3, 2, 0]], [23, 23, 26, 26, 23])"""
    list_cycles=[]
    liste_distance=[]
    for i in range (nb_fourmis) :
        tmp=parcours_fourmi(graphe, pheromones, visibilite, alpha, beta)
        list_cycles.append(tmp[0])
        liste_distance.append(tmp[1])
    
    return list_cycles,liste_distance
        
    
def update_pheromones(pheromones: matrice[float],chemins: list[chemin],longueurs_chemins: list[float],rho: float, Q: float):
    """Met à jour les phéromones sur les arêtes. Dans un premier temps, toutes les phéromones 
    diminuent du facteur rho. Dans un deuxième temps, pour chaque chemin de longueur d, toutes   
    les arête augmentent en phéromone de Q/d.        
    >>> g = get_graphe_exemple()    
    >>> chemins = [[1,0,2,3,1], [3,1,0,2,3], [3,2,1,0,3], [1,0,3,2,1], [0,1,3,2,0]]    
    >>> distances = [23, 23, 26, 26, 23]    
    >>> p = init_pheromones(len(g))    
    >>> update_pheromones(p, chemins,  distances, 0.5, 100)    
    >>> [round(val) for ligne in p for val in ligne]    [0, 21, 14, 8, 21, 0, 8, 14, 14, 8, 0, 21, 8, 14, 21, 0]    """
    for i in range(len(pheromones)):
        for j in range(len(pheromones)):
            pheromones[i][j]=pheromones[i][j]*rho

    for i in range (len(chemins)):
        for j in range (len(chemins[i])-1):
            pheromones[chemins[i][j]][chemins[i][j+1]]+=Q/longueurs_chemins[i]
            pheromones[chemins[i][j+1]][chemins[i][j]]+=Q/longueurs_chemins[i]
              
 

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    