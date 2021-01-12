import psycopg2
from ..model.Marketplace import Marketplace

_host = 'pgsql08-farm15.uni5.net '
_user = 'topskills5'
_password = 'olist123'
_database = 'topskills5'
_connection_string = f'host={_host} user={_user} password={_password} dbname={_database}'

def add_marketplace(mkp: Marketplace) -> None:
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO marketplaces (name_mktplaces, description) values('{mkp.name}','{mkp.description}');")
    conn.commit()
    cursor.close()
    conn.close()


def read_marketplace() -> list:
    _connection_string
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM marketplaces")
    list_mkt = cursor.fetchall()

    l_mkt = []

    for i in list_mkt:
        mkp = Marketplace(i[1],i[2])
        l_mkt.append(mkp)

    conn.commit()
    cursor.close()
    conn.close()

    return l_mkt