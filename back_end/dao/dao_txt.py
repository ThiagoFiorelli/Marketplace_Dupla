import sys
sys.path.append('/Markeplace_Dupla/back_end/')

product_db = 'data/product.txt'
categories_db = 'data/categories.txt'
marketplaces_txt = '../marketplaces.txt'
sellers_db = '../sellers.txt'

#nao achamos a chamda no codigo, talvez possa ser tirado
def verify_db():
    with open(product_db, 'r', encoding='utf-8') as products_file:
        return products_file

def add_product(product: str) -> None:
    with open(product_db, 'a', encoding='utf-8') as products_file:
        products_file.write(f'{product}\n')


def read_products() -> list:
    with open(product_db, 'r', encoding='utf-8') as products_file:
        products = []
        for product in products_file:
            name, description, price = product.strip().split(';')
            products.append({'name': name, 'description': description, 'price': float(price)})
        return products

def add_category(category: str) -> None:
    with open(categories_db, 'a', encoding='utf-8') as categories_file:
        categories_file.write(f'{category}\n')


def read_categories() -> list:
    with open(categories_db, 'r', encoding='utf-8') as categories_file:
        categories = {}
        for category in categories_file:
            name, description = category.strip().split(';')
            categories[name] = description

    return categories


def add_marketplace(marketplace: str) -> None:
    with open(marketplaces_txt, 'a', encoding='utf-8') as marketplaces_file:
        marketplaces_file.write(f'{marketplace}\n')


def read_marketplace() -> list:
    with open(marketplaces_txt, 'r', encoding='utf-8') as marketplaces_file:
        marketplaces = {}
        for mkt in marketplaces_file:
            name, description = mkt.strip().split(';')
            marketplaces[name] = description

    return marketplaces


def add_seller(seller: str) -> None:
    with open(sellers_db, 'a', encoding='utf-8') as sellers_file:
        sellers_file.write(f'{seller}\n')


def read_seller() -> list:
    with open(sellers_db, 'r', encoding='utf-8') as sellers_file:
        sellers = []
        for seller in sellers_file:
            name, phone, email = seller.strip().split(';')
            sellers.append({'name': name, 'phone': phone, 'email': email})

    return sellers
