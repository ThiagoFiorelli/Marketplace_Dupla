import psycopg2
from back_end.models.seller import Seller
from connection import connect_db

def add_seller(seller: Seller) -> None:
    string_connection = connect_db()
    with psycopg2.connect(string_connection) as conn:
        cursor = conn.cursor()

        name = seller.get_name()
        email = seller.get_email()
        phone = seller.get_phone()

        cursor.execute(f"INSERT INTO seller (name_seller, email, phone) values('{name}','{email}', '{phone}');")
        conn.commit()


def read_seller() -> list:
    string_connection = connect_db()
    with psycopg2.connect(string_connection) as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM seller")
        list_seller = cursor.fetchall()

        l_dict_seller = []

        for i in list_seller:
            seller = Seller(i[1], i[2], i[3])
            l_dict_seller.append(seller)

        conn.commit()

    return l_dict_seller