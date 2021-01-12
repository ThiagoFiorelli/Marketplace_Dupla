import psycopg2

_host = 'pgsql08-farm15.uni5.net '
_user = 'topskills5'
_password = 'olist123'
_database = 'topskills5'
_connection_string = f'host={_host} user={_user} password={_password} dbname={_database}'

def add_product(product: str)->None:
    prod_aux = product.split(';')
    _connection_string
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO products (name_prod, description, price) values('{prod_aux[0]}','{prod_aux[1]}', {prod_aux[2]});")
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

    for i in list_prod:
        l_dict_prod.append({'nome':i[1], 'description':i[2], 'price':i[3]})

    conn.commit()
    cursor.close()
    conn.close()

    return l_dict_prod