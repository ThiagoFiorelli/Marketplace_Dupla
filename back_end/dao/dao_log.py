from back_end.dao.base_dao import BaseDao
from back_end.models.log import Log

class LogDao(BaseDao):
    def create(self, log: Log) -> None:
        hora = log.get_hour()
        date = log.get_date()
        message = log.get_message()

        query = f"INSERT INTO log (hora, data, mensagem) values('{hora}','{date}', '{message}');"
        super().execute(query)

    def read_all(self, search: str = None) -> list[Log]:
        if search == None:
            query = "SELECT * FROM log;"
        else:
            query = f"SELECT * FROM log WHERE mensagem LIKE '%{search}%';"
        logs = []
        list_log = super().read_all(query)

        for log in list_log:
            log = Log(log[3], log[1], log[2], log[0],)
            logs.append(log)
        return logs