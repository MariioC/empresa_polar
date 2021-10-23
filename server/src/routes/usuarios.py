from flask import Blueprint, jsonify, request

# Bcrypt
from flask_bcrypt import generate_password_hash, check_password_hash

# Controllers
import controllers.usuariosController as usuariosController

#JWT
from jwt_helpers import verificarToken, identificarUsuario, crearToken, verificarRol

#Yagmail
import yagmail

# PARA GENERAR LAS CONTRASEÑAS NUEVAS DE FORMA ALEATORIA
import string    
import random

# Configuración del correo de la empresa y contraseña del correo
from config import CORREO_EMPRESA, PASSWORD_CORREO

usuariosRoutes = Blueprint('usuariosRoutes', __name__)

@usuariosRoutes.route('/login', methods=['POST'])
def loginUsuario():
    try:

        json_data = request.json
        usuario = json_data['usuario']
        password = json_data['password']

        if usuario is not None and password is not None:

            info_usuario = usuariosController.loginUsuario(usuario)

            if info_usuario is not None:
                if str(usuario) == str(info_usuario['documento']) and check_password_hash(info_usuario['password'], str(password)):

                    token = crearToken({ 'id_usuario' : info_usuario['id_usuario'], 'documento' : info_usuario['documento'], 'rol': info_usuario['rol'] })

                    usuario = usuariosController.getUsuario(info_usuario['id_usuario'])

                    summary = None

                    if info_usuario['rol'] == 'SA' or info_usuario['rol'] == 'A':
                        summary = usuariosController.getSummary()

                    return jsonify({
                        'mensaje': 'Sesión iniciada',
                        'token': token,
                        'usuario': usuario,
                        'summary': summary
                    })

                else:
                    return jsonify({
                        'error': 'Usuario y/o contraseña incorrectos'
                    })
            else:
                return jsonify({
                    'error': 'Usuario no registrado en la empresa'
                })
        else:
            return jsonify({
                'error': 'Falta el usuario y/o la contraseña'
            })
    except Exception as error:
        print("Error en usuariosRoutes.loginUsuario: ", error)
        return jsonify({
            'error': 'Ocurrió un error inesperado al iniciar sesión',
        })

@usuariosRoutes.route('/sesion')
@verificarToken
def comprobarSesion():
    try:
        sesion_usuario = identificarUsuario(request)

        usuario = usuariosController.getUsuario(sesion_usuario['id_usuario'])
        

        if usuario is not None:

            summary = None
            if verificarRol(request, 'A') or verificarRol(request, 'SA'):
                summary = usuariosController.getSummary()

            return jsonify({
                'usuario': usuario,
                'summary': summary
            })
        else:
            return jsonify({
                'error': 'Hay un error con la sesión actual \n Inicie sesión nuevamente',
            })
    except Exception as error:
        print("Error en usuariosRoutes.comprobarSesion: ", error)
        return jsonify({
            'error': 'Ocurrió un error al comprobar la sesión del usuario',
        })

@usuariosRoutes.route('/registro', methods=['POST'])
@verificarToken
def registrarUsuario():
    try:

        json_data = request.json

        info_personal = json_data['info_personal']

        nombres = info_personal['nombres']
        apellidos = info_personal['apellidos']
        documento = info_personal['documento']
        fecha_nacimiento = info_personal['fecha_nacimiento']
        genero = info_personal['genero']
        correo = info_personal['correo']
        celular = info_personal['celular']
        direccion = info_personal['direccion']
        ciudad = info_personal['ciudad']
        estado_civil = info_personal['estado_civil']
        password = info_personal['password']
        rol = info_personal['rol']

        info_laboral = json_data['info_laboral']
        
        id_cargo = info_laboral['id_cargo']
        tipo_contrato = info_laboral['tipo_contrato']     
        fecha_ingreso = info_laboral['fecha_ingreso']     
        fecha_terminacion = info_laboral['fecha_terminacion']


        # Si el rol del usuario que se quiere crear es Empleado, verifico que el usuarrio que envio los datos, tenga el rol necesario
        if rol == 'E':
            if not verificarRol(request, 'A') and not verificarRol(request, 'SA'):
                return jsonify({ 'error': 'Permisos insuficientes para registrar un usuario con el rol "Empleado"' })
        else:
            # SiNo el rol del usuario que se quiere crear es Admin o SuperAdmin, entonces verifico que el usuarrio que envio los datos, tenga el rol de superadministrador
            if not verificarRol(request, 'SA'):
                return jsonify({ 'error': 'Permisos insuficientes para registrar un usuario con el rol seleccionado' })

        if usuariosController.getUsuario(documento) is not None:
            return jsonify({
                'error': 'El numero de documento, ya se encuentra registrado',
            })

        if usuariosController.getUsuario(correo) is not None:
            return jsonify({
                'error': 'El correo diligenciado, ya se encuentra registrado',
            })

        # Hasheo la contraseña
        # Si se envia la contraseña, el password se hashea
        if password is not None and password != "":
            password = generate_password_hash(password, 15).decode('utf-8')
        else:
            # Si NO se envia la contraseña, el password se hashea pero pasa a ser el documento de identidad
            password = generate_password_hash(str(documento), 15).decode('utf-8')


        # Registro al USUARIO y obtengo el id del usuaio que se inserto
        id_usuario = usuariosController.registrarUsuario(nombres, apellidos, documento, fecha_nacimiento, genero, correo, celular, direccion, ciudad, estado_civil, password, rol)

        if id_usuario is not None:
            # Compruebo si se mando informacion laboral, para registrarsela al usuario
            
            if id_cargo is not None and id_cargo != "":
                usuariosController.registrarInfoLaboral(id_cargo, tipo_contrato, fecha_ingreso, fecha_terminacion, id_usuario)

            usuario = usuariosController.getUsuario(id_usuario)
            return jsonify({
                'mensaje': 'Usuario registrado correctamente',
                'usuario': usuario
            })

        else:
            return jsonify({
                'error': 'Ocurrió un error inesperado al registrar usuario',
            })
    except Exception as error:
        print("Error en usuariosRoutes.registrarUsuario: ", error)
        return jsonify({
            'error': 'Ocurrió un error inesperado al registrar usuario',
        })

