from back_end.models.seller import Seller
from back_end.controller.ctrl_seller import SellerController
from flask import Blueprint, render_template, request, redirect, url_for

seller = Blueprint(__name__, 'seller')
CONTROLLER = SellerController()
titulo_head = 'Lojinha'


@seller.route('/cadastrar_seller')
def cadastro_Seller():
    message = ''
    name = request.args.get('name')
    phone = request.args.get('phone')
    email = request.args.get('email')

    if name is not None and phone is not None and email is not None:
        seller = Seller(name, email, phone)
        CONTROLLER.save(seller)
        message = f'{name} adicionado com sucesso'
    return render_template('create_seller.html', menssagem=message, titulo='Cadastro Seller', titulo_head=titulo_head)


@seller.route('/listar_sellers', methods=['GET'])
def lista_sellers():
    sellers = CONTROLLER.read_all()
    return render_template('list_sellers.html', sellers=sellers, titulo="Sellers", titulo_head=titulo_head)


@seller.route('/alterar_seller/<identifier>', methods=['GET', 'POST'])
def alterar_seller(identifier):
    if request.method == 'POST':
        seller = CONTROLLER.read_by_id(identifier)
        seller.name = request.form.get('name')
        seller.email = request.form.get('email')
        seller.phone = request.form.get('phone')
        CONTROLLER.save(seller)
        return redirect('/listar_sellers')
    seller = CONTROLLER.read_by_id(identifier)
    return render_template('create_seller.html', identifier=identifier, seller=seller, titulo='Alteração de Seller', titulo_head=titulo_head)


@seller.route('/delete_seller/<identifier>')
def delete_seller(identifier):
    seller = CONTROLLER.read_by_id(identifier)
    CONTROLLER.delete(seller)
    return redirect('/listar_sellers')