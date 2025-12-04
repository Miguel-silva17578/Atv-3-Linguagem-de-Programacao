import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # seu usuário
        password="telespe",  # sua senha
        database="imcdb"
    )

def inserir_paciente(nome, endereco, altura, peso, imc, classificacao):
    db = conectar()
    cursor = db.cursor()

    comando = """
        INSERT INTO pacientes 
        (nome, endereco, altura, peso, imc, classificacao)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    valores = (nome, endereco, altura, peso, imc, classificacao)
    cursor.execute(comando, valores)

    db.commit()
    db.close()
