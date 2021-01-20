from back_end.controller.ctrl_log import LogController
from flask import Blueprint, render_template, request, redirect

log = Blueprint(__name__, 'log')
CONTROLLER = LogController()
titulo_head = 'Lojinha'


@log.route('/listar_logs', methods=['GET'])
def lista_sellers():
    logs = CONTROLLER.read_all()
    return render_template('list_logs.html', logs=logs, titulo='Logs', titulo_head=titulo_head)