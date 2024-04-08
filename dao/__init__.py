import psycopg2
def login(email, senha, conexao):
    cur = conexao.cursor()
    cur.execute(f"SELECT count(*) FROM usuario WHERE email = '{email}' AND senha = '{senha}'")
    recset = cur.fetchall()
    conexao.close()
    if recset[0][0] == 1:
        return True
    else:
        return False

def conectardb():
    con = psycopg2.connect(
        host='localhost',
        database='aplicacaoprojeto',
        user='postgres',
        password='1234'
    )

    return con


def insert_correlacao(conexao, ind, valor):
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO Correlacao (Indicador, Valor_Correlacao) VALUES ('{ind}', '{valor}' )"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito

def inserirusuer(email, senha, conexao):
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO usuario (email, senha) VALUES ('{email}', '{senha}' )"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito



def listarUsuarios(conexao):
    cur = conexao.cursor()
    cur.execute('select * from usuario')
    recset = cur.fetchall()
    conexao.close()

    return recset
