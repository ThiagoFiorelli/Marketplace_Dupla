import psycopg2
from back_end.models.seller import Seller
from back_end.dao.connection import connect_db

def add_seller(seller: Seller) -> None:
    string_connection = connect_db()
    with psycopg2.connect(string_connection) as conn:
        cursor = conn.cursor()
        name = seller.get_name()
        email = seller.get_email()
        phone = seller.get_phone()

        cursor.execute(f"INSERT INTO seller (name_seller, email, phone) values('{name}','{email}', '{phone}');")
        conn.commit()

def read_sellers() -> list:
    string_connection = connect_db()
    with psycopg2.connect(string_connection) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM seller")
        list_seller = cursor.fetchall()
        sellers = []

        for i in list_seller:
            seller = Seller(i[1], i[2], i[3])
            sellers.append(seller)
        conn.commit()
    return sellers