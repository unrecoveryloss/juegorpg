from config.db import get_connection

class EquipoModel:
    @staticmethod
    def create_equipo(nombre_equipo, descripcion_equipo, origen_equipo):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = "INSERT INTO equipo (nombre_equipo, descripcion_equipo, origen_equipo) VALUES (%s, %s, %s)"
                cursor.execute(sql, (nombre_equipo, descripcion_equipo, origen_equipo))
                conn.commit()
            return True, "Equipamiento creado exitosamente"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def get_all_equipos():
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM equipo")
                result = cursor.fetchall()
            return result
        except:
            return []
        finally:
            conn.close()

    @staticmethod
    def get_equipo_by_id(id_equipo):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM equipo WHERE id_equipo = %s", (id_equipo,))
                return cursor.fetchone()
        except:
            return None
        finally:
            conn.close()

    @staticmethod
    def update_equipo(id_equipo, nombre_equipo, descripcion_equipo, origen_equipo):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = "UPDATE equipo SET nombre_equipo = %s, descripcion_equipo = %s, origen_equipo = %s WHERE id_equipo = %s"
                cursor.execute(sql, (nombre_equipo, descripcion_equipo, origen_equipo, id_equipo))
                conn.commit()
            return True, "Equipamiento actualizado correctamente"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def delete_equipo(id_equipo):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM equipo WHERE id_equipo = %s", (id_equipo,))
                conn.commit()
            return True, "Equipamiento eliminado correctamente"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()
