from back_end.models.marketplace import Marketplace
from back_end.controller.ctrl_marketplace import MarketplaceController
from flask import Blueprint, render_template, request, redirect, url_for

marketplace = Blueprint(__name__, 'marketplace')
CONTROLLER = MarketplaceController()
titulo_head = 'Lojinha'


@marketplace.route('/cadastrar_marketplace')
def cadastro_Marketplace():
    marketplace_add = request.args.get('name')
    description_market = request.args.get('description')
    if marketplace_add is not None and description_market is not None:
        mkp = Marketplace(marketplace_add, description_market)
        CONTROLLER.save(mkp)
    return render_template('create_marketplace.html', titulo='Cadastro de Marketplaces', titulo_head=titulo_head)


@marketplace.route('/alterar_marketplace/<identifier>', methods=['GET', 'POST'])
def altera_marketplace(identifier):
    marketplace = CONTROLLER.read_by_id(identifier)
    if request.method == 'POST':
        marketplace.name = request.form.get('name')
        marketplace.description = request.form.get('description')
        CONTROLLER.save(marketplace)
        return redirect('/listar_marketplaces')
    return render_template('create_marketplace.html', identifier=identifier, titulo='Alteração de Marketplace',
                           titulo_head=titulo_head, marketplace=marketplace)


@marketplace.route('/listar_marketplaces')
def lista_marketplaces():
    marketplaces = CONTROLLER.read_all()
    return render_template('list_marketplaces.html', marketplaces=marketplaces, titulo='Marketplaces',
                           titulo_head=titulo_head)


@marketplace.route('/deletar_marketplace/<identifier>')
def delete_marketplace(identifier):
    marketplace = CONTROLLER.read_by_id(identifier)
    CONTROLLER.delete(marketplace)
    return redirect('/listar_marketplaces')
