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

def delete_seller(id: int) -> list:
    sellers = dao_ac.delete(id)
    ac_log.create_log(f'Deletando seller com id "{id}".')
    return sellers