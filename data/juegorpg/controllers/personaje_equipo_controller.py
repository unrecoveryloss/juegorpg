from flask import request, jsonify
from services.personaje_equipo_service import PersonajeEquipoService

def asignar_equipo():
    data = request.get_json()
    success, msg = PersonajeEquipoService.asignar_equipo(data)
    status = 201 if success else 400
    return jsonify({'success': success, 'message': msg}), status

def obtener_equipos(id_personaje):
    equipos = PersonajeEquipoService.obtener_equipos_por_personaje(id_personaje)
    return jsonify({'success': True, 'equipos': equipos})

def eliminar_equipo():
    data = request.get_json()
    success, msg = PersonajeEquipoService.eliminar_equipo(data)
    status = 200 if success else 400
    return jsonify({'success': success, 'message': msg}), status
