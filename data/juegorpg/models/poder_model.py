from config.db import get_connection

class PoderModel:
    @staticmethod
    def create_poder(nombre_poder, descripcion_poder, origen_poder, id_raza):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = "INSERT INTO poder (nombre_poder, descripcion_poder, origen_poder, id_raza) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (nombre_poder, descripcion_poder, origen_poder, id_raza))
                conn.commit()
            return True, "Poder creado exitosamente"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def get_all_poderes():
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM poder")
                return cursor.fetchall()
        except Exception:
            return []
        finally:
            conn.close()

    @staticmethod
    def get_poder_by_id(id_poder):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM poder WHERE id_poder = %s", (id_poder,))
                return cursor.fetchone()
        except Exception:
            return None
        finally:
            conn.close()

    @staticmethod
    def update_poder(id_poder, nombre_poder, descripcion_poder, origen_poder, id_raza):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = """UPDATE poder SET nombre_poder = %s, descripcion_poder = %s, origen_poder = %s, id_raza = %s 
                         WHERE id_poder = %s"""
                cursor.execute(sql, (nombre_poder, descripcion_poder, origen_poder, id_raza, id_poder))
                conn.commit()
            return True, "Poder actualizado correctamente"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def delete_poder(id_poder):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM poder WHERE id_poder = %s", (id_poder,))
                conn.commit()
            return True, "Poder eliminado correctamente"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()
