import sys

sys.path.append('.')

from back_end.log import generate_log, read_logs
import back_end.controller.ctrl_category as db
import back_end.controller.ctrl_product as db_prod



def create_marketplace(name: str, description: str):
    marketplace = f'{name};{description}'
    db.add_marketplace(marketplace)
    generate_log(f'Cadastro do marketplace "{name}" ao database.')

def create_seller(name: str, phone: str, email: str):
    seller = f'{name};{phone};{email}'
    db.add_seller(seller)
    generate_log(f'Cadastro do seller "{name}" ao database.')


def list_marketplaces():
    marketplaces = db.read_marketplace()
    generate_log('Listado todos os marketplaces.')
    return marketplaces


def list_sellers():
    sellers = db.read_seller()
    generate_log('Listado todos os sellers.')
    return sellers

#pode ser tirado do codigo
def list_logs():
    logs = read_logs()
    return logs


def verify():
    pass
