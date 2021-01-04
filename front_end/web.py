from flask import Flask, render_template, request

app = Flask(__name__)
<<<<<<< HEAD
titulo_head = 'Lojinha'
=======

<<<<<<< HEAD
titulo_head = 'Lojinha'

=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> 5ee3ead864261045519271c9f05f31326612b822

@app.route('/cadastrar_marketplace')
def cadastro_Marketplace():
    menssagem = ''
    marketplace_add = request.args.get('market')
    if marketplace_add is not None:
        menssagem = f'{marketplace_add} cadastrado com sucesso'
    return render_template('create_marketplace.html', menssagem=menssagem)

@app.route()
def cadastro_Produto():
    menssagem = ''
    product_name = request.args.get('name')

    if product_name is not None:
        product_descrpition = request.args.get('descrpition')
        product_price = request.args.get('price')
        create_product(product_name, product_descrpition, product_price)
        menssagem = f'{product_name} cadastrado com sucesso'

<<<<<<< HEAD
    return render_template('create_product.html', menssagem=menssagem)
=======
@app.route('/')
def home():
    return render_template('home.html', titulo_head='titulo_head')


app.run(debug=True)
<<<<<<< HEAD
=======
=======
titulo_head = 'Lojinha'
>>>>>>> 5ee3ead864261045519271c9f05f31326612b822

@app.route('/')
def home():
    return render_template('home.html', titulo_head = 'titulo_head')

app.run(debug=True)
<<<<<<< HEAD
=======
>>>>>>> main
>>>>>>> main
>>>>>>> 5ee3ead864261045519271c9f05f31326612b822
