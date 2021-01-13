from ..models.Category import Category
from back_end.dao.connection import connect_db

def add_category(category: Category)-> None:
    db = connect_db()
    with db as conn:
        cursor=conn.cursor()
        cursor.execute(f"INSERT INTO category (name_category,description) values('{category.name}','{category.description}');")
        conn.commit()

def read_categories() -> list:
    db = connect_db()
    with db as conn:
        cursor= conn.cursor()
        cursor.execute("SELECT * FROM category")
        list_cat= cursor.fetchall() 
        lista=[]
        for i in list_cat:
            cat = Category(i[1], i[2])
            lista.append(cat)
        conn.commit()
        return lista