import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='@escola2025', # senha do banco de dados
    database='biblioteca_escolar'
)


cursor = conexao.cursor()


cursor.execute('CREATE DATABASE IF NOT EXISTS biblioteca_escolar')
cursor.execute('USE biblioteca_escolar')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    quantidade INT NOT NULL
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    turma VARCHAR(20) NOT NULL,
    rm VARCHAR(20) NOT NULL
    )
''')


print('Banco criado com sucesso!')
