import sys

sys.path.append('.')

from back_end.log import generate_log
import back_end.db as db

def create_marketplace(name: str, description: str):
    maketplace = f'{name};{description}\n'
    db.add_marketplace(maketplace)

<<<<<<< HEAD
=======
def create_marketplace(name: str, description: str):
    maketplace = f'{name};{description}\n'
    db.add_marketplace(maketplace)

>>>>>>> main

def create_product(name: str, description: str, price: float):
    product = f'{name};{description};{price}'
    db.add_product(product)
    generate_log(f'Adicionado o produto "{name}" ao database.')
    pass


def verify():
    pass
<<<<<<< HEAD
=======


a = create_marketplace('b', 'a')
>>>>>>> main
