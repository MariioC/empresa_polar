from flask import Flask, jsonify, send_from_directory, __path__
from flask_cors import CORS
import os

# AAgrego la ruta donde tengo todo el proyecto
import sys
sys.path.append('./src/')

# Importación los modulos de rutas
from routes.usuarios import usuariosRoutes
from routes.retroalimentaciones import retroalimentacionesRoutes
from routes.dependencias import dependenciasRoutes

from jwt_helpers import verificarToken, identificarUsuario

# app = Flask(__name__, static_url_path='', 
#                       static_folder='dist/',
#                       template_folder='dist/')

app = Flask(__name__, static_url_path='',
                      static_folder='dist/',
                      template_folder='dist/')

# Registro los modulos
app.register_blueprint(usuariosRoutes, url_prefix="/api/usuarios")
app.register_blueprint(dependenciasRoutes, url_prefix="/api/dependencias")
app.register_blueprint(retroalimentacionesRoutes, url_prefix="/api/retroalimentaciones")

# CROSS ORIGIN - PARA QUE FUNCIONE LA API CORRECTAMENTE
CORS(app)

@app.route('/')
def root():
    print('ENTRA')
    return app.send_static_file('index.html')

# @app.route('/')
# def send_file():
#     print(app.root_path+'/dist/')
#     return send_from_directory(app.root_path+'/dist/', 'Inicio')
    # return jsonify({ 'mensaje' : 'Hola'})

# @app.route('/')
# def index():
#     return '<h1 style="text-align: center;">Bienvenido a la API de EMPRESA POLAR</h1>';

@app.errorhandler(404)
def NotFound(error):
    return jsonify({ 'error' : 'La ruta especificada no existe dentro de la API' });

if __name__ == '__main__':
    app.run(debug=True)