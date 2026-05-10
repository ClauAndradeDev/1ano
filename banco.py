import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@escola2025', # senha do banco de dados
        database='biblioteca_escolar'
    )

    return conexao


# CADASTRAR LIVRO
def cadastrar_livro(titulo, autor, categoria, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = '''
    INSERT INTO livros (titulo, autor, categoria, quantidade)
    VALUES (%s, %s, %s, %s)
    '''

    valores = (titulo, autor, categoria, quantidade)

    cursor.execute(sql, valores)

    conexao.commit()
    conexao.close()


# LISTAR LIVROS
def listar_livros():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM livros')

    livros = cursor.fetchall()

    conexao.close()

    return livros


# CADASTRAR ALUNO
def cadastrar_aluno(nome, turma, rm):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = '''
    INSERT INTO alunos (nome, turma, rm)
    VALUES (%s, %s, %s)
    '''

    valores = (nome, turma, rm)

    cursor.execute(sql, valores)

    conexao.commit()
    conexao.close()


# LISTAR ALUNOS
def listar_alunos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM alunos')

    alunos = cursor.fetchall()

    conexao.close()

    return alunos