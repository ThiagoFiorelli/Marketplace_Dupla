from flask import Flask, render_template, request

app = Flask(__name__)

titulo_head = 'Lojinha'

@app.route('/')
def home():
    return render_template('home.html', titulo_head = 'titulo_head')

app.run(debug=True)