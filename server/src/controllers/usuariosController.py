from controllers.helpers import query_db
from db import get_db

def loginUsuario(documento):
    try:
        return query_db('SELECT id_usuario, documento, password, rol FROM usuarios WHERE documento = ?', [documento], one = True)
    except Exception as error:
        print('ERROR en usuariosController.loginUsuario: ', error)
        return None

def registrarUsuario(nombres, apellidos, documento, fecha_nacimiento, genero, correo, celular, direccion, ciudad, estado_civil, password, rol = "E"):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'INSERT INTO usuarios(nombres, apellidos, documento, fecha_nacimiento, genero, correo, celular, direccion, ciudad, estado_civil, password, rol) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
           (nombres, apellidos, documento, fecha_nacimiento, genero, correo, celular, direccion, ciudad, estado_civil, password, rol)
        )
        db.commit()
        return cursor.lastrowid
    except Exception as error:
        print('ERROR en usuariosController.registrarUsuario: ', error)
        return None

def registrarInfoLaboral(id_cargo, tipo_contrato, fecha_ingreso, fecha_terminacion, id_usuario):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'INSERT INTO info_laboral(id_cargo, tipo_contrato, fecha_ingreso, fecha_terminacion, id_usuario) VALUES(?, ?, ?, ?, ?)',
            (id_cargo, tipo_contrato, fecha_ingreso, fecha_terminacion, id_usuario)
        )
        db.commit()
        return cursor.lastrowid
    except Exception as error:
        print('ERROR en usuariosController.registrarInfoLaboral: ', error)
        return None

def actualizarUsuario(nombres, apellidos, documento, fecha_nacimiento, genero, correo, celular, direccion, ciudad, estado_civil, rol, id_usuario):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'UPDATE usuarios SET nombres = ?, apellidos = ?, documento = ?, fecha_nacimiento = ?, genero = ?, correo = ?, celular = ?, direccion = ?, ciudad = ?, estado_civil = ?, rol = ? WHERE id_usuario = ?',
            (nombres, apellidos, documento, fecha_nacimiento, genero, correo, celular, direccion, ciudad, estado_civil, rol, id_usuario)
        )
        db.commit()
        if cursor.rowcount == 0:
            return False
        else:
            return True
    except Exception as error:
        print('ERROR en usuariosController.actualizarUsuario: ', error)
        return None

def actualizarInfoLaboral(id_cargo, tipo_contrato, fecha_ingreso, fecha_terminacion, id_usuario):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'UPDATE info_laboral SET id_cargo = ?, tipo_contrato = ?, fecha_ingreso = ?, fecha_terminacion = ? WHERE id_usuario = ?',
            (id_cargo, tipo_contrato, fecha_ingreso, fecha_terminacion, id_usuario)
        )
        db.commit()
        if cursor.rowcount == 0:
            return False
        else:
            return True
    except Exception as error:
        print('ERROR en usuariosController.actualizarInfoLaboral: ', error)
        return None

def actualizarPassword(password, id_usuario):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'UPDATE usuarios SET password = ? WHERE id_usuario = ?',
            (password, id_usuario)
        )
        db.commit()
        if cursor.rowcount == 0:
            return False
        else:
            return True
    except Exception as error:
        print('ERROR en usuariosController.actualizarUsuario: ', error)
        return None

def eliminarUsuario(id_usuario):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('DELETE FROM retroalimentaciones WHERE id_usuario = ?', [id_usuario])
        cursor.execute('DELETE FROM info_laboral WHERE id_usuario = ?', [id_usuario])
        cursor.execute('DELETE FROM usuarios WHERE id_usuario = ?', [id_usuario])
        db.commit()
        if cursor.rowcount == 0:
            return False
        else:
            return True
    except Exception as error:
        print('ERROR en usuariosController.eliminarUsuario: ', error)
        return None

