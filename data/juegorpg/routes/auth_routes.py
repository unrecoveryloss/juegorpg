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


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')
    
    if not all([usuario, contraseña]):
        return jsonify({'success': False, 'message': 'Faltan datos'}), 400

    success, result = AuthService.login(usuario, contraseña)
    if success:
        return jsonify({'success': True, 'user': result}), 200
    else:
        return jsonify({'success': False, 'message': result}), 401
