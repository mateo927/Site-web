import database

from modele import Classe

def get_all_Classes() -> list[Classe]:
    """Retourne la liste de toutes les classes"""    
    with database.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, nom FROM Classe ORDER BY nom")
            return [Classe(row[0], row[1], row[2]) for row in cur.fetchall()]

def get_classe(id: int) -> Classe|None:
    """Retourne la classe d'ID id, ou None si non trouvée"""
    with database.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, nom FROM Classe WHERE id = %s", (id,))
            row = cur.fetchone()
            if row is None:
                return None
            return Classe(row[0], row[1], row[2])

def create_classe(nom: str) -> int:
    """Crée une nouvelle classe et retourne son ID"""
    with database.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO Classe (nom) VALUES (%s, %s) RETURNING id", (nom))
            return cur.fetchone()[0]

def update_classe(id: int, nom: str) -> None:
    """Modifie la classe d'ID id"""
    with database.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE Classe SET nom = %s WHERE id = %s", (nom, id))

def delete_classe(id: int) -> None:
    """Supprime la classe d'ID id"""
    with database.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM Classe WHERE id = %s", (id,))