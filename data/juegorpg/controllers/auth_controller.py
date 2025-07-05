from services.auth_service import AuthService

class AuthController:
    @staticmethod
    def register(data):
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        id_rol = data.get('id_rol', 1)  

        success, message = AuthService.register(username, email, password, id_rol)
        return {'success': success, 'message': message}

    @staticmethod
    def login(data):
        username = data.get('username')
        password = data.get('password')
        success, result = AuthService.login(username, password)
        if success:
            return {'success': True, 'user': result}
        else:
            return {'success': False, 'message': result}
