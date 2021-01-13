import sys

sys.path.append('.')

from flask import Flask, render_template, request, redirect
import back_end.controller.ctrl_category as ct_category
import back_end.controller.ctrl_product as ct_product
import back_end.controller.ctrl_marketplace as ct_marketplace
import back_end.controller.ctrl_seller as ct_seller
import back_end.dao.dao_sql_log as ac_log
from back_end.models.Marketplace import Marketplace
from back_end.models.Category import Category
from back_end.models.product import Product
from back_end.models.seller import Seller
from back_end.models.log import Log

app = Flask(__name__)
titulo_head = 'Lojinha'

@app.route('/cadastrar_marketplace')
def cadastro_Marketplace():
    menssagem = ''
    marketplace_add = request.args.get('market')
    description_market = request.args.get('description')
    if marketplace_add is not None and description_market is not None:
        mkp = Marketplace(marketplace_add, description_market)
        ct_marketplace.create_marketplace(mkp)
        menssagem = f'{mkp.name} cadastrado com sucesso'
    return render_template('create_marketplace.html', menssagem=menssagem, titulo='Cadastro de Marketplaces', titulo_head=titulo_head)


@app.route('/cadastrar_produto')
def cadastro_Produto():
    menssagem = ''
    product_name = request.args.get('name')

    if product_name is not None:
        product_description = request.args.get('description')
        product_price = request.args.get('price')
        product = Product(product_name, product_description, product_price)
        ct_product.create_product(product)
        menssagem = f'{product_name} cadastrado com sucesso'
    return render_template('create_product.html', menssagem=menssagem, titulo='Cadastro de Produtos', titulo_head=titulo_head)


@app.route('/cadastrar_categoria')
def cadastro_Categoria():
    mensagem = ''
    category_name = request.args.get('name')

    if category_name is not None:
        category_description = request.args.get('description')
        cat = Category(category_name, category_description)
        ct_category.create_category(cat)
        mensagem = f'{cat.name} cadastrado com sucesso'
    return render_template('create_category.html', menssagem=mensagem, titulo='Cadastro de Categorias', titulo_head=titulo_head)

@app.route('/cadastrar_seller')
def cadastro_Seller():
    message = ''
    seller_name = request.args.get('name')
    seller_phone = request.args.get('phone')
    seller_email = request.args.get('email')

    if seller_name is not None and seller_phone is not None and seller_email is not None:
        seller = Seller(seller_name, seller_email, seller_phone)
        ct_seller.create_seller(seller)
        message = f'{seller_name} adicionado com sucesso'

    return render_template('create_seller.html', menssagem=message, titulo='Cadastro Seller', titulo_head=titulo_head)


@app.route('/listar_marketplaces')
def lista_marketplaces():
    marketplaces = ct_marketplace.list_marketplaces()
    return render_template('list_marketplaces.html', marketplaces=marketplaces, titulo='Marketplaces',
                           titulo_head=titulo_head)

@app.route('/listar_sellers', methods=['GET', 'POST'])
def lista_sellers():
    if request.method == 'POST':
        search = request.form.get('search')
        sellers = ct_seller.list_sellers(search)
        redirect('/listar_sellers')
    else:
        sellers = ct_seller.list_sellers()
    return render_template('list_sellers.html', sellers=sellers, titulo='Sellers', titulo_head=titulo_head)

@app.route('/delete_seller/<identifier>')
def delete_seller(identifier):
    ct_seller.delete_seller(identifier)
    return redirect('/listar_sellers')

@app.route('/alterar_seller/<identifier>', methods=['GET', 'POST'])
def alterar_seller(identifier):
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        seller = Seller(name, email, phone)
        ct_seller.update_seller(identifier, seller)
        return redirect('/listar_sellers')
    return render_template('create_seller.html', identifier = identifier, titulo='Alteração de Seller', titulo_head=titulo_head)

@app.route('/listar_produtos', methods=['GET', 'POST'])
def lista_produtos():
    if request.method == 'POST':
        search = request.form.get('search')
        products = ct_product.list_products(search)
        redirect('/listar_produtos')
    else:
        products = ct_product.list_products()
    return render_template('list_products.html', products=products, titulo="Produtos", titulo_head=titulo_head)

@app.route('/delete_product/<identifier>')
def delete_product(identifier):
    ct_product.delete_product(identifier)
    return redirect('/listar_produtos')

@app.route('/alterar_produto/<identifier>', methods=['GET', 'POST'])
def alterar_produto(identifier):
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        product = Product(name, description, price)
        ct_product.update_product(identifier, product)
        return redirect('/listar_produtos')
    return render_template('create_product.html', identifier = identifier, titulo='Alteração de Produto', titulo_head=titulo_head)

@app.route('/listar_categorias')
def lista_categorias():
    list_cat = ct_category.list_categories()
    return render_template('list_categories.html', categories=list_cat, titulo="Categorias", titulo_head=titulo_head)


@app.route('/listar_logs')
def lista_logs():
    logs: Log = ac_log.read_logs()
    
    return render_template('list_logs.html', logs=logs, titulo="Histórico", titulo_head=titulo_head)


@app.route('/')
def home():
    return render_template('home.html', titulo_head=titulo_head)


app.run()