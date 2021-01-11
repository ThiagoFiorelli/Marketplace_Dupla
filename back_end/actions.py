import sys

sys.path.append('.')

from back_end.log import generate_log, read_logs
import back_end.controller.ctrl_category as db
import back_end.controller.ctrl_product as db_prod


#pode ser tirado do codigo
def list_logs():
    logs = read_logs()
    return logs


def verify():
    pass
