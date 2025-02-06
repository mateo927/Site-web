import database

from modele import Classe

def get_all_Classes() -> list[Classe]:
    """Retourne la liste de tous les élèves"""    
    with database.get_connection() as conn:
        with conn.cursor() as cur:
            #Le select est effectué en fonction de l'orrdre des paramètres du modèle 
            cur.execute("SELECT id, nom, eleves FROM eleves ORDER BY nom, eleves")
            return [Classe(row[0], row[1], row[2]) for row in cur.fetchall()]


def get_classe(id: int) -> Classe|None:
    """Retourne l'élève d'ID id, ou None si non trouvé"""
    with database.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, nom, eleves FROM Classe WHERE id = %s", (id,))
            row = cur.fetchone()
            if row is None:
                return None
            return Classe(row[0], row[1], row[2]) # type: ignore


def create_classe(nom: str, eleves: str) -> int:
    """Crée un nouvel élève et retourne son ID"""
    with database.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO Classe (nom, eleves) VALUES (%s, %s) RETURNING id", (nom,eleves))
            # L'id est créée automatiquement, on la retourne et on la récupère
            return cur.fetchone()[0] # type: ignore


def update_classe(id: int, nom: str, eleves: str) -> None:
    """Modifie l'élève d'ID id"""
    with database.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE Classe SET nom = %s, eleves = %s WHERE id = %s", (nom, id,eleves))


def delete_classe(id: int) -> None:
    """Supprime l'élève d'ID id"""
    with database.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM Classe WHERE id = %s", (id,))
