import time
import random


def tri_selection(L: list[int]):
    """
    Tri par selection EN PLACE
    
    >>> tableau = [12, 5, 7, 3, 10, 9, 1, 4]
    >>> tri_selection(tableau)
    >>> tableau
    [1, 3, 4, 5, 7, 9, 10, 12]
    """
    for i in range(len(L)):
        imin = i
        for j in range(i + 1, len(L)):
            if L[j] < L[imin]:
                imin = j
        L[i], L[imin] = L[imin], L[i]

def tri_insertion(L: list[int]):
    """
    Tri par insertion EN PLACE

    >>> tableau = [12, 5, 7, 3, 10, 9, 1, 4]
    >>> tri_insertion(tableau)
    >>> tableau
    [1, 3, 4, 5, 7, 9, 10, 12]
    """
    for i in range(1, len(L)):
        j = i
        while j > 0 and L[j-1] > L[i]:
            L[j] = L[j-1]
            j -= 1
        L[j] = L[i]


def fusion(L1: list[int], L2: list[int]) -> list[int]:
    """
    Fusion de deux tableaux triés d'un type quelconque T qui est Comparable.
    Par exemple list[int], ou list[str]
    """
    i, j = 0, 0
    res: list[int] = []
    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            res.append(L1[i])
            i += 1
        else:
            res.append(L2[j])
            j += 1
    while i < len(L1):
        res.append(L1[i])
        i += 1
    while j < len(L2):
        res.append(L2[j])
        j += 1
    return res

#! Les tris suivants ne sont pas en place (il en existe des versions en place)

def tri_fusion(L: list[int]) -> list[int]:
    """
    Implémentation d'un tri fusion
    Diviser pour mieux régner:
    Résoudre sur des sous problèmes n (ici 2) fois moins grands puis combiner les résultats

    >>> tableau = [12, 5, 7, 3, 10, 9, 1, 4]
    >>> tri_fusion(tableau)
    [1, 3, 4, 5, 7, 9, 10, 12]
    """

    n = len(L)
    if n <= 1:
        return L
    else:
        m = n // 2
        return fusion(tri_fusion(L[:m]), tri_fusion(L[m:]))

def quick_sort(L: list[int]) -> list[int]:
    """
    Implémentation d'un quick sort

    >>> tableau = [12, 5, 7, 3, 10, 9, 1, 4]
    >>> quick_sort(tableau)
    [1, 3, 4, 5, 7, 9, 10, 12]
    """
    if len(L) <= 1:
        return L
    else:
        pivot = L[0]
        gauche = [x for x in L[1:] if x < pivot]
        droite = [x for x in L[1:] if x >= pivot]
        return quick_sort(gauche) + [pivot] + quick_sort(droite)


def counting_sort(L: list[int]) -> list[int]:
    """
    Ce tri en O(n) n'existe que pour les entiers positifs.
    Sa complexité en espace peut être très importante car elle nécessite la création d'un tableau de taille max(L) + 1
    Il peut être généralisé aux entiers relatif par décalage par rapport au minimum de L

    >>> tableau = [12, 5, 7, 3, 10, 9, 1, 4]
    >>> counting_sort(tableau)
    [1, 3, 4, 5, 7, 9, 10, 12]
    """
    
    max_val = max(L)
    count = [0] * (max_val + 1)
    for x in L:
        count[x] += 1
    res: list[int] = []
    for i in range(max_val + 1):
        for _ in range(count[i]):
            res.append(i)
    return res



def mesurer_temps_execution(sort_func, data, en_place: bool = True) -> float:
    """
    Mesure le temps d'exécution d'une fonction de tri.
    - sort_func : la fonction de tri (un callable).
    - data : les données à trier (une liste).
    - en_place : indique si la fonction trie en place ou renvoie une copie triée.

    Retourne le temps en secondes.
    """
    # On copie la liste si la fonction ne trie pas en place
    # ou si on veut éviter de modifier l'originale.
    data_copy = data.copy()

    # Mesure du temps
    debut = time.perf_counter()
    if en_place:
        sort_func(data_copy)
    else:
        copie = sort_func(data_copy)  # noqa
    fin = time.perf_counter()

    return fin - debut


def comparer_tous_les_tris():
    # Tailles de tableaux à tester
    tailles = [1000, 5000, 10_000, 20_000, 50_000, 100_000,1_000_000]

    # Nombre d'itérations pour chaque taille (pour moyenner un peu le résultat)
    iterations_par_taille = 5 # Il en faudrait au moins 30
    
    print("Comparaison des algorithmes de tri :\n")

    for taille in tailles:
        print(f"--- Taille du tableau : {taille} ---")
        
        # Nous allons cumuler les temps d'exécution pour ensuite calculer une moyenne.
        temps_selection = 0.0
        temps_insertion = 0.0
        temps_fusion = 0.0
        temps_rapide = 0.0
        temps_counting = 0.0

        for _ in range(iterations_par_taille):
            # Génération d'un tableau de "taille" entiers aléatoires dans [0; 10_000]
            tableau = [random.randint(0, taille*2) for _ in range(taille)]

            #temps_selection += mesurer_temps_execution(tri_selection, tableau, en_place=True)
            temps_insertion += mesurer_temps_execution(tri_insertion, tableau, en_place=True)
            #temps_fusion    += mesurer_temps_execution(tri_fusion, tableau, en_place=False)
            #temps_rapide    += mesurer_temps_execution(quick_sort,   tableau, en_place=False)
            temps_counting  += mesurer_temps_execution(counting_sort, tableau, en_place=False)

        # Calcul de la moyenne sur les différentes itérations
        temps_selection /= iterations_par_taille
        temps_insertion /= iterations_par_taille
        temps_fusion    /= iterations_par_taille
        temps_rapide    /= iterations_par_taille
        temps_counting  /= iterations_par_taille

        print(f"Tri par sélection O(n²)      : {temps_selection:.6f} s")
        print(f"Tri par insertion O(n²)      : {temps_insertion:.6f} s")
        print(f"Tri fusion        O(n log(n)): {temps_fusion:.6f} s")
        print(f"Tri rapide (QS)   O(n log(n)): {temps_rapide:.6f} s")
        print(f"Counting sort     O(n)       : {temps_counting:.6f} s")




if __name__ == "__main__":
    import doctest
    doctest.testmod()
    comparer_tous_les_tris()