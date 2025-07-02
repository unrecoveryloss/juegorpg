from config.db import get_connection

class HabilidadModel:
    @staticmethod
    def create_habilidad(data):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = """
                INSERT INTO habilidad (nombre_habilidad, descripcion_habilidad, origen_habilidad, id_raza)
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(sql, (
                    data.get("nombre_habilidad"),
                    data.get("descripcion_habilidad"),
                    data.get("origen_habilidad"),
                    data.get("id_raza")
                ))
                conn.commit()
            return True, "Habilidad creada correctamente"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def get_all_habilidades():
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM habilidad")
                return cursor.fetchall()
        except Exception:
            return []
        finally:
            conn.close()

    @staticmethod
    def get_habilidad_by_id(id_habilidad):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM habilidad WHERE id_habilidad = %s", (id_habilidad,))
                return cursor.fetchone()
        except Exception:
            return None
        finally:
            conn.close()

    @staticmethod
    def update_habilidad(id_habilidad, data):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = """
                UPDATE habilidad SET nombre_habilidad=%s, descripcion_habilidad=%s,
                origen_habilidad=%s, id_raza=%s WHERE id_habilidad=%s
                """
                cursor.execute(sql, (
                    data.get("nombre_habilidad"),
                    data.get("descripcion_habilidad"),
                    data.get("origen_habilidad"),
                    data.get("id_raza"),
                    id_habilidad
                ))
                conn.commit()
            return True, "Habilidad actualizada correctamente"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def delete_habilidad(id_habilidad):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM habilidad WHERE id_habilidad=%s", (id_habilidad,))
                conn.commit()
            return True, "Habilidad eliminada correctamente"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()
