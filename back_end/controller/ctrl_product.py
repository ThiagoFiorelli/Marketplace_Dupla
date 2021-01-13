import sys
sys.path.append('.')

import back_end.dao.dao_sql_product as dao_ac
import back_end.controller.ctrl_log as ac_log
from back_end.models.product import Product

def create_product(product: Product) -> None:
    dao_ac.add_product(product)
    ac_log.create_log(f'Cadastro do produto "{product.get_name()}" ao database.')

def list_products(search: str = None) -> list:
    products = dao_ac.read_products(search)
    ac_log.create_log('Listado todos os produtos.')
    return products

def delete_product(id: int):
    dao_ac.delete(id)
    ac_log.create_log(f'Deletando produto com id "{id}".')

def update_product(id: int, info):
    info_list = []
    info_list.append(info.get('name'))
    info_list.append(info.get('description'))
    info_list.append(info.get('price'))
    dao_ac.update(id, info_list)
    ac_log.create_log(f'Alterando informações de produto com id "{id}".')