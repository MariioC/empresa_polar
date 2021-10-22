from typing import Tuple
from flask import Blueprint, jsonify, request
from datetime import datetime
import calendar

# Controllers
import controllers.retroalimentacionesController as retroalimentacionesController
import controllers.usuariosController as usuariosController

# Json Web Token
from jwt_helpers import verificarToken, verificarRol, identificarUsuario

retroalimentacionesRoutes = Blueprint('retroalimentacionesRoutes', __name__)

@retroalimentacionesRoutes.route('/<id_usuario>', methods=['POST'])
@verificarToken
def registrarRetroalimentacion(id_usuario):
    try:

        json_data = request.json

        puntaje = json_data['puntaje']
        fecha_retroalimentacion = json_data['fecha_retroalimentacion']
        retroalimentacion = json_data['retroalimentacion']

        usuario = usuariosController.getUsuario(id_usuario)
        if usuario is not None:

            if not verificarRol(request, 'A') and not verificarRol(request, 'SA'):   
                return jsonify({ 'error': 'Permisos insuficientes para realizar retroalimentacion al usuario' })
                
            if usuario['info_personal']['rol'] == 'A' or usuario['info_personal']['rol'] == 'SA':
                if not verificarRol(request, 'SA'):
                    return jsonify({ 'error': 'Permisos insuficientes para realizar retroalimentaciones a este rol' })

            sesion_usuario = identificarUsuario(request)

            fecha = datetime.strptime(fecha_retroalimentacion, '%Y-%m-%d')
            str_fecha = fecha.strftime('%Y-%m-%d')

            mes = f'0{fecha.month}' if fecha.month <= 9 else f'{fecha.month}'

            fecha_inicial = f'{fecha.year}-{mes}-01'
            fecha_final = f'{fecha.year}-{mes}-{calendar.monthrange(fecha.year, fecha.month)[1]}'

            if retroalimentacionesController.comrpobarRetroalimentacion(fecha_inicial, fecha_final, usuario['info_personal']['id_usuario']) is not None:
                return jsonify({
                    'error': 'El usuario ya tiene una retroalimentación para el mes especificado',
                })

            id_retroalimentacion = retroalimentacionesController.registrarRetroalimentacion(puntaje, str_fecha, retroalimentacion, usuario['info_personal']['id_usuario'], sesion_usuario['id_usuario'])

            retroalimentacion = retroalimentacionesController.getRetroalimentacion(id_retroalimentacion)
            
            return jsonify({
                'mensaje': 'Se ha registrado la retroalimentación al usuario',
                'retroalimentacion' : retroalimentacion
            })

        else:
            return jsonify({
                'error': 'Ocurrió un error al cargar la información del usuario',
            })
    except Exception as error:
        print("Error en retroalimentacionesRoutes.registrarRetroalimentacion: ", error)
        return jsonify({
            'error': 'Ocurrió un error inesperado al registrar la retroalimentación',
        })

