# Archivo modificado: services/personaje_equipo_service.py
from models.personaje_equipo_model import PersonajeEquipoModel

class PersonajeEquipoService:
    @staticmethod
    def asignar_equipo(data):
        id_personaje = data.get("id_personaje")
        id_equipo = data.get("id_equipo")

        if not id_personaje or not id_equipo:
            return False, "Faltan datos"

        return PersonajeEquipoModel.asignar_equipo(id_personaje, id_equipo)

    @staticmethod
    def obtener_equipos_personaje(id_personaje):
        return PersonajeEquipoModel.obtener_equipos_personaje(id_personaje)

    @staticmethod
    def eliminar_equipo(data):
        id_personaje = data.get("id_personaje")
        id_equipo = data.get("id_equipo")

        if not id_personaje or not id_equipo:
            return False, "Faltan datos"

        return PersonajeEquipoModel.eliminar_equipo_personaje(id_personaje, id_equipo)
