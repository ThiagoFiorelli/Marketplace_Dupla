import sys
sys.path.append('.')

import back_end.dao.dao_txt_marketplace as dao_ac_txt
import back_end.dao.dao_log as dao_ac_log

def create_marketplace(name: str, description: str):
    marketplace = f'{name};{description}'
    dao_ac_txt.add_marketplace(marketplace)
    dao_ac_log.generate_log(f'Cadastro do marketplace "{name}" ao database.')


def list_marketplaces():
    marketplaces = dao_ac_txt.read_marketplace()
    dao_ac_log.generate_log('Listado todos os marketplaces.')
    return marketplaces
