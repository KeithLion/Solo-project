from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.party import Party
from flask_app.models.user import User


@app.route('/addPlayer')
def add_player():
    return render_template('add_player.html', parties=Party.get_all())


@app.route('/savePlayer', methods=['post'])
def save_player():
    data = {
        'name': request.form['name'],
        'strength': request.form['strength'],
        'dexterity': request.form['dexterity'],
        'constitution': request.form['constitution'],
        'wisdom': request.form['wisdom'],
        'intelligence': request.form['intelligence'],
        'charisma': request.form['charisma'],
        'party_id': request.form['party_id']
    }
    User.save_player(data)
    return redirect('/')


@app.route('/updatePlayer/<int:id>', methods=['post'])
def update_player(id):
    data = {
        'id': id,
        'strength': request.form['strength'],
        'dexterity': request.form['dexterity'],
        'constitution': request.form['constitution'],
        'wisdom': request.form['wisdom'],
        'intelligence': request.form['intelligence'],
        'charisma': request.form['charisma'],
    }
    User.update(data)
    return redirect('/')


@app.route('/update/<int:id>')
def update(id):
    data = {
        'id': id
    }

    return render_template('update_player.html', oneUser=User.one_user(data))


@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    User.destroy(data)
    return redirect('/')
