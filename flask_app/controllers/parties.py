from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.party import Party


@app.route('/')
def all_parties():
    return render_template('all_parties.html', open=Party.get_all())


@app.route('/addParty')
def add_parties():

    return render_template('add_party.html')


@app.route('/saveCampaign', methods=['post'])
def save():
    data = {
        'title': request.form['title'],
        'description': request.form['description']
    }
    Party.save(data)
    return redirect('/')


@app.route('/updateParty')
def update_party():
    return render_template('update_party.html')


@app.route('/oneParty/<parties_id>')
def one_party(parties_id):
    data = {
        'parties_id': parties_id
    }
    return render_template('one_party.html', campaign=Party.get_one(data))
