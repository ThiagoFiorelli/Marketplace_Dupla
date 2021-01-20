from back_end.dao.base_dao import BaseDao
from back_end.models.seller import Seller


class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)