def getUsuario(usuario):
    try:
        usuario = query_db('SELECT * FROM usuarios WHERE id_usuario = ? OR documento = ? OR correo = ?', (usuario, usuario, usuario), one = True)

        if usuario is not None:
            usuario.pop('password')

            info_laboral = query_db('SELECT L.*, C.nombre_cargo, C.salario, D.* FROM info_laboral as L INNER JOIN cargos as C ON L.id_cargo = C.id_cargo INNER JOIN dependencias as D ON D.id_dependencia = C.id_dependencia WHERE L.id_usuario = ?', [usuario['id_usuario']], one = True)

            return {
                'info_personal' : usuario,
                'info_laboral' : info_laboral,
            }
        else:
            return usuario
    except Exception as error:
        print('ERROR en usuariosController.getUsuario: ', error)
        return None

def getUsuarios():
    try:
        all_usuarios = query_db('SELECT * FROM usuarios ORDER BY id_usuario DESC')

        if all_usuarios is not None:
            usuarios = []
            for usuario in all_usuarios:
                obj_usuario = getUsuario(usuario['id_usuario'])
                usuarios.append(obj_usuario)
            return usuarios
        else:
            return None
    except Exception as error:
        print('ERROR en usuariosController.getUsuarios: ', error)
        return None

def buscarUsuarios(query):
    try:
        all_usuarios = []

        usuarios = query_db('SELECT * FROM usuarios WHERE nombres LIKE ? OR apellidos LIKE ? OR CAST(documento as CHAR) LIKE ? OR correo LIKE ?', (f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%'))
        
        if usuarios is not None:
            for usuario in usuarios:
                obj_usuario = getUsuario(usuario['id_usuario'])
                all_usuarios.append(obj_usuario)
        
        info_laboral = query_db('SELECT L.*, C.nombre_cargo, C.salario, D.* FROM info_laboral as L INNER JOIN cargos as C ON L.id_cargo = C.id_cargo INNER JOIN dependencias as D ON D.id_dependencia = C.id_dependencia WHERE C.nombre_cargo LIKE ? OR D.nombre_dependencia LIKE ?', (f'%{query}%', f'%{query}%'))

        if info_laboral is not None:
            for info in info_laboral:
                if comprobarUsuario(all_usuarios, lambda x: x['info_personal']['id_usuario'] == info['id_usuario']) is False:
                    obj_usuario = getUsuario(info['id_usuario'])
                    if obj_usuario is not None:
                        all_usuarios.append(obj_usuario)

                
        return all_usuarios
    except Exception as error:
        print('ERROR en usuariosController.buscarUsuarios: ', error)
        return None

def comprobarUsuario(list, filter):
    for x in list:
        if filter(x):
            return True
    return False

def getSummary():
    try:

        db = get_db()
        cursor = db.cursor()
        dependencias = cursor.execute('SELECT count(*) as dependencias FROM dependencias').fetchone()
        cargos = cursor.execute('SELECT count(*) as cargos FROM cargos').fetchone()
        superadmins = cursor.execute('SELECT count(*) FROM usuarios WHERE rol = "SA"').fetchone()
        admins = cursor.execute('SELECT count(*) FROM usuarios WHERE rol = "A"').fetchone()
        empleados = cursor.execute('SELECT count(*) FROM usuarios WHERE rol = "E"').fetchone()
        nomina = cursor.execute('SELECT sum(C.salario) FROM info_laboral as L INNER JOIN cargos as C ON L.id_cargo = C.id_cargo').fetchone()
        retroalimentaciones = cursor.execute('SELECT count(*) FROM retroalimentaciones').fetchone()
        mejor_puntaje = cursor.execute('SELECT max(puntaje) FROM retroalimentaciones').fetchone()
        db.commit()

        return{
            'dependencias': dependencias[0],
            'cargos': cargos[0],
            'superadmins': superadmins[0],
            'admins': admins[0],
            'empleados': empleados[0],
            'nomina': nomina[0],
            'retroalimentaciones': retroalimentaciones[0],
            'mejor_puntaje': mejor_puntaje[0]
        }
    except Exception as error:
        print('ERROR en usuariosController.getUsuarios: ', error)
        return None