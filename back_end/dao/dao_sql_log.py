import psycopg2
from back_end.models.log import Log

_host = 'pgsql08-farm15.uni5.net '
_user = 'topskills5'
_password = 'olist123'
_database = 'topskills5'
_connection_string = f'host={_host} user={_user} password={_password} dbname={_database}'

def generate_log(log: Log) -> None:
    _connection_string
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO log (hora,data,mensagem) values('{log.get_hour()}','{log.get_date()}','{log.get_message()}');")
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
        log = Log(i[1], i[2], i[3])
        l_dict_log.append(log)

    conn.commit()
    cursor.close()
    conn.close()

    return l_dict_log