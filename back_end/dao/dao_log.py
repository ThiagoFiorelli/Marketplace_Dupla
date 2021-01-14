from back_end.models.baseDao import BaseDao
from back_end.models.log import Log

class LogDao(BaseDao):
    def create(self, log: Log) -> None:
        hora = log.get_hour()
        date = log.get_date()
        message = log.get_message()

        query = f"INSERT INTO log (hora, data, menssagem) values('{hora}','{date}', '{message}');"
        super().execute(query)

    def read(self) -> list[Log]:
        query = "SELECT * FROM log;"
        logs = []
        list_log = super().read(query)

        for log in list_log:
            log = Log(log[1], log[2], log[3], log[0])
            logs.append(log)
        return logs