from ..models.category import Category
from .base_dao import BaseDao

class CategoryDao(BaseDao):
    def create(self, model:Category) -> None:
        query = f"""INSERT INTO category
                    (name_category,description)
                    VALUES
                    ('{model.name}','{model.description}');")"""
        super().execute(query)

    def read_by_id(self, id:int)->Category:
        query = f"SELECT id, name_category, description FROM category WHERE id={id};"
        result = super().read(query)[0]
        category = Category(result[1], result[2], result[0])
        return category

    def read_all(self)->list:
        query = f"SELECT id, name_category, description FROM category;"
        result_list = super().read(query)
        categories = []
        for result in result_list:
            category = Category(result[1], result[2], result[0])
            categories.append(category)
        return categories
    
    def delete(self, id:int)->None:
        query = f"DELETE from category WHERE id = {id};"
        super().execute(query)

    def update(self, model:Category)->None:
        query = f"UPDATE category SET name_category='{model.name}', description='{model.description}' WHERE id={model.id};"
        super().execute(query)