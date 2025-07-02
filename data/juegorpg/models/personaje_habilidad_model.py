# Archivo nuevo: models/personaje_habilidad_model.py
from config.db import get_connection

class PersonajeHabilidadModel:
    @staticmethod
    def asignar_habilidad(id_personaje, id_habilidad):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = "INSERT INTO personaje_habilidad (id_personaje, id_habilidad) VALUES (%s, %s)"
                cursor.execute(sql, (id_personaje, id_habilidad))
                conn.commit()
            return True, "Habilidad asignada"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def obtener_habilidades_personaje(id_personaje):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = """
                    SELECT h.id_habilidad, h.nombre_habilidad, h.descripcion_habilidad, h.origen_habilidad
                    FROM personaje_habilidad ph
                    JOIN habilidad h ON ph.id_habilidad = h.id_habilidad
                    WHERE ph.id_personaje = %s
                """
                cursor.execute(sql, (id_personaje,))
                return cursor.fetchall()
        except Exception as e:
            return []
        finally:
            conn.close()

    @staticmethod
    def eliminar_habilidad_personaje(id_personaje, id_habilidad):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = "DELETE FROM personaje_habilidad WHERE id_personaje = %s AND id_habilidad = %s"
                cursor.execute(sql, (id_personaje, id_habilidad))
                conn.commit()
            return True, "Habilidad eliminada del personaje"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()
