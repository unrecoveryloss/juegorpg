from flask import Blueprint, request, jsonify
from services.character_service import CharacterService
from services.auth_service import AuthService

character_bp = Blueprint('character_bp', __name__)

@character_bp.route('', methods=['POST'])  # POST /characters
def create_character():
    data = request.get_json()
    success, msg = CharacterService.create_character(data)
    status = 201 if success else 400
    return jsonify({'success': success, 'message': msg}), status

@character_bp.route('', methods=['GET'])  # GET /characters
def get_characters():
    characters = CharacterService.get_all_characters()
    return jsonify({'success': True, 'characters': characters})

@character_bp.route('/admin/all', methods=['GET'])  # GET /characters/admin/all
@AuthService.verify_role(2)  # Solo administradores
def get_all_characters_admin():
    characters = CharacterService.get_all_characters()
    return jsonify({'success': True, 'characters': characters, 'admin_view': True})

@character_bp.route('/<int:id>', methods=['GET'])  # GET /characters/1
def get_character(id):
    character = CharacterService.get_character_by_id(id)
    if character:
        return jsonify({'success': True, 'character': character})
    return jsonify({'success': False, 'message': 'Personaje no encontrado'}), 404

@character_bp.route('/my-characters', methods=['GET'])  # GET /characters/my-characters
@AuthService.verify_role(1)  # Usuarios normales
def get_my_characters():
    from flask_jwt_extended import get_jwt_identity
    current_user = get_jwt_identity()
    # Parsear el string "usuario:rol" para obtener el usuario
    user_name = current_user.split(':')[0]
    user_characters = CharacterService.get_characters_by_user(user_name)
    return jsonify({'success': True, 'characters': user_characters})

@character_bp.route('/<int:id>', methods=['PUT'])  # PUT /characters/1
def update_character(id):
    data = request.get_json()
    success, msg = CharacterService.update_character(id, data)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status

@character_bp.route('/<int:id>', methods=['DELETE'])  # DELETE /characters/1
@AuthService.verify_role(2)  # Solo administradores pueden eliminar
def delete_character(id):
    success, msg = CharacterService.delete_character(id)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status
