from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth_bp
from routes.character_routes import character_bp
from routes.estado_routes import estado_bp
from routes.raza_routes import raza_bp
from routes.habilidad_routes import habilidad_bp
from routes.poder_routes import poder_bp
from routes.equipo_routes import equipo_bp
from routes.personaje_habilidad_routes import personaje_habilidad_bp
from routes.personaje_poder_routes import personaje_poder_bp
from routes.personaje_equipo_routes import personaje_equipo_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(character_bp, url_prefix='/characters')  
app.register_blueprint(estado_bp, url_prefix='/estado')
app.register_blueprint(raza_bp, url_prefix='/raza')
app.register_blueprint(habilidad_bp, url_prefix='/habilidades')
app.register_blueprint(poder_bp, url_prefix='/poderes')
app.register_blueprint(equipo_bp, url_prefix='/equipo')
app.register_blueprint(personaje_habilidad_bp, url_prefix='/personaje-habilidad')
app.register_blueprint(personaje_poder_bp, url_prefix='/personaje-poder')
app.register_blueprint(personaje_equipo_bp, url_prefix='/personaje-equipo')

if __name__ == '__main__':
    app.run(debug=True)

    
