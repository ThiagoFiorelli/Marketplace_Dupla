import psycopg2
from back_end.models.log import Log
from connection import connect_db

def generate_log(log: Log) -> None:
    string_connection = connect_db()
    with psycopg2.connect(string_connection) as conn:
        cursor = conn.cursor()

        cursor.execute(f"INSERT INTO log (hora, data, mensagem) values('{log.get_hour()}','{log.get_date()}','{log.get_message()}');")
        conn.commit()
    

def read_logs() -> list:
    string_connection = connect_db()
    with psycopg2.connect(string_connection) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM log")
        list_log = cursor.fetchall()
        l_dict_log = []

        for i in list_log:
            log = Log(i[1], i[2], i[3])
            l_dict_log.append(log)

        conn.commit()
        return l_dict_log