import pymysql
import pymysql.cursors
from config.db import get_connection

class UserService:
    
    @staticmethod
    def get_all_users():
        """Obtener todos los usuarios con información de rol"""
        try:
            conn = get_connection()
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("""
                    SELECT u.id_usuario, u.nombre_usuario, u.correo_usuario, 
                           r.nombre_rol, u.id_rol
                    FROM usuario u
                    JOIN rol r ON u.id_rol = r.id_rol
                    ORDER BY u.id_usuario
                """)
                return cursor.fetchall()
        except Exception as e:
            return []
        finally:
            conn.close()
    
    @staticmethod
    def get_user_by_id(user_id):
        """Obtener usuario por ID"""
        try:
            conn = get_connection()
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("""
                    SELECT u.id_usuario, u.nombre_usuario, u.correo_usuario, 
                           r.nombre_rol, u.id_rol
                    FROM usuario u
                    JOIN rol r ON u.id_rol = r.id_rol
                    WHERE u.id_usuario = %s
                """, (user_id,))
                return cursor.fetchone()
        except Exception as e:
            return None
        finally:
            conn.close()
    
    @staticmethod
    def update_user(user_id, data):
        """Actualizar usuario"""
        nombre_usuario = data.get('nombre_usuario')
        correo_usuario = data.get('correo_usuario')
        id_rol = data.get('id_rol')
        
        if not all([nombre_usuario, correo_usuario, id_rol]):
            return False, "Faltan datos obligatorios"
        
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                # Verificar si el usuario existe
                cursor.execute("SELECT id_usuario FROM usuario WHERE id_usuario = %s", (user_id,))
                if not cursor.fetchone():
                    return False, "Usuario no encontrado"
                
                # Verificar si el rol existe
                cursor.execute("SELECT id_rol FROM rol WHERE id_rol = %s", (id_rol,))
                if not cursor.fetchone():
                    return False, "Rol no válido"
                
                # Verificar si el nombre de usuario o correo ya existe en otro usuario
                cursor.execute("""
                    SELECT id_usuario FROM usuario 
                    WHERE (nombre_usuario = %s OR correo_usuario = %s) 
                    AND id_usuario != %s
                """, (nombre_usuario, correo_usuario, user_id))
                if cursor.fetchone():
                    return False, "Nombre de usuario o correo ya existe"
                
                # Actualizar usuario
                cursor.execute("""
                    UPDATE usuario 
                    SET nombre_usuario = %s, correo_usuario = %s, id_rol = %s
                    WHERE id_usuario = %s
                """, (nombre_usuario, correo_usuario, id_rol, user_id))
                conn.commit()
                return True, "Usuario actualizado exitosamente"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()
    
    @staticmethod
    def delete_user(user_id):
        """Eliminar usuario"""
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                # Verificar si el usuario existe
                cursor.execute("SELECT id_usuario FROM usuario WHERE id_usuario = %s", (user_id,))
                if not cursor.fetchone():
                    return False, "Usuario no encontrado"
                
                # Verificar si el usuario tiene personajes
                cursor.execute("SELECT id_personaje FROM personaje WHERE id_usuario = %s", (user_id,))
                if cursor.fetchone():
                    return False, "No se puede eliminar usuario con personajes asociados"
                
                # Eliminar usuario
                cursor.execute("DELETE FROM usuario WHERE id_usuario = %s", (user_id,))
                conn.commit()
                return True, "Usuario eliminado exitosamente"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close() 