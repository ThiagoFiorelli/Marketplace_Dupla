import sys

sys.path.append('.')

from back_end.log import generate_log
import back_end.db as db


def create_marketplace():
    pass


def create_product(name: str, description: str, price: float):
    product = f'{name};{description};{price}'
    db.add_product(product)
    generate_log(f'Adicionado o produto "{name}" ao database.')
    pass


def verify():
    pass
