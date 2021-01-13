import sys
sys.path.append('.')

import back_end.dao.dao_sql_seller as dao_ac
import back_end.controller.ctrl_log as ac_log
from back_end.models.seller import Seller

def create_seller(seller: Seller):
    dao_ac.add_seller(seller)
    ac_log.create_log(f'Cadastro do seller "{seller.get_name()}" ao database.')


def list_sellers(search: str = None):
    sellers = dao_ac.read_sellers(search)
    ac_log.create_log('Listado todos os sellers.')
    return sellers

def delete_seller(id: int):
    dao_ac.delete(id)
    ac_log.create_log(f'Deletando seller com id "{id}".')

def update_seller(id: int, info):
    info_list = []
    info_list.append(info.get('name'))
    info_list.append(info.get('email'))
    info_list.append(info.get('phone'))
    dao_ac.update(id, info_list)
    ac_log.create_log(f'Alterando informações de seller com id "{id}".')