from back_end.models.log import Log
from back_end.dao.base_dao import BaseDao


class LogDao(BaseDao):
    def __init__(self):
        super().__init__(Log)
