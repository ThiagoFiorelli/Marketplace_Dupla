import psycopg2
from datetime import datetime

_host = 'pgsql08-farm15.uni5.net '
_user = 'topskills5'
_password = 'olist123'
_database = 'topskills5'
_connection_string = f'host={_host} user={_user} password={_password} dbname={_database}'

def generate_log(msg: str) -> None:
    hora_atual= datetime.now().strftime('%H:%M:%S')
    data_atual= datetime.now().strftime('%d/%m/%Y')

    _connection_string
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO log (hora,data,mensagem) values('{hora_atual}','{data_atual}','{msg}');")
    conn.commit()
    cursor.close()
    conn.close()
    

def read_logs() -> list:
    _connection_string
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM log")
    list_log = cursor.fetchall()

    l_dict_log = []

    for i in list_log:
        l_dict_log.append({'hora':i[1], 'data':i[2], 'mensagem':i[3]})

    conn.commit()
    cursor.close()
    conn.close()

    return l_dict_log