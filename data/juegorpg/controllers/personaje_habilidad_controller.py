from flask import Blueprint, request, jsonify
from services.personaje_habilidad_service import PersonajeHabilidadService

personaje_habilidad_bp = Blueprint('personaje_habilidad_bp', __name__)

@personaje_habilidad_bp.route('/personajes/<int:id_personaje>/habilidades', methods=['POST'])
def asignar_habilidad(id_personaje):
    data = request.get_json()
    id_habilidad = data.get('id_habilidad')
    if not id_habilidad:
        return jsonify({'success': False, 'message': 'Falta id_habilidad'}), 400

    success, msg = PersonajeHabilidadService.asignar_habilidad(id_personaje, id_habilidad)
    status = 201 if success else 400
    return jsonify({'success': success, 'message': msg}), status

@personaje_habilidad_bp.route('/personajes/<int:id_personaje>/habilidades', methods=['GET'])
def obtener_habilidades(id_personaje):
    habilidades = PersonajeHabilidadService.obtener_habilidades_personaje(id_personaje)
    return jsonify({'success': True, 'habilidades': habilidades})

@personaje_habilidad_bp.route('/personajes/<int:id_personaje>/habilidades/<int:id_habilidad>', methods=['DELETE'])
def eliminar_habilidad(id_personaje, id_habilidad):
    success, msg = PersonajeHabilidadService.eliminar_habilidad_personaje(id_personaje, id_habilidad)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status
