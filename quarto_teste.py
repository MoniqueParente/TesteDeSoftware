import psycopg2
import random 
import string 
import time 

host ='localhost'
port = '1372'
database = 'unifametro'
user = 'postgres'
password = '1234567'

# Configuracao de conexao ao banco de dados para
host = 'localhost'
port = '5432'
database = 'Empresa'
user = 'postgres'	
password = '123456'

def execute_query(query):
    conn = psycopg2.connect(host=host, port=port, 
                            database=database, user=user ,password=password)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

def perform_volume_test(num_queries):
    start_time = time.time()
    for i in range(num_queries):
        query = "SELECT * FROM tabela_exemplo;"
        result = execute_query(query)
        print(f"consulta{i+1} : {result}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\n Tempo Total de execucao : {elapsed_time} segundos")
    print(f"\n Tempo medio por consulta: {elapsed_time / num_queries} segundos")

perform_volume_test(10000)