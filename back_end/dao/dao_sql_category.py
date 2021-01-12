import psycopg2

_host= 'pgsql08-farm15.uni5.net'
_user='topskills5'
_psw='olist123'
_database='topskills5'
_connection_string=f"host={_host} user={_user} dbname={_database} password={_psw}"

def add_category(category: str)-> None:

    cat_aux=category.split(';')
    _connection_string    
    conn= psycopg2.connect(_connection_string)
    cursor=conn.cursor()
    
    cursor.execute(f"INSERT INTO category (name_category,description) values('{cat_aux[0]}','{cat_aux[1]}');")
    conn.commit()
    cursor.close()
    conn.close()


def read_categories() -> list:
    _connection_string
    conn= psycopg2.connect(_connection_string)
    cursor=conn.cursor()
    
    cursor.execute("SELECT * FROM category")
    list_cat =cursor.fetchall() 
    
    l_dicionario=[]

    for i in list_cat:
       l_dicionario.append({'nome':i[1],'descricao':i[2]})

    conn.commit()
    cursor.close()
    conn.close()

    return l_dicionario

         


