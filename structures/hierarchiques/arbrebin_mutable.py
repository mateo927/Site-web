class ArbreBin:
    def __init__(self, cle, gauche: 'ArbreBin', droit: 'ArbreBin'):
        self.cle = cle
        self.gauche = gauche
        self.droit = droit

    def est_feuille(self):
        return self.gauche is ARBRE_VIDE and self.droite is ARBRE_VIDE

    def est_vide(self):
        return self.gauche is ARBRE_VIDE and self.droite is ARBRE_VIDE

    def taille(self) -> int:
        if self.est_vide():
            return -1
        return 1 + self.gauche.taille() + self.droit.taille()
    def hauteur(self)-> int :
        if self.est_vide:
            return 0 
        if self.est_vide(self.gauche) and self.est_vide(self.droit): 
            return 1 
        return 1 + max(self.hauteur(self.gauche), self.hauteur(self.droit))
    def somme(self)-> int :
        if self.est_vide:
            return 0 
        if self.est_vide(self.gauche) and self.est_vide(self.droit): 
            return self.cle 
        return self.cle + self.somme(self.gauche)+ self.somme(self.droit)
    def to_str(self)-> int :
        if self.est_vide:
            return "_|_" 
        if self.est_vide(self.gauche) and self.est_vide(self.droit): 
            return f"{self.cle}" + "->" + "_|_"
        return  f"{self.cle}" +"->" + f"{self.to_str(self.gauche)}"+ "->" + f"{self.to_str(self.droit)}"
    def minimum(self)-> int :
        if self.est_vide:
            return "pas de minimum" 
        if self.est_vide(self.gauche) and self.est_vide(self.droit): 
            return self.cle
        return min(self.cle,self.minimum(self.gauche), self.minimum(self.droit))
    def maximum(self)-> int :
        if self.est_vide:
            return "pas de maximum" 
        if self.est_vide(self.gauche) and self.est_vide(self.droit): 
            return self.cle
        return max(self.cle,self.maximum(self.gauche), self.maximum(self.droit))
    def sont_egaux(self,a1: 'ArbreBin') -> bool:
        if self.taille(self) != self.taille(a1):
            return  False
        return True if self.sont_egaux(self.gauche,a1.gauche) and self.sont_egaux(self.droit,a1.droit) else False

    
class Sentinelle(ArbreBin):
    def __init__(self):
        super().__init__(0, self, self)

ARBRE_VIDE = Sentinelle()