import psycopg2
from back_end.models.product import Product
from back_end.dao.connection import connect_db

def add_product(product: Product) -> None:
    string_connection = connect_db()
    with psycopg2.connect(string_connection) as conn:
        cursor = conn.cursor()
        name = product.get_name()
        description = product.get_description()
        price = product.get_price()

        cursor.execute(f"INSERT INTO products (name_prod, description, price) values('{name}','{description}', {price});")
        conn.commit()

def read_products(search: str = None) -> list:
    string_connection = connect_db()
    with psycopg2.connect(string_connection) as conn:
        cursor = conn.cursor()
        if search == None:
            cursor.execute("SELECT * FROM products")
        else:
            cursor.execute(f"SELECT * FROM products WHERE name_prod LIKE '%{search}%' OR description LIKE '%{search}%';")
        list_prod = cursor.fetchall()
        products = []

        for prod in list_prod:
            product = Product(prod[1], prod[2], prod[3], prod[0])
            products.append(product)

        conn.commit()
    return products

def delete(id: int):
    string_connection = connect_db()
    with psycopg2.connect(string_connection) as conn:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM products WHERE id = {id};")
        conn.commit()

def update(id: int, info: list):
    string_connection = connect_db()
    with psycopg2.connect(string_connection) as conn:
        cursor = conn.cursor()
        name = info[0]
        description = info[1]
        price = info[2]
        cursor.execute(f"UPDATE products set name_prod = '{name}', description = '{description}', price = {price} WHERE id = {id};")
        conn.commit()