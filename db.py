import psycopg2

import psycopg2

def connect_db():
    return psycopg2.connect(
        dbname='horario_academico'
    )

def get_all_alunos():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM alunos')
            return cur.fetchall()

def insert_aluno(nome,matricula,cpf, cursos):
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                # Prepara a declaração SQL para inserir os dados
                # A sintaxe %(nome)s e %(curso)s são placeholders para os valores que serão inseridos
                cur.execute('INSERT INTO alunos (nome,matricula,cpf, cursos) VALUES (%(nome)s,%(matricula)s,%(cpf)s, %(curso)s)',
                            {'nome': nome, 'matricula': matricula, 'cpf': cpf, 'curso': cursos})
                conn.commit()  # Garante que a transação seja aplicada ao banco de dados
                print("Aluno inserido com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao inserir o aluno: {e}")

