import sys

sys.path.append('.')

from flask import Flask, render_template, request, redirect, url_for
import back_end.controller.ctrl_marketplace as ct_marketplace
from back_end.controller.ctrl_seller import SellerController
import back_end.controller.ctrl_category as ct_category
from back_end.controller.ctrl_product import ProductController
from back_end.controller.ctrl_log import LogController

from back_end.models.Marketplace import Marketplace
from back_end.models.seller import Seller
from back_end.models.Category import Category
from back_end.models.product import Product
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

@app.route('/cadastrar_seller')
def cadastro_Seller():
    message = ''
    name = request.args.get('name')
    phone = request.args.get('phone')
    email = request.args.get('email')

    if name is not None and phone is not None and email is not None:
        seller = Seller(name, email, phone)
        SellerController().create(seller)
        log = Log(f'Cadastro do seller "{name}" ao database.')
        LogController().create(log)
        message = f'{name} adicionado com sucesso'
    return render_template('create_seller.html', menssagem=message, titulo='Cadastro Seller', titulo_head=titulo_head)

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

@app.route('/cadastrar_produto')
def cadastro_Produto():
    menssagem = ''
    name = request.args.get('name')

    if name is not None:
        description = request.args.get('description')
        price = request.args.get('price')
        product = Product(name, description, price)
        ProductController().create(product)
        log = Log(f'Cadastro do seller "{name}" ao database.')
        LogController().create(log)
        menssagem = f'{name} cadastrado com sucesso'
    return render_template('create_product.html', menssagem=menssagem, titulo='Cadastro de Produtos', titulo_head=titulo_head)


@app.route('/listar_marketplaces')
def lista_marketplaces():
    marketplaces = ct_marketplace.list_marketplaces()
    return render_template('list_marketplaces.html', marketplaces=marketplaces, titulo='Marketplaces',
                           titulo_head=titulo_head)

@app.route('/listar_sellers', methods=['GET', 'POST'])
def lista_sellers():
    if request.method == 'POST':
        search = request.form.get('search')
        log = Log(f'Listado sellers com o filtro "{search}".')
    else:
        search = None
        log = Log('Listado todos os sellers.')
    sellers = SellerController().read_all(search)
    LogController().create(log)
    return render_template('list_sellers.html', sellers=sellers, titulo='Sellers', titulo_head=titulo_head)

@app.route('/listar_categorias')
def lista_categorias():
    list_cat = ct_category.list_categories()
    return render_template('list_categories.html', categories=list_cat, titulo="Categorias", titulo_head=titulo_head)

@app.route('/listar_produtos', methods=['GET', 'POST'])
def lista_produtos():
    if request.method == 'POST':
        search = request.form.get('search')
        log = Log(f'Listado produtos com o filtro "{search}".')
    else:
        search = None
        log = Log('Listado todos os produtos.')
    products = ProductController().read_all(search)
    LogController().create(log)
    return render_template('list_products.html', products=products, titulo="Produtos", titulo_head=titulo_head)

@app.route('/listar_logs', methods=['GET', 'POST'])
def lista_logs():
    if request.method == 'POST':
        search = request.form.get('search')
        log = Log(f'Listado logs com o filtro "{search}".')
    else:
        search = None
        log = Log(f'Listado todos os logs.')
    logs = LogController().read_all(search)
    LogController().create(log)
    return render_template('list_logs.html', logs=logs, titulo="Histórico", titulo_head=titulo_head)


@app.route('/alterar_marketplace/<identifier>', methods=['GET', 'POST'])
def altera_marketplace(identifier):
    if request.method == 'POST':
        info = request.form
        ct_marketplace.update_marketplace(identifier, info)
        return redirect('listar_marketplaces')
    return render_template('create_marketplace.html', identifier = identifier, titulo='Alteração de Marketplace', titulo_head=titulo_head)

@app.route('/alterar_seller/<identifier>', methods=['GET', 'POST'])
def alterar_seller(identifier):
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        seller = Seller(name, email, phone, identifier)
        SellerController().update(seller)
        log = Log(f'Alterado informações de seller com id "{identifier}".')
        LogController().create(log)
        return redirect('/listar_sellers')
    return render_template('create_seller.html', identifier = identifier, titulo='Alteração de Seller', titulo_head=titulo_head)

@app.route('/alterar_categoria/<identifier>', methods=['GET', 'POST'])
def altera_categorias(identifier):
    if request.method == 'POST':
        info = request.form
        ct_category.update_category(identifier, info)
        return redirect('/listar_categorias')
    return render_template('create_category.html', identifier = identifier, titulo='Alteração de Categoria', titulo_head=titulo_head)

@app.route('/alterar_produto/<identifier>', methods=['GET', 'POST'])
def alterar_produto(identifier):
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        product = Product(name, description, price, identifier)
        ProductController().update(product)
        log = Log(f'Alterado informações de produto com id "{identifier}".')
        LogController().create(log)
        return redirect('/listar_produtos')
    return render_template('create_product.html', identifier = identifier, titulo='Alteração de Produto', titulo_head=titulo_head)


@app.route('/deletar_marketplace/<identifier>')
def delete_marketplace(identifier):
    ct_marketplace.delete_marketplace(identifier)
    return redirect(url_for('lista_marketplaces'), code=302)

@app.route('/delete_seller/<identifier>')
def delete_seller(identifier):
    SellerController().delete(identifier)
    log = Log(f'Deletado seller com id "{identifier}".')
    LogController().create(log)
    return redirect('/listar_sellers')

@app.route('/deletar_categoria/<identifier>')
def delete_category(identifier):
    ct_category.delete_category(identifier)
    return redirect(url_for('lista_categorias'), code=302)

@app.route('/delete_product/<identifier>')
def delete_product(identifier):
    ProductController().delete(identifier)
    log = Log(f'Deletado produto com id "{identifier}".')
    LogController().create(log)
    return redirect('/listar_produtos')


@app.route('/')
def home():
    return render_template('home.html', titulo_head=titulo_head)


app.run()
