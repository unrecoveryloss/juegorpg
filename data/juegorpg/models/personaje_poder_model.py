from config.db import get_connection

class PersonajePoderModel:
    @staticmethod
    def asignar_poder(id_personaje, id_poder):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = "INSERT INTO personaje_poder (id_personaje, id_poder) VALUES (%s, %s)"
                cursor.execute(sql, (id_personaje, id_poder))
                conn.commit()
            return True, "Poder asignado"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def obtener_poderes_personaje(id_personaje):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = """
                    SELECT p.id_poder, p.nombre_poder, p.descripcion_poder, p.origen_poder
                    FROM personaje_poder pp
                    JOIN poder p ON pp.id_poder = p.id_poder
                    WHERE pp.id_personaje = %s
                """
                cursor.execute(sql, (id_personaje,))
                return cursor.fetchall()
        except Exception as e:
            return []
        finally:
            conn.close()

    @staticmethod
    def eliminar_poder_personaje(id_personaje, id_poder):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = "DELETE FROM personaje_poder WHERE id_personaje = %s AND id_poder = %s"
                cursor.execute(sql, (id_personaje, id_poder))
                conn.commit()
            return True, "Poder eliminado del personaje"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()
