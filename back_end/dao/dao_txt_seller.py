
sellers_db = 'data/sellers.txt'


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
