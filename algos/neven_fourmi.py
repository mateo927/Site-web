#uv run -m algos.neven_fourmi  
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
    for element in graphe:
        for i in element:
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
