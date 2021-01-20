from back_end.controller.base_controller import BaseController
from back_end.dao.dao_category import CategoryDao

import sys
sys.path.append('.')


class CategoryController(BaseController):
    def __init__(self):
        self.__dao = CategoryDao()
        super().__init__(self.__dao, 'Category')