@usuariosRoutes.route('/', methods=['PUT'])
@usuariosRoutes.route('/<id_usuario>', methods=['PUT'])
@verificarToken
def actualizarUsuario(id_usuario = None):
    try:
        json_data = request.json

        info_personal = json_data['info_personal']

        nombres = info_personal['nombres']
        apellidos = info_personal['apellidos']
        documento = info_personal['documento']
        fecha_nacimiento = info_personal['fecha_nacimiento']
        genero = info_personal['genero']
        correo = info_personal['correo']
        celular = info_personal['celular']
        direccion = info_personal['direccion']
        ciudad = info_personal['ciudad']
        estado_civil = info_personal['estado_civil']
        rol = info_personal['rol']

        info_laboral = json_data['info_laboral']
        
        id_cargo = info_laboral['id_cargo']
        tipo_contrato = info_laboral['tipo_contrato']     
        fecha_ingreso = info_laboral['fecha_ingreso']     
        fecha_terminacion = info_laboral['fecha_terminacion']

        # SI SE TIENE EL ID_USUARIO POR PARAMETRO QUIERE DECIR QUE UN ADMIN O SUPERADMIN QUIERE ACTUALIZAR UN PERFIL DE USUARIO
        if id_usuario:

            if not verificarRol(request, 'A') and not verificarRol(request, 'SA'):   
                return jsonify({ 'error': 'Permisos insuficientes para actualizar un usuario' })
            
            if rol == 'A' or rol == 'SA':
                if not verificarRol(request, 'SA'):
                    return jsonify({ 'error': 'Permisos insuficientes para actualizar este usuario' })
            
            usuario = usuariosController.getUsuario(id_usuario)

            if usuario is None:
                return jsonify({
                    'error': 'No se ha encontrado la información del usuario',
                })

            if usuariosController.actualizarUsuario(nombres, apellidos, documento, fecha_nacimiento, genero, correo, celular, direccion, ciudad, estado_civil, rol, id_usuario) is True:
                
                if id_cargo != "" and id_cargo is not None:
                    if usuario['info_laboral'] is not None:
                        usuariosController.actualizarInfoLaboral(id_cargo, tipo_contrato, fecha_ingreso, fecha_terminacion, id_usuario)
                    else:
                        usuariosController.registrarInfoLaboral(id_cargo, tipo_contrato, fecha_ingreso, fecha_terminacion, id_usuario)


                usuario_actualizado = usuariosController.getUsuario(id_usuario)
                return jsonify({
                    'mensaje': 'Se ha actualizado la información del usuario correctamente',
                    'usuario': usuario_actualizado
                })

            else:
                return jsonify({
                    'error': 'No se ha podido actualizar la información del usuario',
                })
        else:
            session_usuario = identificarUsuario(request)

            usuario = usuariosController.getUsuario(session_usuario['id_usuario'])

            if usuario is None:
                return jsonify({
                    'error': 'No se ha encontrado la información del usuario',
                })

            if usuariosController.actualizarUsuario(nombres, apellidos, documento, fecha_nacimiento, genero, correo, celular, direccion, ciudad, estado_civil, session_usuario['rol'], session_usuario['id_usuario']) is True:
                if verificarRol(request, 'SA'):
                    if id_cargo != "" and id_cargo is not None:
                        if usuario['info_laboral'] is not None:
                            usuariosController.actualizarInfoLaboral(id_cargo, tipo_contrato, fecha_ingreso, fecha_terminacion, session_usuario['id_usuario'])
                        else:
                            usuariosController.registrarInfoLaboral(id_cargo, tipo_contrato, fecha_ingreso, fecha_terminacion, session_usuario['id_usuario'])

                usuario_actualizado = usuariosController.getUsuario(session_usuario['id_usuario'])
                return jsonify({
                    'mensaje': 'Se ha actualizado su información de perfil correctamente',
                    'usuario': usuario_actualizado
                })
            else:
                return jsonify({
                    'error': 'No se ha podido actualizar la información de su perfil',
                })
    except Exception as error:
        print("Error en usuariosRoutes.actualizarUsuario: ", error)
        return jsonify({
            'error': 'Ocurrió un error inesperado al actualizar la información del usuario'
        })

