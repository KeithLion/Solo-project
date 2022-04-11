from flask_app.config.mysqlconnection import connectToMySQL


class Party:

    db = 'DnDSchema'

    def __init__(self, data):
        self.parties_id = data['parties_id']
        self.name = data['name']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
