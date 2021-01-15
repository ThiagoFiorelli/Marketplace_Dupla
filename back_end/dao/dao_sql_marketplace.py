from ..models.Marketplace import Marketplace
from back_end.dao.connection import Connection
from .base_dao import BaseDao

class MarketplaceDao(BaseDao):
    def create(self, model:Marketplace) -> list:
        query = f"INSERT INTO marketplaces (name_mktplaces, description) values('{mkp.name}','{mkp.description}');"
        super().execute(query)

    def read_by_id(self, id:int)->Marketplace:
        query = f"SELECT * FROM marketplaces WHERE id={id};"
        result = super().read(query)[0]
        mkp = Marketplace(result[1], result[2])
        mkp.id = result[0]
        return mkp

    def read_all(self)->list:
        query = f"SELECT * FROM marketplaces;"
        result_list = super().read(query)
        marketplaces = []
        for result in result_list:
            mkp = Marketplace(result[1], result[2])
            mkp.id = result[0]
            marketplaces.append(mkp)
        return marketplaces
    
    def delete(self, id:int)->None:
        query = f"DELETE FROM marketplaces WHERE id={id};"
        super().execute(query)

    def update(self, model:Marketplace)->None:
        query = f"UPDATE marketplaces SET name_mktplaces='{model.name}', description='{model.description}' WHERE id={model.id};"
        super().execute(query)

# from ..models.Marketplace import Marketplace
# from back_end.dao.connection import Connection

# def add_marketplace(mkp: Marketplace) -> None:
#     with Connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute(f"INSERT INTO marketplaces (name_mktplaces, description) values('{mkp.name}','{mkp.description}');")
#         conn.commit()

# def read_marketplaces() -> list:
#     with Connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM marketplaces")
#         list_mkt = cursor.fetchall()
#         mkts = []
#         for i in list_mkt:
#             mkp = Marketplace(i[1], i[2])
#             mkp.id = i[0]
#             mkts.append(mkp)
#         return mkts

# def update(marketplace: Marketplace)->None:
#     with Connection() as conn:
#         cursor=conn.cursor()
#         cursor.execute(f"UPDATE marketplaces SET name_mktplaces='{marketplace.name}', description='{marketplace.description}' WHERE id={marketplace.id};")
#         conn.commit() 

# def delete(marketplace: Marketplace)->None:
#     with Connection() as conn:
#         cursor=conn.cursor()
#         cursor.execute(f"DELETE FROM marketplaces WHERE id={marketplace.id};")
#         conn.commit() 

# def search_by_id(id:int)->Marketplace:
#     with Connection() as conn:
#         cursor= conn.cursor()
#         cursor.execute(f"SELECT * FROM marketplaces WHERE id={id}")
#         mkp=cursor.fetchone()
#     marketplace = Marketplace(mkp[1], mkp[2])
#     marketplace.id = mkp[0]
#     return marketplace