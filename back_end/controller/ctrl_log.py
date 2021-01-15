import sys
sys.path.append('.')

from back_end.dao.dao_log import LogDao
from back_end.models.log import Log

class LogController:
    def __init__(self) -> None:
        self.__dao = LogDao()

    def create(self, model: object) -> None:
        self.__dao.create(model)
    
    def read_all(self) -> list[Log]:
        return self.__dao.read_all()