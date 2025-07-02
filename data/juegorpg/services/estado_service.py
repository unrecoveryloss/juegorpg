from config.db import get_connection

class EstadoService:

    @staticmethod
    def create_estado(data):
        try:
            nombre = data.get("nombre_estado")
            base = data.get("estado_base")
            origen = data.get("origen_estado")

            if not nombre:
                return False, "Falta nombre_estado"

            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO estado (nombre_estado, estado_base, origen_estado) VALUES (%s, %s, %s)",
                    (nombre, base, origen)
                )
            return True, "Estado creado"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def get_all_estados():
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM estado")
                return cursor.fetchall()
        finally:
            conn.close()

    @staticmethod
    def get_estado_by_id(id_estado):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM estado WHERE id_estado = %s", (id_estado,))
                return cursor.fetchone()
        finally:
            conn.close()

    @staticmethod
    def update_estado(id_estado, data):
        try:
            nombre = data.get("nombre_estado")
            base = data.get("estado_base")
            origen = data.get("origen_estado")

            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE estado SET nombre_estado=%s, estado_base=%s, origen_estado=%s WHERE id_estado=%s",
                    (nombre, base, origen, id_estado)
                )
                if cursor.rowcount == 0:
                    return False, "Estado no encontrado"
            return True, "Estado actualizado"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def delete_estado(id_estado):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM estado WHERE id_estado = %s", (id_estado,))
                if cursor.rowcount == 0:
                    return False, "Estado no encontrado"
            return True, "Estado eliminado"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()
