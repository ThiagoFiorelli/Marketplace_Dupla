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


def read_products() -> list:
    string_connection = connect_db()
    with psycopg2.connect(string_connection) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        list_prod = cursor.fetchall()
        l_dict_prod = []

        for prod in list_prod:
            product = Product(prod[1], prod[2], prod[3])
            l_dict_prod.append(product)

        conn.commit()
        return l_dict_prod