from flask import Flask, render_template, request

app = Flask(__name__)

titulo_head = 'Lojinha'


@app.route('/cadastrar_marketplace')
def cadastro_Marketplace():
    menssagem = ''
    marketplace_add = request.args.get('market')
    if marketplace_add is not None:
        menssagem = f'{marketplace_add} cadastrado com sucesso'
    return render_template('create_marketplace.html', menssagem=menssagem)


@app.route('/')
def home():
    return render_template('home.html', titulo_head='titulo_head')


app.run(debug=True)
