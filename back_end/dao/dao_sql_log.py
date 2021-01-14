from back_end.models.log import Log
from back_end.dao.connection import connect_db

def add_log(log: Log) -> None:
    db = connect_db()
    with db as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO log (hora, data, mensagem) values('{log.get_hour()}','{log.get_date()}','{log.get_message()}');")
        conn.commit()
    
def read_logs() -> list:
    db = connect_db()
    with db as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM log")
        list_log = cursor.fetchall()
        logs = []

        for i in list_log:
            log = Log(i[1], i[2], i[3])
            logs.append(log)
        return logs