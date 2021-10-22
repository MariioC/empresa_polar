from flask import jsonify, request;
from functools import wraps

import config

# JWT
import jwt

def crearToken(payload):
    try:
        token = jwt.encode(payload, config.SECRET_KEY, algorithm = 'HS256')
        if isinstance(token, str) is True:
            return token
        else:
            return token.decode('utf-8')
    except Exception as error:
        print('ERROR al crear el token: ', error)
        return None

def verificarToken(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token:
            return jsonify({ 'error' : 'Inicie sesión para realizar esta acción'})

        try:
            data = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
        except Exception as error:
            print('ERROR al verificarToken: ', error)
            return jsonify({ 'error': 'Error en la sesión actual. \n Inicie sesión nuevamente.' })
        return func(*args, **kwargs)
    return wrapped

def identificarUsuario(request):
    token = request.headers.get('Authorization')
        
    if not token:
        return jsonify({ 'error' : 'No tiene una sesión activa'})
        
    try:
        return jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
    except Exception as error:
        print('ERROR al identificar usuario con el token: ', error)
        return jsonify({ 'error': 'Error en la sesión actual \n Inicie sesión nuevamente' })

def verificarRol(request, rol):
    usuario = identificarUsuario(request)
    if usuario['rol'] == rol:
        return True
    else:
        return False
        # return jsonify({ 'error': 'Solo el rol "Superadministrador" puede realizar esta acción' })