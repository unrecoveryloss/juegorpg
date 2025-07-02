from flask import Blueprint, request, jsonify
from services.personaje_habilidad_service import PersonajeHabilidadService

personaje_habilidad_bp = Blueprint('personaje_habilidad_bp', __name__)

@personaje_habilidad_bp.route('/', methods=['POST'])
def asignar_habilidad():
    data = request.get_json()
    success, msg = PersonajeHabilidadService.asignar_habilidad(data)
    status = 201 if success else 400
    return jsonify({'success': success, 'message': msg}), status

@personaje_habilidad_bp.route('/<int:id_personaje>', methods=['GET'])
def obtener_habilidades(id_personaje):
    habilidades = PersonajeHabilidadService.obtener_habilidades_personaje(id_personaje)
    return jsonify({'success': True, 'habilidades': habilidades})

@personaje_habilidad_bp.route('/', methods=['DELETE'])
def eliminar_habilidad():
    data = request.get_json()
    success, msg = PersonajeHabilidadService.eliminar_habilidad(data)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status
