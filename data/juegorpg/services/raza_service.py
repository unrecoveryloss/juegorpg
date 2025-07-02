from models.raza_model import RazaModel

class RazaService:
    @staticmethod
    def create_raza(nombre_raza):
        return RazaModel.create_raza(nombre_raza)

    @staticmethod
    def get_all_razas():
        return RazaModel.get_all_razas()

    @staticmethod
    def get_raza_by_id(id_raza):
        return RazaModel.get_raza_by_id(id_raza)

    @staticmethod
    def update_raza(id_raza, data):
        nombre_raza = data.get('nombre_raza')
        if not nombre_raza:
            return False, "Falta nombre_raza"
        
        # Verificar si ya existe otra raza con ese nombre y distinto id
        existing = RazaModel.get_raza_by_nombre(nombre_raza)
        if existing and existing['id_raza'] != id_raza:
            return False, "Ya existe una raza con ese nombre"
        
        return RazaModel.update_raza(id_raza, nombre_raza)

    @staticmethod
    def delete_raza(id_raza):
        return RazaModel.delete_raza(id_raza)
