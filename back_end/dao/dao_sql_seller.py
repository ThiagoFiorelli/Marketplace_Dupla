import psycopg2
from back_end.models.seller import Seller

_host = 'pgsql08-farm15.uni5.net '
_user = 'topskills5'
_password = 'olist123'
_database = 'topskills5'
_connection_string = f'host={_host} user={_user} password={_password} dbname={_database}'

def add_seller(seller: Seller) -> None:
    _connection_string
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()

    name = seller.get_name()
    email = seller.get_email()
    phone = seller.get_phone()

    cursor.execute(f"INSERT INTO seller (name_seller, email, phone) values('{name}','{email}', '{phone}');")
    conn.commit()
    cursor.close()
    conn.close()


def read_seller() -> list:
    _connection_string
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM seller")
    list_seller = cursor.fetchall()

    l_dict_seller = []

    for i in list_seller:
        seller = Seller(i[1], i[2], i[3])
        l_dict_seller.append(seller)

    conn.commit()
    cursor.close()
    conn.close()

    return l_dict_seller