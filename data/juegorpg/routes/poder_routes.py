from flask import Blueprint, request, jsonify
from services.poder_service import PoderService

poder_bp = Blueprint('poder_bp', __name__)

@poder_bp.route('/poderes', methods=['POST'])
def create_poder():
    data = request.get_json()
    success, msg = PoderService.create_poder(data)
    status = 201 if success else 400
    return jsonify({'success': success, 'message': msg}), status

@poder_bp.route('/poderes', methods=['GET'])
def get_all_poderes():
    poderes = PoderService.get_all_poderes()
    return jsonify({'success': True, 'poderes': poderes})

@poder_bp.route('/poderes/<int:id>', methods=['GET'])
def get_poder(id):
    poder = PoderService.get_poder_by_id(id)
    if poder:
        return jsonify({'success': True, 'poder': poder})
    return jsonify({'success': False, 'message': 'Poder no encontrado'}), 404

@poder_bp.route('/poderes/<int:id>', methods=['PUT'])
def update_poder(id):
    data = request.get_json()
    success, msg = PoderService.update_poder(id, data)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status

@poder_bp.route('/poderes/<int:id>', methods=['DELETE'])
def delete_poder(id):
    success, msg = PoderService.delete_poder(id)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status
