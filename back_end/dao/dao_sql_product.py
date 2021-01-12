import psycopg2
from back_end.models.product import Product

_host = 'pgsql08-farm15.uni5.net '
_user = 'topskills5'
_password = 'olist123'
_database = 'topskills5'
_connection_string = f'host={_host} user={_user} password={_password} dbname={_database}'

def add_product(product: Product) -> None:
    _connection_string
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()

    name = product.get_name()
    description = product.get_description()
    price = product.get_price()

    cursor.execute(f"INSERT INTO products (name_prod, description, price) values('{name}','{description}', {price});")
    conn.commit()
    cursor.close()
    conn.close()


def read_products() -> list:
    _connection_string
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    list_prod = cursor.fetchall()

    l_dict_prod = []

    for prod in list_prod:
        product = Product(prod[1], prod[2], prod[3])
        l_dict_prod.append(product)

    conn.commit()
    cursor.close()
    conn.close()

    return l_dict_prod