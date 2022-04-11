from flask_app import app
from flask import render_template, redirect, request
# from flask_app.models import Parties
# from flask_app.models import User


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/onePlayer')
def one_player():
    return render_template('one_player.html')


@app.route('/updatePlayer')
def update_player():
    return render_template('update_player.html')
