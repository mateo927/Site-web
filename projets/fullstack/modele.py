from dataclasses import dataclass

@dataclass
class Eleve:
    id: int
    nom: str
    prenom: str
    age : int
    classe: str

@dataclass
class Classe:
    id: int
    nom: str