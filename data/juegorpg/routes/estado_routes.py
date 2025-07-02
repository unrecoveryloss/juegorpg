from flask import Blueprint, request, jsonify
from services.estado_service import EstadoService

estado_bp = Blueprint('estado_bp', __name__)

@estado_bp.route('', methods=['POST'])
def create_estado():
    data = request.get_json()
    success, msg = EstadoService.create_estado(data)
    status = 201 if success else 400
    return jsonify({'success': success, 'message': msg}), status

@estado_bp.route('', methods=['GET'])
def get_estados():
    estados = EstadoService.get_all_estados()
    return jsonify({'success': True, 'estados': estados})

@estado_bp.route('/<int:id>', methods=['GET'])
def get_estado(id):
    estado = EstadoService.get_estado_by_id(id)
    if estado:
        return jsonify({'success': True, 'estado': estado})
    return jsonify({'success': False, 'message': 'Estado no encontrado'}), 404

@estado_bp.route('/<int:id>', methods=['PUT'])
def update_estado(id):
    data = request.get_json()
    success, msg = EstadoService.update_estado(id, data)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status

@estado_bp.route('/<int:id>', methods=['DELETE'])
def delete_estado(id):
    success, msg = EstadoService.delete_estado(id)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status