@usuariosRoutes.route('/password/', methods=['PUT'])
@usuariosRoutes.route('/password/<id_usuario>', methods=['PUT'])
@verificarToken
def actualizarPasswordUsuario(id_usuario = None):
    try:
        
        json_data = request.json
        password = json_data['password']
        new_password = json_data['new_password']
        re_password = json_data['re_password']

        # SI SE TIENE EL ID_USUARIO POR PARAMETRO QUIERE DECIR QUE UN ADMIN O SUPERADMIN QUIERE ACTUALIZAR UN PERFIL DE USUARIO
        if id_usuario:
            usuario = usuariosController.getUsuario(id_usuario)

            if not verificarRol(request, 'A') and not verificarRol(request, 'SA'):   
                return jsonify({ 'error': 'Permisos insuficientes para actualizar contraseñas' })
            
            if usuario['info_personal']['rol'] == 'A' or usuario['info_personal']['rol'] == 'SA':
                if not verificarRol(request, 'SA'):
                    return jsonify({ 'error': 'Permisos insuficientes para actualizar la contraseña de este usuario' })

            if(new_password == re_password):
                new_password = generate_password_hash(str(new_password), 15).decode('utf-8')

                if usuariosController.actualizarPassword(new_password, usuario['info_personal']['id_usuario']) is True:
                    return jsonify({
                        'mensaje': 'Se ha actualizado la contraseña del usuario correctamente',
                    })
                else:
                    return jsonify({
                        'error': 'No se ha podido actualizar la contraseña del usuario',
                    })
            else:
                return jsonify({
                    'error': 'Las contraseñas nuevas no coinciden',
                })
        else:
            session_usuario = identificarUsuario(request)

            usuario = usuariosController.loginUsuario(session_usuario['documento'])

            if check_password_hash(usuario['password'], str(password)) is True:
                if(new_password == re_password):
                    new_password = generate_password_hash(str(new_password), 15).decode('utf-8')
                    if usuariosController.actualizarPassword(new_password, session_usuario['id_usuario']) is True:
                        return jsonify({
                            'mensaje': 'Se ha actualizado su contraseña correctamente',
                        })
                    else:
                        return jsonify({
                            'error': 'No se ha podido actualizar su contraseña',
                        })
                else:
                    return jsonify({
                        'error': 'Las contraseñas nuevas no coinciden',
                    })
            else:
                return jsonify({
                    'error': 'La contraseña actual es incorrecta',
                })
    except Exception as error:
        print("Error en usuariosRoutes.actualizarPassword: ", error)
        return jsonify({
            'error': 'Ocurrió un error inesperado al actualizar la contraseña del usuario'
        })

@usuariosRoutes.route('/password/<usuario>', methods=['GET'])
def restablecerPasswordUsuario(usuario = None):
    try:

        # SI SE TIENE EL ID_USUARIO POR PARAMETRO QUIERE DECIR QUE UN ADMIN O SUPERADMIN QUIERE ACTUALIZAR UN PERFIL DE USUARIO
        if usuario is not None:
            
            info_usuario = usuariosController.getUsuario(str(usuario))
            if info_usuario is not None:
                # GENERO LA NUEVA CONTRASEÑA
                password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))

                new_password = generate_password_hash(str(password), 15).decode('utf-8')
                if usuariosController.actualizarPassword(new_password, info_usuario['info_personal']['id_usuario']) is True:
                    
                    asunto = 'Empresa polar | Restablecimiento de contraseña'
                    correo = info_usuario['info_personal']['correo']
                    mensaje = 'Hola, {0}.\n\n Se ha restablecido su contraseña de forma correcta. \n\nSu contraseña ha sido actualizada, se le recomienda cambiarla una vez inicie sesión.\n\n Contraseña nueva: <b>{1}</b>'.format(info_usuario['info_personal']['nombres'], password)

                    yag = yagmail.SMTP(user=CORREO_EMPRESA, password=PASSWORD_CORREO)
                    
                    yag.send(to=correo, subject=asunto, contents=mensaje)

                    preview_correo = correo[0:4] + '........' + correo[correo.find('@')-3: correo.find('@')] + correo[correo.find('@'):];

                    return jsonify({
                        'mensaje': 'Hemos enviado un correo con la información necesaria al correo registrado en la empresa: {0}'.format(preview_correo)
                    })
                else:
                    return jsonify({
                        'error': 'No se ha podido restablecer la contraseña del usuario',
                    })
            else:
                return jsonify({
                    'error': 'Usuario no registrado en la empresa',
                })
        else:
            return jsonify({
                'error': 'Hay un error con el usuario que ha digitado',
            })
    except Exception as error:
        print("Error en usuariosRoutes.restablecerPasswordUsuario: ", error)
        return jsonify({
            'error': 'Ocurrió un error inesperado al rerstablecer la contraseña del usuario'
        })

