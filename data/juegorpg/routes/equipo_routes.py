from flask import Blueprint
from controllers.equipo_controller import EquipoController

equipo_bp = Blueprint('equipo_bp', __name__)

equipo_bp.route('/equipos', methods=['POST'])(EquipoController.create_equipo)
equipo_bp.route('/equipos', methods=['GET'])(EquipoController.get_all_equipos)
equipo_bp.route('/equipos/<int:id_equipo>', methods=['GET'])(EquipoController.get_equipo_by_id)
equipo_bp.route('/equipos/<int:id_equipo>', methods=['PUT'])(EquipoController.update_equipo)
equipo_bp.route('/equipos/<int:id_equipo>', methods=['DELETE'])(EquipoController.delete_equipo)
