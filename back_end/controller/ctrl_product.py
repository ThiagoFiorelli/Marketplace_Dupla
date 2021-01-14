import sys
sys.path.append('.')

from back_end.models.product import Product
from back_end.dao.product_dao import ProductDao
from back_end.controller.base_controller import BaseController

class ProductController(BaseController):
    def __init__(self) -> None:
        self.__dao = ProductDao()
        super().__init__(self.__dao)
