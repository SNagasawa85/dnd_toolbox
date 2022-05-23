from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app import DATABASE

class Campaign:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.notes = data['notes']
        self.character_id = data['character_id']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # This will get all campaigns with the attached user ID
    @classmethod
    def get_all_camps(cls, data):
        query = 'SELECT * FROM campaigns WHERE user_id= %(user_id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        camps = []
        if not results:
            return False
        for row in results:
            camps.append(cls(row))
        return camps
    
    # this will create a new campaign with notes
    @classmethod
    def create_camp(cls, data):
        query = 'INSERT INTO campaigns (name, notes, user_id, character_id, created_at, updated_at)'
        query += 'VALUES ( %(name)s, %(notes)s, %(user_id)s, %(character_id)s, NOW(), NOW());'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    # this will return only the campaign by ID
    @classmethod
    def get_one_camp(cls, data):
        query = 'SELECT * FROM campaigns WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    # this will update the notes
    @classmethod
    def update_camp(cls, data):
        query = 'UPDATE campaigns SET notes= %(notes)s WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    # this method will change the character assigned to the campaign
    @classmethod
    def change_character(cls,data):
        query = 'UPDATE campaigns SET character_id = %(character_id)s WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    # this will get last updated campaign
    @classmethod
    def most_recent_camp(cls,data):
        query = 'SELECT * From campaigns WHERE user_id = %(user_id)s ORDER BY updated_at DESC LIMIT 1;'
        result = connectToMySQL(DATABASE).query_db(query,data)
        if not result:
            return False
        return cls(result[0])

    # this deletes a campaign
    @classmethod
    def delete_camp(cls,data):
        query = 'DELETE FROM campaigns WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    # staticmethod to validate campaign info
    @staticmethod
    def validate_camp(camp):
        is_valid = True
        if not len(camp['name']) > 2:
            flash('Campaign must have a name more than 2 characters.', 'err.camp_name')
            is_valid = False
        if not len(camp['notes']) > 0:
            flash('Campaign must start with at least 1 note.', 'err.camp_notes')
            is_valid = False
        return is_valid


