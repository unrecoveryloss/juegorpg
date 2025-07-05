from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    usuario = data.get('usuario')
    correo = data.get('correo')
    contraseña = data.get('contraseña')
    
    if not all([usuario, correo, contraseña]):
        return jsonify({'success': False, 'message': 'Faltan datos'}), 400

    success, msg = AuthService.register(usuario, correo, contraseña)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status


@auth_bp.route('/register/admin', methods=['POST'])
def register_admin():
    data = request.get_json()
    usuario = data.get('usuario')
    correo = data.get('correo')
    contraseña = data.get('contraseña')
    
    if not all([usuario, correo, contraseña]):
        return jsonify({'success': False, 'message': 'Faltan datos'}), 400

    # id_rol = 2 para administrador
    success, msg = AuthService.register(usuario, correo, contraseña, id_rol=2)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')
    
    if not all([usuario, contraseña]):
        return jsonify({'success': False, 'message': 'Faltan datos'}), 400

    success, result = AuthService.login(usuario, contraseña)
    if success:
        # Ignorar el error del linter - sabemos que result es un diccionario
        return jsonify({
            'success': True, 
            'user': result['user'],  # type: ignore
            'token': result['token']  # type: ignore
        }), 200
    else:
        return jsonify({'success': False, 'message': result}), 401
