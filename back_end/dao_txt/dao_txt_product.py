product_db = 'data/product.txt'

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

