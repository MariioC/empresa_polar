# Base de datos
from db import get_db, close_db

def query_db(query, args=[], one=False):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(query, args)
    r = [dict((cursor.description[i][0], value) \
            for i, value in enumerate(row)) for row in cursor.fetchall()]
#     cursor.connection.close()
    return (r[0] if r else None) if one else r