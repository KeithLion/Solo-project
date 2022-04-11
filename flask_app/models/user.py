from flask_app.config.mysqlconnection import connectToMySQL


class User:

    db = 'DnDSchema'

    def __init__(self, data):
        self.users_id = data['users_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['create_at']
        self.updated_at = data['updated_at']
