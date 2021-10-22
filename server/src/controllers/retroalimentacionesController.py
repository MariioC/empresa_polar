from controllers.helpers import query_db
from db import get_db

def registrarRetroalimentacion(puntaje, fecha_retroalimentacion, retroalimentacion, id_usuario, id_evaluador):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'INSERT INTO retroalimentaciones(puntaje, fecha_retroalimentacion, retroalimentacion, id_usuario, id_evaluador) VALUES(?, ?, ?, ?, ?)',
            (puntaje, fecha_retroalimentacion, retroalimentacion, id_usuario, id_evaluador)
        )
        db.commit()
        return cursor.lastrowid
    except Exception as error:
        print('ERROR en retroalimentacionesController.registrarRetroalimentacion: ', error)
        return None

def actualizarRetroalimentacion(puntaje, retroalimentacion, id_evaluador, id_retroalimentacion):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'UPDATE retroalimentaciones SET puntaje = ?, retroalimentacion = ?, id_evaluador = ? WHERE id_retroalimentacion = ?',
            (puntaje, retroalimentacion, id_evaluador, id_retroalimentacion)
        )
        db.commit()
        if cursor.rowcount == 0:
            return False
        else:
            return True
    except Exception as error:
        print('ERROR en retroalimentacionesController.actualizarRetroalimentacion: ', error)
        return None

def eliminarRetroalimentacion(id_retroalimentacion):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('DELETE FROM retroalimentaciones WHERE id_retroalimentacion = ?', [id_retroalimentacion])
        db.commit()
        if cursor.rowcount == 0:
            return False
        else:
            return True
    except Exception as error:
        print('ERROR en retroalimentacionesController.eliminarRetroalimentacion: ', error)
        return None

def comrpobarRetroalimentacion(fecha_inicial, fecha_final, id_usuario):
    try:
        retroalimentacion = query_db('SELECT * FROM retroalimentaciones WHERE fecha_retroalimentacion BETWEEN ? AND ? AND id_usuario = ?', (fecha_inicial, fecha_final, id_usuario), one = True)

        return retroalimentacion
        
    except Exception as error:
        print('ERROR en retroalimentacionesController.getRetroalimentacion: ', error)
        return None

def getRetroalimentacion(id_retroalimentacion):
    try:
        retroalimentacion = query_db('SELECT * FROM retroalimentaciones WHERE id_retroalimentacion = ?', [id_retroalimentacion], one = True)

        return retroalimentacion

    except Exception as error:
        print('ERROR en retroalimentacionesController.getRetroalimentacion: ', error)
        return None

def getRetroalimentaciones(id_usuaio):
    try:
        retroalimentaciones = query_db('SELECT R.*, U.nombres as evaluador FROM retroalimentaciones as R INNER JOIN usuarios as U ON R.id_evaluador = U.id_usuario WHERE R.id_usuario = ? ORDER BY R.id_retroalimentacion DESC', [id_usuaio])
        return retroalimentaciones
    except Exception as error:
        print('ERROR en retroalimentacionesController.getRetroalimentaciones: ', error)
        return None