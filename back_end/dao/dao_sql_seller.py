from back_end.models.seller import Seller
from back_end.dao.connection import connect_db

def add_seller(seller: Seller) -> None:
    db = connect_db()
    with db as conn:
        cursor = conn.cursor()
        name = seller.get_name()
        email = seller.get_email()
        phone = seller.get_phone()

        cursor.execute(f"INSERT INTO seller (name_seller, email, phone) values('{name}','{email}', '{phone}');")
        conn.commit()

def read_sellers(search: str = None) -> list:
    db = connect_db()
    with db as conn:
        cursor = conn.cursor()
        if search == None:
            cursor.execute("SELECT * FROM seller;")
        else:
            cursor.execute(f"SELECT * FROM seller WHERE name_seller LIKE '%{search}%' OR email LIKE '%{search}%' OR phone LIKE '%{search}%'")
        list_seller = cursor.fetchall()
        sellers = []

        for i in list_seller:
            seller = Seller(i[1], i[2], i[3], i[0])
            sellers.append(seller)
        conn.commit()
    return sellers

def delete(id: int):
    db = connect_db()
    with db as conn:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM seller WHERE id = {id};")
        conn.commit()

def update(id: int, info: list):
    db = connect_db()
    with db as conn:
        cursor = conn.cursor()
        name = info[0]
        email = info[1]
        phone = info[2]
        cursor.execute(f"UPDATE seller set name_seller = '{name}', email = '{email}', phone = '{phone}' WHERE id = {id};")
        conn.commit()