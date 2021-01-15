import sys
sys.path.append('.')

from back_end.dao.dao_log import LogDao
from back_end.controller.base_controller import BaseController

class LogController(BaseController):
    def __init__(self) -> None:
        self.__dao = LogDao()
        super().__init__(self.__dao)