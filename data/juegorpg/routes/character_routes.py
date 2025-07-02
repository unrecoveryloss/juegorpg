from flask import Blueprint, request, jsonify
from services.character_service import CharacterService

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

@character_bp.route('/<int:id>', methods=['GET'])  # GET /characters/1
def get_character(id):
    character = CharacterService.get_character_by_id(id)
    if character:
        return jsonify({'success': True, 'character': character})
    return jsonify({'success': False, 'message': 'Personaje no encontrado'}), 404

@character_bp.route('/<int:id>', methods=['PUT'])  # PUT /characters/1
def update_character(id):
    data = request.get_json()
    success, msg = CharacterService.update_character(id, data)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status

@character_bp.route('/<int:id>', methods=['DELETE'])  # DELETE /characters/1
def delete_character(id):
    success, msg = CharacterService.delete_character(id)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status
