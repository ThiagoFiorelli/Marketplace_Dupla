from datetime import datetime
import sys
sys.path.append('.')

import back_end.dao.dao_sql_log as dao_log
from back_end.models.log import Log


def save_log(dado:str):
    hora_atual= datetime.now().strftime('%H:%M:%S')
    data_atual= datetime.now().strftime('%d/%m/%Y')
    log = Log(hora_atual, data_atual, dado)
    dao_log.generate_log(log)



def list_log() -> list:
    list_aux=[]
    list_aux = dao_log.read_logs()
    return list_aux

