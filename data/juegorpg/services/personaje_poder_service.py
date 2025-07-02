from models.personaje_poder_model import PersonajePoderModel

class PersonajePoderService:
    @staticmethod
    def asignar_poder(data):
        id_personaje = data.get('id_personaje')
        id_poder = data.get('id_poder')
        if not id_personaje or not id_poder:
            return False, "Faltan datos necesarios"
        return PersonajePoderModel.asignar_poder(id_personaje, id_poder)

    @staticmethod
    def obtener_poderes_personaje(id_personaje):
        return PersonajePoderModel.obtener_poderes_personaje(id_personaje)

    @staticmethod
    def eliminar_poder(data):
        id_personaje = data.get('id_personaje')
        id_poder = data.get('id_poder')
        if not id_personaje or not id_poder:
            return False, "Faltan datos necesarios"
        return PersonajePoderModel.eliminar_poder_personaje(id_personaje, id_poder)
