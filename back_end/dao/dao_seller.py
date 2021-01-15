from back_end.dao.base_dao import BaseDao
from back_end.models.seller import Seller

class SellerDao(BaseDao):
    def create(self, seller: Seller) -> None:
        name = seller.get_name()
        email = seller.get_email()
        phone = seller.get_phone()

        query = f"INSERT INTO seller (name_seller, email, phone) values('{name}','{email}', '{phone}');"
        super().execute(query)

    def read(self, search: str = None) -> list[Seller]:
        if search == None:
            query = "SELECT * FROM seller;"
        else:
            query = f"SELECT * FROM seller WHERE name_seller LIKE '%{search}%' OR email LIKE '%{search}%' OR phone LIKE '%{search}%';"
        sellers = []
        list_seller = super().read(query)

        for seller in list_seller:
            seller = Seller(seller[1], seller[2], seller[3], seller[0])
            sellers.append(seller)
        return sellers
    
    def read_by_id(self, id: int) -> Seller:
        query = f"SELECT * FROM seller WHERE id = {id};"
        list_seller = super().read(query)[0]
        seller = Seller(list_seller[1], list_seller[2], list_seller[3], list_seller[0])
        return seller

    def delete(self, id: int) -> None:
        query = f"DELETE FROM seller WHERE id = {id};"
        super().execute(query)

    def update(self, id: int, seller: Seller) -> None:
        name = seller.get_name()
        email = seller.get_email()
        phone = seller.get_phone()
        query = f"UPDATE seller set name_seller = '{name}', email = '{email}', phone = '{phone}' WHERE id = {id};"
        super().execute(query)