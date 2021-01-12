import sys
sys.path.append('.')

import back_end.dao.dao_sql_product as dao_ac_txt
import back_end.dao.dao_log as dao_ac_log

def create_product(name: str, description: str, price: float):
    product = f'{name};{description};{price}'
    dao_ac_txt.add_product(product)
    dao_ac_log.generate_log(f'Cadastro do produto "{name}" ao database.')


def list_products():
    products =  dao_ac_txt.read_products()
    dao_ac_log.generate_log('Listado todos os produtos.')
    return products