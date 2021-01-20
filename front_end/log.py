from back_end.controller.ctrl_log import LogController
from flask import Blueprint, render_template, request, redirect

log = Blueprint(__name__, 'log')
CONTROLLER = LogController()
titulo_head = 'Lojinha'


@log.route('/listar_sellers', methods=['GET'])
def lista_sellers():
    sellers = CONTROLLER.read_all()
    return render_template('list_sellers.html', sellers=sellers, titulo='Sellers', titulo_head=titulo_head)