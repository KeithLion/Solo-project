from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash


class Party:

    db = 'dndschema'

    def __init__(self, data):
        self.parties_id = data['parties_id']
        self.title = data['title']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.player = []

    @classmethod
    def get_all(cls):
        query = "select * from parties;"
        results = connectToMySQL(cls.db).query_db(query)
        parties = []
        for p in results:
            parties.append(cls(p))
        return parties

    @classmethod
    def save(cls, data):
        query = "insert into parties (title,description) values (%(title)s, %(description)s)"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM parties left join users on users.party_id = parties_id  where users.party_id = %(parties_id)s "
        result = connectToMySQL(cls.db).query_db(query, data)
        campaign_with_players = []
        for user in result:
            campaign_with_players.append(User(user))
        print(campaign_with_players)
        return campaign_with_players
