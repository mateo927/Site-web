import database

from modele import Eleve

def get_all_eleves() -> list[Eleve]:
    """Retourne la liste de tous les élèves"""    
    with database.get_connection() as conn:
        with conn.cursor() as cur:
            #Le select est effectué en fonction de l'orrdre des paramètres du modèle 
            cur.execute("SELECT id, nom,prenom,age , classe FROM eleves ORDER BY nom, prenom,age,classe")
            return [Eleve(row[0], row[1], row[2],row[3],row[4]) for row in cur.fetchall()]


def get_eleve(id: int) -> Eleve|None:
    """Retourne l'élève d'ID id, ou None si non trouvé"""
    with database.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, nom, prenom,age ,classe FROM eleves WHERE id = %s", (id,))
            row = cur.fetchone()
            if row is None:
                return None
            return Eleve(row[0], row[1], row[2],row[3],row[4]) # type: ignore


def create_eleve(nom: str, prenom: str,age:int,classe:str) -> int:
    """Crée un nouvel élève et retourne son ID"""
    with database.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO eleves (nom, prenom,age,classe) VALUES (%s, %s) RETURNING id", (nom, prenom,age,classe))
            # L'id est créée automatiquement, on la retourne et on la récupère
            return cur.fetchone()[0] # type: ignore


def update_eleve(id: int, nom: str, prenom: str,age:int,classe:str) -> None:
    """Modifie l'élève d'ID id"""
    with database.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE eleves SET nom = %s, prenom = %s, age = %s,classe = %s, WHERE id = %s", (nom, prenom,age,classe, id))


def delete_eleve(id: int) -> None:
    """Supprime l'élève d'ID id"""
    with database.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM eleves WHERE id = %s", (id,))
