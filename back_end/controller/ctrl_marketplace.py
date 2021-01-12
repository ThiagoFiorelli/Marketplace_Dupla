import sys
sys.path.append('.')

import back_end.dao.dao_sql_marketplace as dao_ac_txt
import back_end.controller.ctrl_log as ac_log

def create_marketplace(name: str, description: str):
    marketplace = f'{name};{description}'
    print(marketplace)
    dao_ac_txt.add_marketplace(marketplace)
    ac_log.save_log(f'Cadastro do marketplace "{name}" ao database.')


def list_marketplaces():
    marketplaces = dao_ac_txt.read_marketplace()
    ac_log.save_log('Listado todos os marketplaces.')
    return marketplaces
