from controllers.helpers import query_db
from db import get_db

def registrarDependencia(nombre_dependencia):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'INSERT INTO dependencias(nombre_dependencia) VALUES(?)',
            [nombre_dependencia]
        )
        db.commit()
        return cursor.lastrowid
    except Exception as error:
        print('ERROR en dependenciasController.registrarDependencia: ', error)
        return None

def registrarCargo(nombre_cargo, salario, id_dependencia):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'INSERT INTO cargos(nombre_cargo, salario, id_dependencia) VALUES(?, ?, ?)',
            (nombre_cargo, salario, id_dependencia)
        )
        db.commit()
        return cursor.lastrowid
    except Exception as error:
        print('ERROR en dependenciasController.registrarCargo: ', error)
        return None

def actualizarDependencia(nombre_dependencia, id_dependencia):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'UPDATE dependencias SET nombre_dependencia = ? WHERE id_dependencia = ?',
            (nombre_dependencia, id_dependencia)
        )
        db.commit()
        if cursor.rowcount == 0:
            return False
        else:
            return True
    except Exception as error:
        print('ERROR en dependenciasController.actualizarDependencia: ', error)
        return None

def actualizarCargo(nombre_cargo, salario, id_cargo):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'UPDATE cargos SET nombre_cargo = ?, salario = ? WHERE id_cargo = ?',
            (nombre_cargo, salario, id_cargo)
        )
        db.commit()
        if cursor.rowcount == 0:
            return False
        else:
            return True
    except Exception as error:
        print('ERROR en dependenciasController.actualizarCargo: ', error)
        return None

def eliminarDependencia(id_dependencia):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('DELETE FROM cargos WHERE id_dependencia = ?', [id_dependencia])
        cursor.execute('DELETE FROM dependencias WHERE id_dependencia = ?', [id_dependencia])
        db.commit()
        if cursor.rowcount == 0:
            return False
        else:
            return True
    except Exception as error:
        print('ERROR en dependenciasController.eliminarDependencia: ', error)
        return None

def eliminarCargo(id_cargo):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('DELETE FROM cargos WHERE id_cargo = ?', [id_cargo])
        db.commit()
        if cursor.rowcount == 0:
            return False
        else:
            return True
    except Exception as error:
        print('ERROR en dependenciasController.eliminarCargo: ', error)
        return None

def getDependencia(id_dependencia):
    try:
        dependencia = query_db('SELECT * FROM dependencias WHERE id_dependencia = ?', [id_dependencia], one = True)

        if dependencia is not None:
            cargos = query_db('SELECT * FROM cargos WHERE id_dependencia = ? ORDER BY id_cargo DESC', [id_dependencia])
            return {
                'dependencia': dependencia,
                'cargos' : cargos
            }
        else:
            return None
    except Exception as error:
        print('ERROR en dependenciasController.getDependencia: ', error)
        return None

def getDependencias():
    try:
        info_dependencias = query_db('SELECT * FROM dependencias ORDER BY id_dependencia DESC')

        dependencias = []

        if info_dependencias is not None:
            for dependencia in info_dependencias:
                cargos = query_db('SELECT * FROM cargos WHERE id_dependencia = ? ORDER BY id_cargo DESC', [dependencia['id_dependencia']])
                obj_dependencia = {
                    'dependencia' : dependencia,
                    'cargos' : cargos
                }
                dependencias.append(obj_dependencia)
        return dependencias

    except Exception as error:
        print('ERROR en dependenciasController.getDependencia: ', error)
        return None