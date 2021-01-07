import sys

sys.path.append('.')

from back_end.log import generate_log
import back_end.db as db


def create_marketplace(name: str, description: str):
    marketplace = f'{name};{description}'
    db.add_marketplace(marketplace)
    generate_log(f'Adicionado o marketplace "{name}" ao database.')


def create_product(name: str, description: str, price: float):
    product = f'{name};{description};{price}'
    db.add_product(product)
    generate_log(f'Adicionado o produto "{name}" ao database.')


def create_category(name: str, description: str):
    category = f'{name};{description}'
    db.add_category(category)
    generate_log(f'Adicionado a categoria "{name}" ao database.')


def create_seller(name: str, phone: str, email: str):
    seller = f'{name};{phone};{email}'
    db.add_seller(seller)
    generate_log(f'Cadastro do seller "{name}" ao database.')


def list_marketplaces():
    marketplaces = db.read_marketplace()
    generate_log('Listado todos os marketplaces.')
    return marketplaces


def list_products():
    products = db.read_products()
    generate_log('Listado todos os produtos.')
    return products


def list_sellers():
    sellers = db.read_seller()
    generate_log('Listado todos os sellers.')
    return sellers


def list_categories():
    categories = db.read_categories()
    generate_log('Listado todas as categorias.')
    return categories


def verify():
    pass
