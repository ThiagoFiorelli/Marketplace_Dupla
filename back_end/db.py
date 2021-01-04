add_product()

product_db = 'data/product.txt'

def add_product(product: str) -> None:
    with open(product_db, 'a', encoding='utf-8') as products_file:
        products_file.write(product)

def verify_db():
    with open(product_db, 'r', encoding='utf-8') as products_file:
        return products_file