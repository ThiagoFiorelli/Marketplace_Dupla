import sys

sys.path.append('.')

from flask import Flask, render_template, request, redirect, url_for
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
    marketplace_add = request.args.get('name')
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

@app.route('/listar_sellers')
def lista_sellers():
    sellers: Seller = ct_seller.list_sellers()
    return render_template('list_sellers.html', sellers=sellers, titulo='Sellers', titulo_head=titulo_head)


@app.route('/listar_produtos')
def lista_produtos():
    products: Product = ct_product.list_products()
    return render_template('list_products.html', products=products, titulo="Produtos", titulo_head=titulo_head)

@app.route('/listar_categorias')
def lista_categorias():
    list_cat = ct_category.list_categories()
    return render_template('list_categories.html', categories=list_cat, titulo="Categorias", titulo_head=titulo_head)

@app.route('/listar_logs')
def lista_logs():
    logs: Log = ac_log.read_logs()
    
    return render_template('list_logs.html', logs=logs, titulo="Histórico", titulo_head=titulo_head)


@app.route('/deletar_marketplace/<identifier>')
def delete_marketplace(identifier):
    ct_marketplace.delete_marketplace(identifier)
    return redirect(url_for('lista_marketplaces'), code=302)

@app.route('/alterar_marketplace/<identifier>', methods=['GET', 'POST'])
def altera_marketplace(identifier):
    if request.method == 'POST':
        info = request.form
        ct_marketplace.update_marketplace(identifier, info)
        return redirect('listar_marketplaces')
    return render_template('create_marketplace.html', identifier = identifier, titulo='Alteração de Marketplace', titulo_head=titulo_head)


@app.route('/deletar_categoria/<identifier>')
def delete_category(identifier):
    ct_category.delete_category(identifier)
    return redirect(url_for('lista_categorias'), code=302)

@app.route('/alterar_categoria/<identifier>', methods=['GET', 'POST'])
def altera_categorias(identifier):
    if request.method == 'POST':
        info = request.form
        ct_category.update_category(identifier, info)
        return redirect('/listar_categorias')
    return render_template('create_category.html', identifier = identifier, titulo='Alteração de Categoria', titulo_head=titulo_head)

@app.route('/')
def home():
    return render_template('home.html', titulo_head=titulo_head)


app.run()