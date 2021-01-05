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


def verify():
    pass
