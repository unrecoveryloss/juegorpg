from flask import Blueprint, request, jsonify
from services.user_service import UserService
from services.auth_service import AuthService

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('', methods=['GET'])  # GET /users
@AuthService.verify_role(2)  # Solo administradores
def get_all_users():
    """Obtener todos los usuarios (solo admin)"""
    users = UserService.get_all_users()
    return jsonify({'success': True, 'users': users})

@user_bp.route('/<int:user_id>', methods=['GET'])  # GET /users/1
@AuthService.verify_role(2)  # Solo administradores
def get_user(user_id):
    """Obtener usuario específico (solo admin)"""
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify({'success': True, 'user': user})
    return jsonify({'success': False, 'message': 'Usuario no encontrado'}), 404

@user_bp.route('/<int:user_id>', methods=['PUT'])  # PUT /users/1
@AuthService.verify_role(2)  # Solo administradores
def update_user(user_id):
    """Actualizar usuario (solo admin)"""
    data = request.get_json()
    success, msg = UserService.update_user(user_id, data)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status

@user_bp.route('/<int:user_id>', methods=['DELETE'])  # DELETE /users/1
@AuthService.verify_role(2)  # Solo administradores
def delete_user(user_id):
    """Eliminar usuario (solo admin)"""
    success, msg = UserService.delete_user(user_id)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status 