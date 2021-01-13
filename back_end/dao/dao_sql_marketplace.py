import psycopg2
from ..model.Marketplace import Marketplace
from back_end.dao.connection import connect_db

def add_marketplace(mkp: Marketplace) -> None:
    string_connection = connect_db()
    with psycopg2.connect(string_connection) as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO marketplaces (name_mktplaces, description) values('{mkp.name}','{mkp.description}');")
        conn.commit()

def read_marketplaces() -> list:
    string_connection = connect_db()
    with psycopg2.connect(string_connection) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM marketplaces")
        list_mkt = cursor.fetchall()
        mkts = []
        for i in list_mkt:
            mkp = Marketplace(i[1], i[2])
            mkts.append(mkp)
        conn.commit()
        return mkts