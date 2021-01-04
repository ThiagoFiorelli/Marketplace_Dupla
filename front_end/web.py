import sys

sys.path.append('.')
from flask import Flask, render_template, request
import back_end.actions as actions

app = Flask(__name__)
titulo_head = 'Lojinha'

@app.route('/cadastrar_marketplace')
def cadastro_Marketplace():
    menssagem = ''
    marketplace_add = request.args.get('market')
    description_market = request.args.get('descrption')
    if marketplace_add is not None and description_market is not None:
        actions.create_marketplace(marketplace_add,description_market)
        menssagem = f'{marketplace_add} cadastrado com sucesso'
    return render_template('create_marketplace.html', menssagem=menssagem, titulo='Cadastro de Marketplaces')

@app.route('/cadastrar_produto')
def cadastro_Produto():
    menssagem = ''
    product_name = request.args.get('name')

    if product_name is not None:
        product_descrpition = request.args.get('description')
        product_price = request.args.get('price')
        actions.create_product(product_name, product_descrpition, product_price)
        menssagem = f'{product_name} cadastrado com sucesso'
    return render_template('create_product.html', menssagem=menssagem)

@app.route('/')
def home():
    return render_template('home.html', titulo_head='titulo_head')


app.run(debug=True)