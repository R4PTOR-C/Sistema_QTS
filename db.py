import psycopg2

import psycopg2

def get_all_alunos():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname='horario_academico'
        )
        cur = conn.cursor()

        cur.execute('SELECT * FROM alunos')
        rows = cur.fetchall()

        return rows
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None
    finally:
        if conn is not None:
            conn.close()
