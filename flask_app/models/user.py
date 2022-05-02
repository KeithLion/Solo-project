from flask_app.config.mysqlconnection import connectToMySQL


class User:

    db = 'dndschema'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.strength = data['strength']
        self.dexterity = data['dexterity']
        self.constitution = data['constitution']
        self.wisdom = data['wisdom']
        self.intelligence = data['intelligence']
        self.charisma = data['charisma']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_player(cls, data):
        query = "INSERT INTO users (name,strength,dexterity,constitution,wisdom,intelligence,charisma,party_id) VALUES (%(name)s,%(strength)s,%(dexterity)s,%(constitution)s,%(wisdom)s,%(intelligence)s,%(charisma)s, %(party_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET strength=%(strength)s, dexterity=%(dexterity)s, constitution=%(constitution)s, wisdom=%(wisdom)s, intelligence=%(intelligence)s,charisma=%(charisma)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def one_user(cls, data):
        query = "select * from users where id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
