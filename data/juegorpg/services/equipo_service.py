from models.equipo_model import EquipoModel

class EquipoService:
    @staticmethod
    def create_equipo(data):
        nombre = data.get("nombre_equipo")
        descripcion = data.get("descripcion_equipo")
        origen = data.get("origen_equipo")

        if not nombre or not descripcion or not origen:
            return False, "Faltan datos obligatorios"

        return EquipoModel.create_equipo(nombre, descripcion, origen)

    @staticmethod
    def get_all_equipos():
        return EquipoModel.get_all_equipos()

    @staticmethod
    def get_equipo_by_id(id_equipo):
        return EquipoModel.get_equipo_by_id(id_equipo)

    @staticmethod
    def update_equipo(id_equipo, data):
        nombre = data.get("nombre_equipo")
        descripcion = data.get("descripcion_equipo")
        origen = data.get("origen_equipo")

        if not nombre or not descripcion or not origen:
            return False, "Faltan datos para actualizar"

        return EquipoModel.update_equipo(id_equipo, nombre, descripcion, origen)

    @staticmethod
    def delete_equipo(id_equipo):
        return EquipoModel.delete_equipo(id_equipo)
