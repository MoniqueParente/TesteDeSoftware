import psycopg2
import random 
import string 
import time 

host ='localhost'
port = '1372'
database = 'unifametro'
user = 'postgres'
password = '1234567'

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def execute_query(query):
    conn = psycopg2.connect(host=host, port=port, database=database, user=user ,password=password)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

# Funcao para executar uma consulta no banco de dados
def execute_query(query):
    conn = psycopg2.connect(host=host, port=port, database=database, user=user ,password=password)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    conn.commit()
    conn.close()
    return result

def read_query(query):
    conn = psycopg2.connect(host=host, port=port, database=database, user=user ,password=password)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def perform_volume_test(num_records):

    for i in range(num_records):
        dados = generate_random_string(1000)
        insert_query = f"INSERT INTO tabela_exemplo(dados) VALUES ('{dados}');"
        execute_query(insert_query)

    count_query = "SELECT COUNT(*) FROM tabela_exemplo;"
    result = read_query(count_query)
    count = result[0][0]
    print(f"Número Total de Registros:{count}")


    #Executa o teste de volume com 1000 registro
    start_time = time.time()
    perform_volume_test(10)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Numero Tempo de execucao:{elapsed_time}")

