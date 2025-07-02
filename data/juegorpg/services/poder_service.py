from models.poder_model import PoderModel

class PoderService:
    @staticmethod
    def create_poder(data):
        nombre = data.get("nombre_poder")
        descripcion = data.get("descripcion_poder")
        origen = data.get("origen_poder")
        id_raza = data.get("id_raza")
        if not all([nombre, descripcion, origen, id_raza]):
            return False, "Faltan datos"
        return PoderModel.create_poder(nombre, descripcion, origen, id_raza)

    @staticmethod
    def get_all_poderes():
        return PoderModel.get_all_poderes()

    @staticmethod
    def get_poder_by_id(id_poder):
        return PoderModel.get_poder_by_id(id_poder)

    @staticmethod
    def update_poder(id_poder, data):
        nombre = data.get("nombre_poder")
        descripcion = data.get("descripcion_poder")
        origen = data.get("origen_poder")
        id_raza = data.get("id_raza")
        if not all([nombre, descripcion, origen, id_raza]):
            return False, "Faltan datos"
        return PoderModel.update_poder(id_poder, nombre, descripcion, origen, id_raza)

    @staticmethod
    def delete_poder(id_poder):
        return PoderModel.delete_poder(id_poder)
