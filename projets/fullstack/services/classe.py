from modele import Eleve
from modele import Classe

Classes = [Classe(1,'T09',(
        Eleve(1, 'Dupont', 'Jean',15,'T09'),
        Eleve(2, 'Durand', 'Pierre',15,'T09'),
        Eleve(3, 'Dufour', 'Paul',15,'T09'),))
        
    ]

def get_all_Classes() -> list[Eleve]:
    return Classes

def get_Classes(id: int) -> Eleve:
    return [e for e in Classes if e.id == id][0]

def update_Classes(id: int, nom: str, eleves: tuple[Eleve, ...]) -> None:
    e = get_Classes(id)
    e.nom = nom
    e.eleves = eleves

def delete_eleve(id: int) -> None:
    Classes.remove(get_Classes(id))

def create_Classes(nom: str, eleves: tuple[Eleve, ...]) -> int:
    newid: int = max(Classes, key=lambda e: e.id).id + 1
    Classes.append(Classe(newid, nom, eleves))
    return newid