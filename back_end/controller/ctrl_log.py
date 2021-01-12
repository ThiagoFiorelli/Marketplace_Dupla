import sys
sys.path.append('.')

import back_end.dao.dao_sql_log as dao_log


def save_log(dado:str):
    dao_log.generate_log(dado)



def list_log()->list:
    list_aux=[]
    list_aux = dao_log.read_logs()
    return list_aux

