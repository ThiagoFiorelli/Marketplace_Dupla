import sys
sys.path.append('.')

import back_end.dao.dao_txt as dao_ac_txt
import back_end.dao.dao_log as dao_ac_log

def create_seller(name: str, phone: str, email: str):
    seller = f'{name};{phone};{email}'
    dao_ac_txt.add_seller(seller)
    dao_ac_log.generate_log(f'Cadastro do seller "{name}" ao database.')


def list_sellers():
    sellers = dao_ac_txt.read_seller()
    dao_ac_log.generate_log('Listado todos os sellers.')
    return sellers
