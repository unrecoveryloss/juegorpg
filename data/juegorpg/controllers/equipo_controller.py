from flask import request, jsonify
from services.equipo_service import EquipoService

class EquipoController:
    @staticmethod
    def create_equipo():
        data = request.get_json()
        success, msg = EquipoService.create_equipo(data)
        status = 201 if success else 400
        return jsonify({'success': success, 'message': msg}), status

    @staticmethod
    def get_all_equipos():
        equipos = EquipoService.get_all_equipos()
        return jsonify({'success': True, 'equipos': equipos})

    @staticmethod
    def get_equipo_by_id(id_equipo):
        equipo = EquipoService.get_equipo_by_id(id_equipo)
        if equipo:
            return jsonify({'success': True, 'equipo': equipo})
        return jsonify({'success': False, 'message': 'Equipo no encontrado'}), 404

    @staticmethod
    def update_equipo(id_equipo):
        data = request.get_json()
        success, msg = EquipoService.update_equipo(id_equipo, data)
        status = 200 if success else 400
        return jsonify({'success': success, 'message': msg}), status

    @staticmethod
    def delete_equipo(id_equipo):
        success, msg = EquipoService.delete_equipo(id_equipo)
        status = 200 if success else 400
        return jsonify({'success': success, 'message': msg}), status
