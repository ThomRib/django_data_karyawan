# utils/db_utils.py
from django.db import connections, connection

def cursor_fetch_result(query, params=[], db='default'):
    try:
        with connections[db].cursor() as cursor:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in rows]
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None


def cursor_execute_commit(query, params=[],db='default'):
    try:
        with connections[db].cursor() as cursor:
            cursor.execute(query, params)
            connection.commit()
            cursor.close()
            return {'status': True, 'message': 'Query executed successfully'}
    except Exception as e:
        print('Error : ',e)
        connection.rollback()
        return {'status': False, 'message': str(e)}

# cek koneksi database
def cek_db_default():
    try:
        connection.ensure_connection()
        print("[DB DEBUG] Default DB CONNECTED")
        return True
    except Exception as e:
        print("[DB DEBUG] Default DB FAILED:", e)
        return False