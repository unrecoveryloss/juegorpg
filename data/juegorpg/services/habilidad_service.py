from models.habilidad_model import HabilidadModel

class HabilidadService:
    @staticmethod
    def create_habilidad(data):
        return HabilidadModel.create_habilidad(data)

    @staticmethod
    def get_all_habilidades():
        return HabilidadModel.get_all_habilidades()

    @staticmethod
    def get_habilidad_by_id(id_habilidad):
        return HabilidadModel.get_habilidad_by_id(id_habilidad)

    @staticmethod
    def update_habilidad(id_habilidad, data):
        return HabilidadModel.update_habilidad(id_habilidad, data)

    @staticmethod
    def delete_habilidad(id_habilidad):
        return HabilidadModel.delete_habilidad(id_habilidad)
