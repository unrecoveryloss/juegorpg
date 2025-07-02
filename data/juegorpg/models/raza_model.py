from config.db import get_connection

class RazaModel:
    @staticmethod
    def create_raza(nombre_raza):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = "INSERT INTO raza (nombre_raza) VALUES (%s)"
                cursor.execute(sql, (nombre_raza,))
                conn.commit()
            return True, "Raza creada exitosamente"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def get_all_razas():
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM raza")
                result = cursor.fetchall()
            return result
        except Exception as e:
            return []
        finally:
            conn.close()

    @staticmethod
    def get_raza_by_id(id_raza):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM raza WHERE id_raza = %s", (id_raza,))
                return cursor.fetchone()
        except Exception as e:
            return None
        finally:
            conn.close()

    @staticmethod
    def update_raza(id_raza, nombre_raza):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = "UPDATE raza SET nombre_raza = %s WHERE id_raza = %s"
                cursor.execute(sql, (nombre_raza, id_raza))
                conn.commit()
            return True, "Raza actualizada correctamente"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def delete_raza(id_raza):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = "DELETE FROM raza WHERE id_raza = %s"
                cursor.execute(sql, (id_raza,))
                conn.commit()
            return True, "Raza eliminada correctamente"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def get_raza_by_nombre(nombre_raza):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                sql = "SELECT * FROM raza WHERE nombre_raza = %s"
                cursor.execute(sql, (nombre_raza,))
                return cursor.fetchone()
        except Exception:
            return None
        finally:
            conn.close()