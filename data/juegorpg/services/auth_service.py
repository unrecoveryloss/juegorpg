import pymysql
import hashlib
from config.db import get_connection

class AuthService:

    @staticmethod
    def register(usuario, correo, contraseña):
        hash_pass = hashlib.sha256(contraseña.encode()).hexdigest()
        try:
            conn = get_connection()
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("SELECT * FROM usuario WHERE nombre_usuario=%s OR correo_usuario=%s", (usuario, correo))
                if cursor.fetchone():
                    return False, "Usuario o correo ya registrados"

                cursor.execute(
                    "INSERT INTO usuario (nombre_usuario, correo_usuario, contraseña_usuario, id_rol) VALUES (%s, %s, %s, %s)",
                    (usuario, correo, hash_pass, 1)
                )
                conn.commit()
                return True, "¡Registro exitoso!"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def login(usuario, contraseña):
        hash_pass = hashlib.sha256(contraseña.encode()).hexdigest()
        try:
            conn = get_connection()
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("SELECT nombre_usuario, id_rol FROM usuario WHERE nombre_usuario=%s AND contraseña_usuario=%s",
                               (usuario, hash_pass))
                user = cursor.fetchone()
                if user:
                    return True, user
                else:
                    return False, "Credenciales inválidas"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()
