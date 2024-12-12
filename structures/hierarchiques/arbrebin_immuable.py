import random as rd
# On modélise le vide par un tuple vide. Donc le type vide est le type du tuple vide.
type vide = tuple[()]
# Un arbre est vide ou c'est un tuple constitué d'une clé et de 2 arbres, le sag et le sad.
type arbrebin[T] = vide|tuple[T, arbrebin[T], arbrebin[T]] 

ARBRE_VIDE = ()

def cle[T](a: arbrebin[T]) -> T:
    assert len(a)==3, "L'arbre est vide"
    return a[0]
        
def sag[T](a: arbrebin[T]) -> arbrebin[T]:
    assert len(a)==3, "L'arbre est vide"
    return a[1]

def sad[T](a: arbrebin[T]) -> arbrebin[T]:
    assert len(a)==3, "L'arbre est vide"
    return a[2]

def creer[T](e: T, gauche: arbrebin[T], droite: arbrebin[T]) -> arbrebin[T]:
    return (e, gauche, droite)

def creer_feuille[T](e: T) -> arbrebin[T]:
    return (e, ARBRE_VIDE, ARBRE_VIDE)

def est_vide[T](a: arbrebin[T]) -> bool:
    return len(a) == 0

#! A partir de maintenant, nous n'utiliserons plus les tuples.

def exemple() -> arbrebin[int]:
    a = creer(11, creer_feuille(9), ARBRE_VIDE)
    b = creer(18, creer_feuille(15), creer_feuille(19))
    f = creer(14, a, b)
    g = creer_feuille(25)
    h = creer_feuille(32)
    i = creer(28, g, h)
    return creer(21, f, i)

def hauteur[T](a: arbrebin[T]) -> T:
    if est_vide(a):
        return 0 
    if est_vide(sag(a)) and est_vide(sad(a)): 
        return 1 
    return 1 + max(hauteur(sag(a)), hauteur(sad(a)))

def taille[T](a: arbrebin[T]) -> T:
    if est_vide(a):
        return 0 
    if est_vide(sag(a)) and est_vide(sad(a)): 
        return 1 
    return 1 + taille(sag(a)) + taille(sad(a))

def somme[T](a: arbrebin[T]) -> T:
    if est_vide(a):
        return 0 
    if est_vide(sag(a)) and est_vide(sad(a)): 
        return a 
    return a + somme(sag(a)) + somme(sad(a))

def to_str[T](a: arbrebin[T]) -> T:
    if est_vide(a):
        return "_|_"
    if est_vide(sag(a)) and est_vide(sad(a)): 
        return f"{a}" "->" "_|_"
    return f"{a}" "->" f"{to_str(sag(a))}" "->" f"{to_str(sad(a))}"

def minimum[T](a: arbrebin[T]) -> T:
    if est_vide(a):
        return "pas de minimum" 
    if est_vide(sag(a)) and est_vide(sad(a)): 
        return a 
    return min(a + minimum(sag(a)) + minimum(sad(a)))

def maximum[T](a: arbrebin[T]) -> T:
    if est_vide(a):
        return "pas de maximum" 
    if est_vide(sag(a)) and est_vide(sad(a)): 
        return a 
    return max(a+ maximum(sag(a)) + maximum(sad(a)))

def sont_egaux[T](a: arbrebin[T],a1: arbrebin[T]) -> T:
    if taille(a) != taille(a1):
        return  False
    return True if sont_egaux(sad(a),sad(a1)) and sont_egaux(sag(a),sag(a1)) else False

def genere_alea(h: int) -> arbrebin:
    if h==1:
        return creer_feuille(rd.randint(1,100))
    else:
        arbre_gauche=genere_alea(h-1)
        arbre_droite=genere_alea(h-1)
        return creer(rd.randint(1,100),arbre_gauche,arbre_droite)
def sont_miroirs[T](a1: arbrebin[T], a2: arbrebin[T]) -> bool:
    assert est_vide(a1) and  est_vide(a2)
    

if __name__ == "__main__":

    import doctest
    from .import dessin

    print(f"Début des tests pour {__file__}")
    res = doctest.testmod()
    print(f"Fin des tests pour {__file__}")

    dessin.show(genere_alea(2))