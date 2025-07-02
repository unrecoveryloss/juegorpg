from flask import Blueprint, request, jsonify
from services.personaje_equipo_service import PersonajeEquipoService

personaje_equipo_bp = Blueprint('personaje_equipo_bp', __name__)

@personaje_equipo_bp.route('/', methods=['POST'])
def asignar_equipo():
    data = request.get_json()
    success, msg = PersonajeEquipoService.asignar_equipo(data)
    status = 201 if success else 400
    return jsonify({'success': success, 'message': msg}), status

@personaje_equipo_bp.route('/<int:id_personaje>', methods=['GET'])
def obtener_equipos(id_personaje):
    equipos = PersonajeEquipoService.obtener_equipos_personaje(id_personaje)
    return jsonify({'success': True, 'equipos': equipos})

@personaje_equipo_bp.route('/', methods=['DELETE'])
def eliminar_equipo():
    data = request.get_json()
    success, msg = PersonajeEquipoService.eliminar_equipo(data)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status
