from back_end.models.product import Product
from back_end.controller.ctrl_product import ProductController
from flask import Blueprint, render_template, request, redirect, url_for

product = Blueprint(__name__, 'product')
CONTROLLER = ProductController()
titulo_head = 'Lojinha'


@product.route('/cadastrar_produto')
def cadastro_Produto():
    menssagem = ''
    name = request.args.get('name')
    if name is not None:
        description = request.args.get('description')
        price = request.args.get('price')
        product = Product(name, description, price)
        CONTROLLER.save(product)
        menssagem = f'{name} cadastrado com sucesso'
    return render_template('create_product.html', menssagem=menssagem, titulo='Cadastro de Produtos',
                           titulo_head=titulo_head)


@product.route('/listar_produtos', methods=['GET'])
def lista_produtos():
    products = CONTROLLER.read_all()
    return render_template('list_products.html', products=products, titulo="Produtos", titulo_head=titulo_head)


@product.route('/alterar_produto/<identifier>', methods=['GET', 'POST'])
def alterar_produto(identifier):
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')

        product = CONTROLLER.read_by_id(identifier)
        product.name = name
        product.description = description
        product.price = price
        CONTROLLER.save(product)
        return redirect('/listar_produtos')
    product = CONTROLLER.read_by_id(identifier)
    return render_template('create_product.html', identifier=identifier, product=product, titulo='Alteração de Produto', titulo_head=titulo_head)


@product.route('/delete_product/<identifier>')
def delete_product(identifier):
    product_deleted = CONTROLLER.read_by_id(identifier)
    CONTROLLER.delete(product_deleted)
    return redirect('/listar_produtos')