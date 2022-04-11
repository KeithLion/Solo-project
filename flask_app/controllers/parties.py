from flask_app import app
from flask import render_template, redirect, request
# from flask_app.models import Party
# from flask_app import User


@app.route('/all')
def all_parties():
    return render_template('all_parties.html')


@app.route('/addParty')
def add_parties():
    return render_template('add_party.html')


@app.route('/updateParty')
def update_party():
    return render_template('update_party.html')


@app.route('/oneParty')
def one_party():
    return render_template('one_party.html')
