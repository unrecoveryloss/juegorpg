from flask import Blueprint, request, jsonify
from services.habilidad_service import HabilidadService

habilidad_bp = Blueprint('habilidad_bp', __name__)

@habilidad_bp.route('/habilidades', methods=['POST'])
def create_habilidad():
    data = request.get_json()
    success, msg = HabilidadService.create_habilidad(data)
    status = 201 if success else 400
    return jsonify({'success': success, 'message': msg}), status

@habilidad_bp.route('/habilidades', methods=['GET'])
def get_habilidades():
    habilidades = HabilidadService.get_all_habilidades()
    return jsonify({'success': True, 'habilidades': habilidades})

@habilidad_bp.route('/habilidades/<int:id>', methods=['GET'])
def get_habilidad(id):
    habilidad = HabilidadService.get_habilidad_by_id(id)
    if habilidad:
        return jsonify({'success': True, 'habilidad': habilidad})
    return jsonify({'success': False, 'message': 'Habilidad no encontrada'}), 404

@habilidad_bp.route('/habilidades/<int:id>', methods=['PUT'])
def update_habilidad(id):
    data = request.get_json()
    success, msg = HabilidadService.update_habilidad(id, data)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status

@habilidad_bp.route('/habilidades/<int:id>', methods=['DELETE'])
def delete_habilidad(id):
    success, msg = HabilidadService.delete_habilidad(id)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status
