import sys
sys.path.append('.')

import back_end.dao.dao_sql_seller as dao_ac_txt
import back_end.controller.ctrl_log as ac_log
from back_end.models.seller import Seller

def create_seller(seller: Seller):
    dao_ac_txt.add_seller(seller)
    ac_log.create_log(f'Cadastro do seller "{seller.get_name()}" ao database.')


def list_sellers():
    sellers = dao_ac_txt.read_sellers()
    ac_log.create_log('Listado todos os sellers.')
    return sellers
