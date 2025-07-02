from flask import Blueprint, request, jsonify
from services.personaje_poder_service import PersonajePoderService

personaje_poder_bp = Blueprint('personaje_poder_bp', __name__)

@personaje_poder_bp.route('/', methods=['POST'])
def asignar_poder():
    data = request.get_json()
    success, msg = PersonajePoderService.asignar_poder(data)
    status = 201 if success else 400
    return jsonify({'success': success, 'message': msg}), status

@personaje_poder_bp.route('/<int:id_personaje>', methods=['GET'])
def obtener_poderes(id_personaje):
    poderes = PersonajePoderService.obtener_poderes_personaje(id_personaje)
    return jsonify({'success': True, 'poderes': poderes})

@personaje_poder_bp.route('/', methods=['DELETE'])
def eliminar_poder():
    data = request.get_json()
    success, msg = PersonajePoderService.eliminar_poder(data)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status
