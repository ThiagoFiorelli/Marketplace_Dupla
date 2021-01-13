import sys
sys.path.append('.')

import back_end.dao.dao_sql_product as dao_ac
import back_end.controller.ctrl_log as ac_log
from back_end.models.product import Product

def create_product(product: Product):
    dao_ac.add_product(product)
    ac_log.create_log(f'Cadastro do produto "{product.get_name()}" ao database.')

def list_products():
    products = dao_ac.read_products()
    ac_log.create_log('Listado todos os produtos.')
    return products