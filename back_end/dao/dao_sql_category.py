from ..models.Category import Category
from back_end.dao.connection import Connection

def add_category(category: Category)-> None:
    with Connection as conn:
        cursor=conn.cursor()
        cursor.execute(f"INSERT INTO category (name_category,description) values('{category.name}','{category.description}');")
        conn.commit()

def read_categories() -> list:
    with Connection as conn:
        cursor= conn.cursor()
        cursor.execute("SELECT * FROM category")
        list_cat= cursor.fetchall() 
        lista=[]
        for i in list_cat:
            cat = Category(i[1], i[2])
            cat.id = i[0]
            lista.append(cat)
        return lista

def update(category: Category)->None:
    with Connection as conn:
        cursor=conn.cursor()
        cursor.execute(f"UPDATE category SET name_category='{category.name}', description='{category.description}' WHERE id={category.id};")
        conn.commit() 

def delete(category: Category)->None:
    with Connection as conn:
        cursor=conn.cursor()
        cursor.execute(f"DELETE FROM category WHERE id={category.id};")
        conn.commit() 

def search_by_id(id:int)->Category:
    with Connection as conn:
        cursor= conn.cursor()
        cursor.execute(f"SELECT * FROM category WHERE id={id}")
        cat=cursor.fetchone()
    category = Category(cat[1], cat[2])
    category.id = cat[0]
    return category