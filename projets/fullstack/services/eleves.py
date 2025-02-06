from modele import Eleve

eleves = [
        Eleve(1, 'Dupont', 'Jean',12,'T09'),
        Eleve(2, 'Durand', 'Pierre',14,'T09'),
        Eleve(3, 'Dufour', 'Paul',15,'T09'),
    ]

def get_all_eleves() -> list[Eleve]:
    return eleves

def get_eleve(id: int) -> Eleve:
    return [e for e in eleves if e.id == id][0]

def update_eleve(id: int, nom: str, prenom: str,age: int,classe:str) -> None:
    e = get_eleve(id)
    e.nom = nom
    e.eleves = prenom
    e.age = age
    e.classe= classe

def delete_eleve(id: int) -> None:
    eleves.remove(get_eleve(id))

def create_eleve(nom: str, prenom: str,age: int,classe:str) -> int:
    newid: int = max(eleves, key=lambda e: e.id).id + 1
    eleves.append(Eleve(newid, nom, prenom,age,classe))
    return newid