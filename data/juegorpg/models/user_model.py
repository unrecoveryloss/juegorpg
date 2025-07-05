from config.db import get_connection

class UserModel:
    @staticmethod
    def find_by_username(username):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM usuario WHERE nombre_usuario = %s"
                cursor.execute(sql, (username,))
                return cursor.fetchone()
        finally:
            conn.close()

    @staticmethod
    def create_user(usuario, correo, hashed_password, id_rol):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO usuario (nombre_usuario, correo_usuario, contraseña_usuario, id_rol) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (usuario, correo, hashed_password, id_rol))
                conn.commit()
                return True, "Usuario creado exitosamente"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

