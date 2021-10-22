from flask import Blueprint, jsonify, request

# Controlladores
import controllers.dependenciasController as dependenciasController

# Json Web Token
from jwt_helpers import verificarToken, verificarRol

dependenciasRoutes = Blueprint('dependenciasRoutes', __name__)

@dependenciasRoutes.route('/', methods=['POST'])
@verificarToken
def registrarDependencia():
    try:
        if not verificarRol(request, 'SA'):
            return jsonify({ 'error': 'Permisos insuficientes para registrar dependencias' })
        
        json_data = request.json

        data_dependencia = json_data['dependencia']
        nombre_dependencia = data_dependencia['nombre_dependencia']

        data_cargos = json_data['cargos']

        id_dependencia = dependenciasController.registrarDependencia(nombre_dependencia)

        if id_dependencia is not None:

            for cargo in data_cargos:
                dependenciasController.registrarCargo(cargo['nombre_cargo'], cargo['salario'], id_dependencia)

            dependencia = dependenciasController.getDependencia(id_dependencia)

            return jsonify({
                'mensaje': 'Se ha registrado la dependencia de manera correcta',
                'dependencia': dependencia
            })
        else:
            return jsonify({
                'error': 'Ocurrió un error inesperado al registrar la dependencia',
            })
    except Exception as error:
        print('ERROR: ', error)
        return jsonify({
            'error': 'Ocurrió un error inesperado al registrar la dependencia',
        })

@dependenciasRoutes.route('/', methods=['PUT'])
@verificarToken
def actualizarDependencia():
    try:
        if not verificarRol(request, 'SA'):
            return jsonify({ 'error': 'Permisos insuficientes para registrar dependencias' })
        
        json_data = request.json

        data_dependencia = json_data['dependencia']

        id_dependencia = data_dependencia['id_dependencia']
        nombre_dependencia = data_dependencia['nombre_dependencia']

        data_cargos = json_data['cargos']

        if id_dependencia is not None:

            if dependenciasController.actualizarDependencia(nombre_dependencia, id_dependencia) is True:

                for cargo in data_cargos:
                    if 'id_cargo' in cargo:
                        dependenciasController.actualizarCargo(cargo['nombre_cargo'], cargo['salario'], cargo['id_cargo'])
                    else:
                        dependenciasController.registrarCargo(cargo['nombre_cargo'], cargo['salario'], id_dependencia)

                dependencia = dependenciasController.getDependencia(id_dependencia)

                return jsonify({
                    'mensaje': 'Se ha actualizado la dependencia de manera correcta',
                    'dependencia': dependencia
                })
            else:
                return jsonify({
                    'error': 'No se ha podido actualizar la dependencia',
                })
        else:
            return jsonify({
                'error': 'Ocurrió un error inesperado al actualizar la dependencia',
            })
    except Exception as error:
        print('ERROR: ', error)
        return jsonify({
            'error': 'Ocurrió un error inesperado al actualizar la dependencia',
        })

@dependenciasRoutes.route('/', methods=['GET'])
@dependenciasRoutes.route('/<id_dependencia>', methods=['GET'])
@verificarToken
def obtenerDependencias(id_dependencia=None):
    try:
        if id_dependencia is not None:

            dependencia = dependenciasController.getDependencia(id_dependencia)
            return jsonify({
                'mensaje': 'Se retornara la depedencia y sus respectivos cargos',
                'dependencia': dependencia
            })
        else:
            dependencias = dependenciasController.getDependencias()

            return jsonify({
                'mensaje': 'Se retornarán todas las depedencias y sus respectivos cargos',
                'dependencias': dependencias
            })

    except Exception as error:
        print('ERROR: ', error)
        return jsonify({
            'error': 'Ocurrió un error inesperado al obtener las dependencias',
        })

@dependenciasRoutes.route('/<id_dependencia>', methods=['DELETE'])
@verificarToken
def eliminarDependencia(id_dependencia):
    try:
        if not verificarRol(request, 'SA'):
            return jsonify({ 'error': 'Permisos insuficientes para realizar esta acción' })

        if id_dependencia is not None:

            if dependenciasController.eliminarDependencia(id_dependencia) is True:
                return jsonify({
                    'mensaje': 'Se ha eliminado la dependencia de manera correcta',
                })
            else:
                return jsonify({
                    'error': 'No se ha podido eliminar la dependencia',
                })
        else:
            return jsonify({
                'error': 'Ocurrió un error inesperado al eliminar la dependencia',
            })
    except Exception as error:
        print('ERROR: ', error)
        return jsonify({
            'error': 'Ocurrió un error inesperado al eliminar la dependencia',
        })

@dependenciasRoutes.route('/cargo/<id_cargo>', methods=['DELETE'])
@verificarToken
def eliminarCargo(id_cargo):
    try:
        if not verificarRol(request, 'SA'):
            return jsonify({ 'error': 'Permisos insuficientes para realizar esta acción' })

        if id_cargo is not None:

            if dependenciasController.eliminarCargo(id_cargo) is True:
                return jsonify({
                    'mensaje': 'Se ha eliminado el cargo de manera correcta',
                })
            else:
                return jsonify({
                    'error': 'No se ha podido eliminar el cargo',
                })
        else:
            return jsonify({
                'error': 'Ocurrió un error inesperado al eliminar el cargo',
            })
    except Exception as error:
        print('ERROR: ', error)
        return jsonify({
            'error': 'Ocurrió un error inesperado al eliminar el cargo',
        })