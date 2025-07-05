from config.db import get_connection

class PersonajeEquipoModel:
    @staticmethod
    def asignar_equipo(id_personaje, id_equipo):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = "INSERT INTO personaje_equipo (id_personaje, id_equipo) VALUES (%s, %s)"
                cursor.execute(sql, (id_personaje, id_equipo))
                conn.commit()
            return True, "Equipamiento asignado"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def obtener_equipos_personaje(id_personaje):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = """
                    SELECT e.id_equipo, e.nombre_equipo, e.descripcion_equipo, e.origen_equipo
                    FROM personaje_equipo pe
                    JOIN equipo e ON pe.id_equipo = e.id_equipo
                    WHERE pe.id_personaje = %s
                """
                cursor.execute(sql, (id_personaje,))
                return cursor.fetchall()
        except Exception as e:
            return []
        finally:
            conn.close()

    @staticmethod
    def eliminar_equipo_personaje(id_personaje, id_equipo):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = "DELETE FROM personaje_equipo WHERE id_personaje = %s AND id_equipo = %s"
                cursor.execute(sql, (id_personaje, id_equipo))
                conn.commit()
            return True, "Equipamiento eliminado del personaje"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()
