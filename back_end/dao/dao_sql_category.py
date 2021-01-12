import psycopg2
from ..model.Category import Category


_host= 'pgsql08-farm15.uni5.net'
_user='topskills5'
_psw='olist123'
_database='topskills5'
_connection_string=f"host={_host} user={_user} dbname={_database} password={_psw}"

def add_category(category: Category)-> None:
    conn= psycopg2.connect(_connection_string)
    cursor=conn.cursor()
    
    cursor.execute(f"INSERT INTO category (name_category,description) values('{category.name}','{category.description}');")
    conn.commit()
    cursor.close()
    conn.close()


def read_categories() -> list:
    _connection_string
    conn= psycopg2.connect(_connection_string)
    cursor=conn.cursor()
    
    cursor.execute("SELECT * FROM category")
    list_cat =cursor.fetchall() 
    
    lista=[]

    for i in list_cat:
        cat = Category(i[1], i[2])
        lista.append(cat)

    conn.commit()
    cursor.close()
    conn.close()

    return lista

         


