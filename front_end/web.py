import sys
sys.path.append('.')

from flask import Flask, render_template, request, redirect, url_for

from back_end.controller.ctrl_seller import SellerController
from back_end.controller.ctrl_product import ProductController
from back_end.controller.ctrl_log import LogController
from back_end.controller.ctrl_marketplace import MarketplaceController
from back_end.controller.ctrl_category import CategoryController

from back_end.models.marketplace import Marketplace
from back_end.models.category import Category
from back_end.models.product import Product
from back_end.models.seller import Seller
from back_end.models.log import Log

app = Flask(__name__)
titulo_head = 'Lojinha'

@app.route('/cadastrar_seller')
def cadastro_Seller():
    message = ''
    name = request.args.get('name')
    phone = request.args.get('phone')
    email = request.args.get('email')

    if name is not None and phone is not None and email is not None:
        seller = Seller(name, email, phone)
        SellerController().save(seller)
        message = f'{name} adicionado com sucesso'
    return render_template('create_seller.html', menssagem=message, titulo='Cadastro Seller', titulo_head=titulo_head)

@app.route('/cadastrar_categoria')
def cadastro_Categoria():
    mensagem = ''
    category_name = request.args.get('name')

    if category_name is not None:
        category_description = request.args.get('description')
        cat = Category(category_name, category_description)
        CategoryController().create(cat)
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
        ProductController().save(product)
        menssagem = f'{name} cadastrado com sucesso'
    return render_template('create_product.html', menssagem=menssagem, titulo='Cadastro de Produtos', titulo_head=titulo_head)


@app.route('/listar_marketplaces')
def lista_marketplaces():
    marketplaces = MarketplaceController().read_all()
    return render_template('list_marketplaces.html', marketplaces=marketplaces, titulo='Marketplaces',
                           titulo_head=titulo_head)

@app.route('/listar_sellers', methods=['GET'])
def lista_sellers():
    sellers = SellerController().read_all()
    return render_template('list_sellers.html', sellers=sellers, titulo='Sellers', titulo_head=titulo_head)

@app.route('/listar_produtos', methods=['GET'])
def lista_produtos():
    products = ProductController().read_all()
    return render_template('list_products.html', products=products, titulo="Produtos", titulo_head=titulo_head)

@app.route('/listar_logs', methods=['GET'])
def lista_logs():
    logs = LogController().read_all()
    return render_template('list_logs.html', logs=logs, titulo="Histórico", titulo_head=titulo_head)

@app.route('/alterar_seller/<identifier>', methods=['GET', 'POST'])
def alterar_seller(identifier):
    if request.method == 'POST':
        seller = SellerController().read_by_id(identifier)
        seller.name = request.form.get('name')
        seller.email = request.form.get('email')
        seller.phone = request.form.get('phone')
        SellerController().save(seller)
        return redirect('/listar_sellers')
    seller = SellerController().read_by_id(identifier)
    return render_template('create_seller.html', identifier = identifier, seller = seller, titulo='Alteração de Seller', titulo_head=titulo_head)

@app.route('/alterar_produto/<identifier>', methods=['GET', 'POST'])
def alterar_produto(identifier):
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')

        product = ProductController().read_by_id(identifier)
        product.name = name
        product.description = description
        product.price = price
        ProductController().save(product)
        return redirect('/listar_produtos')
    product = ProductController().read_by_id(identifier)
    return render_template('create_product.html', identifier = identifier, product = product, titulo='Alteração de Produto', titulo_head=titulo_head)
      
@app.route('/listar_categorias')
def lista_categorias():
    list_cat = CategoryController().read_all()
    return render_template('list_categories.html', categories=list_cat, titulo="Categorias", titulo_head=titulo_head)

@app.route('/deletar_marketplace/<identifier>')
def delete_marketplace(identifier):
    marketplace = MarketplaceController().read_by_id(identifier)
    print(marketplace.name)
    MarketplaceController().delete(marketplace)
    return redirect(url_for('lista_marketplaces'), code=302)

@app.route('/alterar_marketplace/<identifier>', methods=['GET', 'POST'])
def altera_marketplace(identifier):
    marketplace = MarketplaceController().read_by_id(identifier)
    if request.method == 'POST':
        marketplace.name = request.form.get('name')
        marketplace.description = request.form.get('description')
        MarketplaceController().save(marketplace)
        menssagem = f'{marketplace.name} atualizado com sucesso'
        return redirect('listar_marketplaces')
    return render_template('create_marketplace.html', identifier = identifier, titulo='Alteração de Marketplace', titulo_head=titulo_head, marketplace=marketplace)
  

@app.route('/cadastrar_marketplace')
def cadastro_Marketplace():
    menssagem = ''
    marketplace_add = request.args.get('name')
    description_market = request.args.get('description')
    if marketplace_add is not None and description_market is not None:
        mkp = Marketplace(marketplace_add, description_market)
        print(mkp.name)
        MarketplaceController().save(mkp)
        #menssagem = f'{mkp.name} cadastrado com sucesso'
    return render_template('create_marketplace.html', menssagem=menssagem, titulo='Cadastro de Marketplaces', titulo_head=titulo_head)

@app.route('/delete_seller/<identifier>')
def delete_seller(identifier):
    seller = SellerController().read_by_id(identifier)
    SellerController().delete(seller)
    return redirect('/listar_sellers')

@app.route('/deletar_categoria/<identifier>')
def delete_category(identifier):
    CategoryController().delete(identifier)
    return redirect(url_for('lista_categorias'), code=302)

@app.route('/alterar_categoria/<identifier>', methods=['GET', 'POST'])
def altera_categorias(identifier):
    if request.method == 'POST':
        cat_name = request.form.get('name')
        cat_desc = request.form.get('description')
        cat = Category(cat_name, cat_desc, identifier)
        CategoryController().update(cat)
        return redirect('/listar_categorias')
    return render_template('create_category.html', identifier = identifier, titulo='Alteração de Categoria', titulo_head=titulo_head)

@app.route('/delete_product/<identifier>')
def delete_product(identifier):
    product = ProductController()
    product_deleted = product.read_by_id(identifier)
    product.delete(product_deleted)
    return redirect('/listar_produtos')

@app.route('/')
def home():
    return render_template('home.html', titulo_head=titulo_head)


app.run(debug=True)
