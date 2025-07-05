import pymysql
import pymysql.cursors
import hashlib
from flask_jwt_extended import create_access_token
from config.db import get_connection
from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

class AuthService:

    @staticmethod
    def register(usuario, correo, contraseña, id_rol=1):
        hash_pass = hashlib.sha256(contraseña.encode()).hexdigest()
        try:
            conn = get_connection()
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("SELECT * FROM usuario WHERE nombre_usuario=%s OR correo_usuario=%s", (usuario, correo))
                if cursor.fetchone():
                    return False, "Usuario o correo ya registrados"

                cursor.execute(
                    "INSERT INTO usuario (nombre_usuario, correo_usuario, contraseña_usuario, id_rol) VALUES (%s, %s, %s, %s)",
                    (usuario, correo, hash_pass, id_rol)
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
                    # Crear token JWT con información del usuario como string
                    user_data = f"{user['nombre_usuario']}:{user['id_rol']}"
                    token = create_access_token(identity=user_data)
                    return True, {'user': user, 'token': token}
                else:
                    return False, "Credenciales inválidas"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def verify_role(required_role):
        """Decorador para verificar el rol del usuario"""
        def decorator(f):
            @wraps(f)
            @jwt_required()
            def decorated_function(*args, **kwargs):
                current_user = get_jwt_identity()
                # Parsear el string "usuario:rol" para obtener el rol
                user_parts = current_user.split(':')
                if len(user_parts) != 2 or int(user_parts[1]) != required_role:
                    return jsonify({'success': False, 'message': 'Acceso denegado'}), 403
                return f(*args, **kwargs)
            return decorated_function
        return decorator
