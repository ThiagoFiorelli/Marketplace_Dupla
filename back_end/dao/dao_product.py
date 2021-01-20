from back_end.dao.base_dao import BaseDao
from back_end.models.product import Product


class ProductDao(BaseDao):
    def __init__(self):
        super().__init__(Product)