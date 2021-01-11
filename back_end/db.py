import sys

sys.path.append('.')
from back_end.log import generate_log

marketplaces_txt = 'data/marketplaces.txt'
sellers_db = 'data/sellers.txt'


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



