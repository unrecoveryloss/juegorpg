# juegorpg
Evaluación 4 de appdev, juego rpg

# como instalar dependencias 
pip install -r requirements.txt

# ejecutar proyecto local desde la terminal python de vscode CON WAMP INICIADO
una vez abierta la carpeta del proyecto, ejecutar comandos en este orden: 

cd .\juegorpg\
cd .\data\
cd .\juegorpg\
python .\main.py

esto iniciará el servidor de flask, por lo que luego continuaremos hacia postman
para interactuar con el backend

descripción de la interfaz ,---
FALTA ESTO

# Base de datos

script /sql/init_db

# registro
curl -X POST --location 'http://127.0.0.1:5000/auth/register' \
--header 'Content-Type: application/json' \
--data-raw '{
  "usuario": "miusuario",
  "correo": "micorreo@dominio.com",
  "contraseña": "miclave123"
}'



# login 

curl -X POST --location 'http://127.0.0.1:5000/auth/login' \
--header 'Content-Type: application/json' \
--data '{
  "usuario": "miusuario",
  "contraseña": "miclave123"
}'


# Wampserver
para descargar
https://sourceforge.net/projects/wampserver/files/WampServer%203/WampServer%203.0.0/wampserver3.3.7_x64.exe/download
si faltan dependencias para la instalación de wampserver, instalar desde aquí
https://wampserver.aviatechno.net/
VC++ Packages, buscar según se indique
