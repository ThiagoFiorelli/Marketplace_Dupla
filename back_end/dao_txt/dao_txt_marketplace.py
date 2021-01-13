s.Marketplace import Marketplace

marketplaces_txt = 'data/marketplaces.txt'

def add_marketplace(marketplace: Marketplace) -> None:
    with open(marketplaces_txt, 'a', encoding='utf-8') as marketplaces_file:
        marketplaces_file.write(f'{marketplace}\n')

def read_marketplace() -> list:
    with open(marketplaces_txt, 'r', encoding='utf-8') as marketplaces_file:
        marketplaces = []
        for mkt in marketplaces_file:
            name, description = mkt.strip().split(';')
            mkplace = Marketplace(name, description)
            marketplaces.append(mkplace)
    return marketplaces
