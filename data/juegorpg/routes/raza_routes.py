from flask import Blueprint
from controllers.raza_controller import RazaController

raza_bp = Blueprint('raza_bp', __name__)

raza_bp.route('/razas', methods=['POST'])(RazaController.create)
raza_bp.route('/razas', methods=['GET'])(RazaController.get_all)
raza_bp.route('/razas/<int:id_raza>', methods=['GET'])(RazaController.get_by_id)
raza_bp.route('/razas/<int:id_raza>', methods=['PUT'])(RazaController.update)
raza_bp.route('/razas/<int:id_raza>', methods=['DELETE'])(RazaController.delete)
