from twitter import app
from flask import render_template, url_for

@app.route('/')
def homepage():

    lista = ['item1', 'item2', 'item3']
    return render_template('homepage.html', lista=lista)