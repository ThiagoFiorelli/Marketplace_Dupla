from ..models.Marketplace import Marketplace
from back_end.dao.connection import connect_db

def add_marketplace(mkp: Marketplace) -> None:
    db = connect_db()
    with db as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO marketplaces (name_mktplaces, description) values('{mkp.name}','{mkp.description}');")
        conn.commit()

def read_marketplaces() -> list:
    db = connect_db()
    with db as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM marketplaces")
        list_mkt = cursor.fetchall()
        mkts = []
        for i in list_mkt:
            mkp = Marketplace(i[1], i[2])
            mkts.append(mkp)
        conn.commit()
        return mkts