@usuariosRoutes.route('/<id_usuario>', methods=['DELETE'])
@verificarToken
def eliminarUsuario(id_usuario):
    try:
         
        usuario = usuariosController.getUsuario(id_usuario)

        if usuario is not None:

            if not verificarRol(request, 'A') and not verificarRol(request, 'SA'):
                return jsonify({ 'error': 'Permisos insuficientes para eliminar usuarios' })

            if usuario['info_personal']['rol'] == 'A' or usuario['info_personal']['rol'] == 'SA':
                if not verificarRol(request, 'SA'):
                    return jsonify({ 'error': 'Permisos insuficientes para eliminar este usuario' })
            

            if usuariosController.eliminarUsuario(usuario['info_personal']['id_usuario']) is True:
                return jsonify({
                    'mensaje': 'Se ha eliminado el usuario de manera correcta'
                })
            else:
                return jsonify({
                    'error': 'No se ha podido eliminar el usuario'
                })

        else:
            return jsonify({
                'error': 'El usuario que desea eliminar no existe'
            })
    except Exception as error:
        print("Error en usuariosRoutes.eliminarUsuario: ", error)
        return jsonify({
            'error': 'Ocurrió un error inesperado al eliminar el usuario',
        })

@usuariosRoutes.route('/')
@usuariosRoutes.route('/<id_usuario>')
@verificarToken
def obtenerUsuarios(id_usuario = None):
    try:
        if id_usuario:
            token_usuario = identificarUsuario(request)

            if not verificarRol(request, 'A') and not verificarRol(request, 'SA'):
                id_usuario = token_usuario['id_usuario']

            usuario = usuariosController.getUsuario(id_usuario)
            return jsonify({
                'mensaje': 'Se retornará la información del usuario: {0}'.format(id_usuario),
                'usuario': usuario
            })
        else:

            if not verificarRol(request, 'A') and not verificarRol(request, 'SA'):
                return jsonify({ 'error': 'Permisos insuficientes para realizar la petición solicitada' })

            usuarios = usuariosController.getUsuarios()
            return jsonify({
                'mensaje': 'Se retornarán todos los usuarios',
                'usuarios': usuarios
            })
    except Exception as error:
        print("Error en usuariosRoutes.obtenerUsuarios: ", error)
        return jsonify({
            'error': 'Ocurrió un error inesperado al obtener la información solicitada',
        })

@usuariosRoutes.route('/buscar/<query>')
@verificarToken
def buscarUsuarios(query):
    try:
        if not verificarRol(request, 'A') and not verificarRol(request, 'SA'):
            return jsonify({ 'error': 'Permisos insuficientes para realizar esta acción' })
        
        resultados = usuariosController.buscarUsuarios(query)
        return jsonify({
            'mensaje': 'Se retornarán los usuarios que coincidan con el termino de busqueda: {0}'.format(query),
            'resultados': resultados
        })
    except Exception as error:
        print("Error en usuariosRoutes.buscarUsuarios: ", error)
        return jsonify({
            'error': 'Ocurrió un error al realizar la busqueda de usuarios',
        })

@usuariosRoutes.route('/contacto', methods=['POST'])
def enviarMensajeContacto():
    try:
        json_data = request.json

        asunto = json_data['asunto']
        correo = json_data['correo']
        mensaje = 'Mensaje enviado por: <b>{0}</b>\n\n {1}'.format(correo, json_data['mensaje'])

        yag = yagmail.SMTP(user=CORREO_EMPRESA, password=PASSWORD_CORREO)

        yag.send(to=CORREO_EMPRESA, subject=asunto, contents=mensaje)
        
        return jsonify({
            'mensaje': 'Mensaje enviado.\n Nos pondremos en contacto lo más pronto posible',
        })
    except Exception as error:
        print("Error en usuariosRoutes.enviarMensajeContacto: ", error)
        return jsonify({
            'error': 'Ocurrió un error al enviar el correo de contacto.\n Inténtalo más tarde',
        })