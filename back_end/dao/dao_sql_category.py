from ..models.Category import Category
from back_end.dao.connection import Connection
from .base_dao import BaseDao

class CategoryDao(BaseDao):
    def create(self, model:Category) -> list:
        query = f"""INSERT INTO category
                    (name_category,description)
                    VALUES
                    ('{model.name}','{model.description}');")"""
        super().execute(query)

    def read_by_id(self, id:int)->Category:
        query = f"SELECT id, name_category, description FROM category WHERE id={id};"
        result = super().read(query)[0]
        category = Category(result[1], result[2])
        category.id = result[0]
        return category

    def read_all(self)->list:
        query = f"SELECT id, name_category, description FROM category;"
        result_list = super().read(query)
        categories = []
        for result in result_list:
            category = Category(result[1], result[2])
            category.id = result[0]
            categories.append(category)
        return categories
    
    def delete(self, id:int)->None:
        query = f"DELETE from category WHERE id = {id};"
        super().execute(query)

    def update(self, model:Category)->None:
        query = f"UPDATE category SET name_category='{category.name}', description='{category.description}' WHERE id={category.id};"
        super().execute(query)

# def update(category: Category)->None:
#     with Connection() as conn:
#         cursor=conn.cursor()
#         cursor.execute(f"UPDATE category SET name_category='{category.name}', description='{category.description}' WHERE id={category.id};")
#         conn.commit() 

# from ..models.Category import Category
# from back_end.dao.connection import Connection

# def add_category(category: Category)-> None:
#     with Connection() as conn:
#         cursor=conn.cursor()
#         cursor.execute(f"INSERT INTO category (name_category,description) values('{category.name}','{category.description}');")
#         conn.commit()

# def read_categories() -> list:
#     with Connection() as conn:
#         cursor= conn.cursor()
#         cursor.execute("SELECT * FROM category")
#         list_cat= cursor.fetchall() 
#         lista=[]
#         for i in list_cat:
#             cat = Category(i[1], i[2])
#             cat.id = i[0]
#             lista.append(cat)
#         return lista

# def update(category: Category)->None:
#     with Connection() as conn:
#         cursor=conn.cursor()
#         cursor.execute(f"UPDATE category SET name_category='{category.name}', description='{category.description}' WHERE id={category.id};")
#         conn.commit() 

# def delete(category: Category)->None:
#     with Connection() as conn:
#         cursor=conn.cursor()
#         cursor.execute(f"DELETE FROM category WHERE id={category.id};")
#         conn.commit() 

# def search_by_id(id:int)->Category:
#     with Connection() as conn:
#         cursor= conn.cursor()
#         cursor.execute(f"SELECT * FROM category WHERE id={id}")
#         cat=cursor.fetchone()
#     category = Category(cat[1], cat[2])
#     category.id = cat[0]
#     return category