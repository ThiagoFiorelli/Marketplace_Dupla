import psycopg2

def connect_db():
    host= 'pgsql08-farm15.uni5.net'
    user='topskills5'
    psw='olist123'
    database='topskills5'
    connection_string = f"host={host} user={user} dbname={database} password={psw}"
    db = psycopg2.connect(connection_string)
    return db