@retroalimentacionesRoutes.route('/<id_retroalimentacion>', methods=['PUT'])
@verificarToken
def actualizarRetroalimentacion(id_retroalimentacion):
    try:
        json_data = request.json

        puntaje = json_data['puntaje']
        retroalimentacion = json_data['retroalimentacion']

        db_retroalimentacion = retroalimentacionesController.getRetroalimentacion(id_retroalimentacion)
       
        if db_retroalimentacion is not None:

            usuario = usuariosController.getUsuario(db_retroalimentacion['id_usuario'])
            
            if usuario is not None:

                if not verificarRol(request, 'A') and not verificarRol(request, 'SA'):
                    return jsonify({ 'error': 'Permisos insuficientes para actualizar retroalimentaciones' })
                    
                if usuario['info_personal']['rol'] == 'A' or usuario['info_personal']['rol'] == 'SA':
                    if not verificarRol(request, 'SA'):
                        return jsonify({ 'error': 'Permisos insuficientes para actualizar retroalimentaciones a este rol' })
                
                session_usuario = identificarUsuario(request)

                if retroalimentacionesController.actualizarRetroalimentacion(puntaje, retroalimentacion, session_usuario['id_usuario'], id_retroalimentacion) is True:

                    new_retroalimentacion = retroalimentacionesController.getRetroalimentacion(id_retroalimentacion)
                    
                    return jsonify({
                        'mensaje': 'Se ha actualizado la retroalimentación correctamente',
                        'retroalimentacion': new_retroalimentacion
                    })
                else:
                    return jsonify({
                        'error': 'No se ha podido actualizar la retroalimentación',
                    })
            else:
                return jsonify({
                    'error': 'No se ha podido obtener la información del usuario perteneciente a la retroalimentación',
                })
        else:
            return jsonify({
                'error': 'La retroalimentación que desea actualizar no existe',
            })
    except Exception as error:
        print("Error en retroalimentacionesRoutes.actualizarRetroalimentacion: ", error)
        return jsonify({
            'error': 'Ocurrió un error inesperado al actualizar la retroalimentación',
        })

@retroalimentacionesRoutes.route('/<id_retroalimentacion>', methods=['DELETE'])
@verificarToken
def eliminarRetroalimentacion(id_retroalimentacion):
    try:
        if not verificarRol(request, 'A') and not verificarRol(request, 'SA'):   
            return jsonify({ 'error': 'Permisos insuficientes para realizar esta acción' })
        
        if retroalimentacionesController.eliminarRetroalimentacion(id_retroalimentacion) is True:
            return jsonify({
                'mensaje': 'Se ha eliminado la retroalimentación correctamente'
            })
        else:
            return jsonify({
                'error': 'No se ha podido eliminar la retroalimentación',
            })
    except Exception as error:
        print("Error en retroalimentacionesRoutes.eliminarRetroalimentacion: ", error)
        return jsonify({
            'error': 'Ocurrió un error inesperado al eliminar la retroalimentación',
        })

@retroalimentacionesRoutes.route('/retroalimentacion/<id_retroalimentacion>')
@verificarToken
def obtenerRetroalimentacion(id_retroalimentacion):
    try:

        retroalimentacion = retroalimentacionesController.getRetroalimentacion(id_retroalimentacion)

        return jsonify({
            'mensaje': 'Se retornará la retroalimentación con id: {0}'.format(id_retroalimentacion),
            'retroalimentacion': retroalimentacion
        })
    except Exception as error:
        print("Error en retroalimentacionesRoutes.obtenerRetroalimentacion: ", error)
        return jsonify({
            'error': 'Ocurrió un error inesperado al obtener la retroalimentación deseada',
        })

@retroalimentacionesRoutes.route('/')
@retroalimentacionesRoutes.route('/<id_usuario>')
@verificarToken
def obtenerRetroalimentaciones(id_usuario = None):
    try:
        if not verificarRol(request, 'A') and not verificarRol(request, 'SA'):
            id_usuario = None

        if id_usuario is not None:
            retroalimentaciones = retroalimentacionesController.getRetroalimentaciones(id_usuario)
            return jsonify({
                'mensaje': 'Se retornan las retroalimentaciones del usuario con id: {0}'.format(id_usuario),
                'retroalimentaciones': retroalimentaciones
            })
        else:
            session_usuario = identificarUsuario(request)
            retroalimentaciones = retroalimentacionesController.getRetroalimentaciones(session_usuario['id_usuario'])
            return jsonify({
                'mensaje': 'Se retornan las retroalimentaciones del usuario con la sesión activa',
                'retroalimentaciones': retroalimentaciones
            })

    except Exception as error:
        print("Error en retroalimentacionesRoutes.obtenerRetroalimentaciones: ", error)
        return jsonify({
            'error': 'Ocurrió un error inesperado al obtener las retroalimentaciones',
        })