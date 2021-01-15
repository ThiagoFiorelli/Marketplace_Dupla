import sys
sys.path.append('.')

from back_end.dao.dao_product import ProductDao
from back_end.controller.base_controller import BaseController

class ProductController(BaseController):
    def __init__(self) -> None:
        self.__dao = ProductDao()
        super().__init__(self.__dao)
