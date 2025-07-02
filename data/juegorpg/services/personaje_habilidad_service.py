from models.personaje_habilidad_model import PersonajeHabilidadModel

class PersonajeHabilidadService:
    @staticmethod
    def asignar_habilidad(data):
        id_personaje = data.get('id_personaje')
        id_habilidad = data.get('id_habilidad')
        if not id_personaje or not id_habilidad:
            return False, "Faltan datos"
        return PersonajeHabilidadModel.asignar_habilidad(id_personaje, id_habilidad)

    @staticmethod
    def obtener_habilidades_personaje(id_personaje):
        return PersonajeHabilidadModel.obtener_habilidades_personaje(id_personaje)

    @staticmethod
    def eliminar_habilidad(data):
        id_personaje = data.get('id_personaje')
        id_habilidad = data.get('id_habilidad')
        if not id_personaje or not id_habilidad:
            return False, "Faltan datos"
        return PersonajeHabilidadModel.eliminar_habilidad_personaje(id_personaje, id_habilidad)
