from flask import Flask, render_template
from front_end.marketplace import marketplace
from front_end.category import category
from front_end.log import log
from front_end.product import product
from front_end.seller import seller

app = Flask(__name__)
titulo_head = 'Lojinha'
marketplace = app.register_blueprint(marketplace)
app.register_blueprint(product)
app.register_blueprint(category)
app.register_blueprint(seller)
app.register_blueprint(log)


@app.route('/')
def home():
    return render_template('home.html', titulo_head=titulo_head)
