import pymysql
import pymysql.cursors
from config.db import get_connection

class CharacterService:
    @staticmethod
    def create_character(data):
        nombre = data.get('nombre_personaje')
        nivel = data.get('nivel', 1)
        id_usuario = data.get('id_usuario')
        id_raza = data.get('id_raza')
        id_estado = data.get('id_estado')

        if not all([nombre, id_usuario, id_raza, id_estado]):
            return False, "Faltan datos obligatorios"

        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO personaje (nombre_personaje, nivel, id_usuario, id_raza, id_estado)
                    VALUES (%s, %s, %s, %s, %s)
                """, (nombre, nivel, id_usuario, id_raza, id_estado))
            return True, "Personaje creado exitosamente"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def get_all_characters():
        try:
            conn = get_connection()
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("""
                    SELECT p.id_personaje, p.nombre_personaje, p.nivel,
                           u.nombre_usuario as usuario,
                           r.nombre_raza as raza,
                           e.nombre_estado as estado
                    FROM personaje p
                    JOIN usuario u ON p.id_usuario = u.id_usuario
                    JOIN raza r ON p.id_raza = r.id_raza
                    JOIN estado e ON p.id_estado = e.id_estado
                    ORDER BY p.id_personaje
                """)
                return cursor.fetchall()
        except Exception as e:
            return []
        finally:
            conn.close()

    @staticmethod
    def get_characters_by_user(nombre_usuario):
        try:
            conn = get_connection()
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("""
                    SELECT p.id_personaje, p.nombre_personaje, p.nivel,
                           u.nombre_usuario as usuario,
                           r.nombre_raza as raza,
                           e.nombre_estado as estado
                    FROM personaje p
                    JOIN usuario u ON p.id_usuario = u.id_usuario
                    JOIN raza r ON p.id_raza = r.id_raza
                    JOIN estado e ON p.id_estado = e.id_estado
                    WHERE u.nombre_usuario = %s
                    ORDER BY p.id_personaje
                """, (nombre_usuario,))
                return cursor.fetchall()
        except Exception as e:
            return []
        finally:
            conn.close()

    @staticmethod
    def get_character_by_id(character_id):
        try:
            conn = get_connection()
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("""
                    SELECT p.id_personaje, p.nombre_personaje, p.nivel,
                           u.nombre_usuario as usuario,
                           r.nombre_raza as raza,
                           e.nombre_estado as estado
                    FROM personaje p
                    JOIN usuario u ON p.id_usuario = u.id_usuario
                    JOIN raza r ON p.id_raza = r.id_raza
                    JOIN estado e ON p.id_estado = e.id_estado
                    WHERE p.id_personaje = %s
                """, (character_id,))
                return cursor.fetchone()
        except Exception as e:
            return None
        finally:
            conn.close()

    @staticmethod
    def update_character(character_id, data):
        nombre = data.get('nombre_personaje')
        nivel = data.get('nivel')
        id_raza = data.get('id_raza')
        id_estado = data.get('id_estado')

        if not all([nombre, nivel, id_raza, id_estado]):
            return False, "Faltan datos para actualizar"

        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("""
                    UPDATE personaje
                    SET nombre_personaje = %s,
                        nivel = %s,
                        id_raza = %s,
                        id_estado = %s
                    WHERE id_personaje = %s
                """, (nombre, nivel, id_raza, id_estado, character_id))
            return True, "Personaje actualizado exitosamente"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def delete_character(character_id):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM personaje WHERE id_personaje = %s", (character_id,))
            return True, "Personaje eliminado exitosamente"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()
