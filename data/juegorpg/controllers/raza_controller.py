from flask import request, jsonify
from services.raza_service import RazaService

class RazaController:
    @staticmethod
    def create():
        data = request.get_json()
        nombre_raza = data.get('nombre_raza')
        if not nombre_raza:
            return jsonify({'success': False, 'message': 'Falta nombre_raza'}), 400
        success, msg = RazaService.create_raza(nombre_raza)
        status = 201 if success else 400
        return jsonify({'success': success, 'message': msg}), status

    @staticmethod
    def get_all():
        razas = RazaService.get_all_razas()
        return jsonify({'success': True, 'razas': razas})

    @staticmethod
    def get_by_id(id_raza):
        raza = RazaService.get_raza_by_id(id_raza)
        if raza:
            return jsonify({'success': True, 'raza': raza})
        return jsonify({'success': False, 'message': 'Raza no encontrada'}), 404

    @staticmethod
    def update(id_raza):
        data = request.get_json()
        success, msg = RazaService.update_raza(id_raza, data)
        status = 200 if success else 400
        return jsonify({'success': success, 'message': msg}), status

    @staticmethod
    def delete(id_raza):
        success, msg = RazaService.delete_raza(id_raza)
        status = 200 if success else 400
        return jsonify({'success': success, 'message': msg}), status
