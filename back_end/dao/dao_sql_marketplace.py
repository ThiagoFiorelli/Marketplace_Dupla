import psycopg2

_host = 'pgsql08-farm15.uni5.net '
_user = 'topskills5'
_password = 'olist123'
_database = 'topskills5'
_connection_string = f'host={_host} user={_user} password={_password} dbname={_database}'

def add_marketplace(marketplace: str) -> None:
    mkt_aux = marketplace.split(';')
    _connection_string
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO marketplaces (name_mktplaces, description) values('{mkt_aux[0]}','{mkt_aux[1]}');")
    conn.commit()
    cursor.close()
    conn.close()


def read_marketplace() -> list:
    _connection_string
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM marketplaces")
    list_mkt = cursor.fetchall()

    l_dict_mkt = []

    for i in list_mkt:
        l_dict_mkt.append({'nome':i[1], 'descricao':i[2]})

    conn.commit()
    cursor.close()
    conn.close()

    return l_dict_mkt