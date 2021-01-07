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
    description_market = request.args.get('description')
    if marketplace_add is not None and description_market is not None:
        actions.create_marketplace(marketplace_add, description_market)
        menssagem = f'{marketplace_add} cadastrado com sucesso'
    return render_template('create_marketplace.html', menssagem=menssagem, titulo='Cadastro de Marketplaces', titulo_head=titulo_head)


@app.route('/cadastrar_produto')
def cadastro_Produto():
    menssagem = ''
    product_name = request.args.get('name')

    if product_name is not None:
        product_description = request.args.get('description')
        product_price = request.args.get('price')
        actions.create_product(product_name, product_description, product_price)
        menssagem = f'{product_name} cadastrado com sucesso'
    return render_template('create_product.html', menssagem=menssagem, titulo='Cadastro de Produtos', titulo_head=titulo_head)


@app.route('/cadastrar_categoria')
def cadastro_Categoria():
    mensagem = ''
    category_name = request.args.get('name')

    if category_name is not None:
        category_description = request.args.get('description')
        actions.create_category(category_name, category_description)
        mensagem = f'{category_name} cadastrado com sucesso'
    return render_template('create_category.html', menssagem=mensagem, titulo='Cadastro de Categorias', titulo_head=titulo_head)

@app.route('/cadastrar_seller')
def cadastro_Seller():
    message = ''
    seller_name = request.args.get('name')
    seller_phone = request.args.get('phone')
    seller_email = request.args.get('email')

    if seller_name is not None and seller_phone is not None and seller_email is not None:
        actions.create_seller(seller_name, seller_phone, seller_email)
        message = f'{seller_name} adicionado com sucesso'

    return render_template('create_seller.html', menssagem=message, titulo='Cadastro Seller', titulo_head=titulo_head)


@app.route('/listar_marketplaces')
def lista_marketplaces():
    marketplaces = actions.list_marketplaces()
    return render_template('list_marketplaces.html', marketplaces=marketplaces, titulo='Marketplaces',
                           titulo_head=titulo_head)


@app.route('/listar_produtos')
def lista_produtos():
    products = actions.list_products()
    return render_template('list_products.html', products=products, titulo="Produtos", titulo_head=titulo_head)


@app.route('/listar_categorias')
def lista_categorias():
    categories = actions.list_categories()
    return render_template('list_categories.html', categories=categories, titulo="Categorias", titulo_head=titulo_head)


@app.route('/')
def home():
    return render_template('home.html', titulo_head=titulo_head)


app.run(debug=True)