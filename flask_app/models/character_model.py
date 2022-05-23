from types import ClassMethodDescriptorType
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request, session

from flask_app import DATABASE

class Character:
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.char_class = data['char_class']
        self.race = data['race']
        self.strength = data['strength']
        self.constitution = data['constitution']
        self.dexterity = data['dexterity']
        self.intelligence = data['intelligence']
        self.wisdom = data['wisdom']
        self.charisma = data['charisma']
        self.user_id = data['user_id']
        self.notes = data['notes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        


#classmethods for characters

    # this class method will create a new character
    @classmethod
    def create_char(cls, data):
        query = 'INSERT INTO characters (name, char_class, race, strength, constitution, dexterity, intelligence, wisdom, charisma, user_id, notes, created_at, updated_at) '
        query += 'Values (%(name)s, %(char_class)s, %(race)s, %(strength)s, %(constitution)s, %(dexterity)s, %(intelligence)s, %(wisdom)s, %(charisma)s, %(user_id)s, %(notes)s, NOW(), NOW() );'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def show_all_chars(cls):
        query= 'SELECT * FROM characters;'
        results = connectToMySQL(DATABASE).query_db(query)
        chars = []
        if not results:
            return False
        for row in results:
            chars.append(cls(row))
        return chars

    # this method will return a list of dicitonaries for every charcter that player has created
    @classmethod
    def get_all_chars(cls, data):
        query = 'SELECT * FROM characters WHERE user_id = %(user_id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        characters = []
        if not results:
            return False
        for row in results:
            characters.append(cls(row))
        return characters

    # this method will return a specific character selected by the user
    @classmethod
    def get_one_char(cls, data):
        query = "SELECT * FROM characters where id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    # get last updated character
    @classmethod
    def most_recent_char(cls, data):
        query = 'SELECT * From characters WHERE user_id = %(user_id)s ORDER BY updated_at DESC LIMIT 1;'
        result = connectToMySQL(DATABASE).query_db(query,data)
        if not result:
            return False
        return cls(result[0])

    # this will update character notes
    @classmethod
    def update_char_notes(cls,data):
        query = 'UPDATE characters SET notes= %(notes)s WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    # delete character
    @classmethod
    def delete_char(cls, data):
        query = 'DELETE FROM characters WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result




    # static methods for validating character input
    @staticmethod
    def validate_input(char):
        is_valid = True
        if not len(char['name']) > 2:
            flash('Character name must be at least 3 characters.','err.char_name')
            is_valid = False
        if not len(char['char_class']) > 2:
            flash('You must enter a class','err.class')
            is_valid = False
        if not len(char['race']) > 2:
            flash('You must enter a Race', 'err.race')
            is_valid = False
        if len(char['strength']) > 0:
            if not int(char['strength']) > 5:
                flash('this is not a valid roll.','err.str')
                is_valid = False
        if not len(char['strength']) > 0:
            flash('you must roll for this stat!','err.str')
            is_valid = False
        if len(char['constitution']) > 0:
            if not int(char['constitution']) > 5:
                flash('this is not a valid roll.','err.const')
                is_valid = False
        if not len(char['constitution']) > 0:
            flash('You must roll for this stat!','err.const')
            is_valid = False
        if len(char['dexterity']) > 0: 
            if not int(char['dexterity']) > 5:
                flash('This is not a valid roll.','err.dex')
                is_valid = False
        if not len(char['dexterity']) > 0:
            flash('You must roll for this stat!','err.dex')
            is_valid = False 
        if len(char['intelligence']) > 0: 
            if not int(char['intelligence']) > 5:
                flash('This is not a valid roll.','err.int')
                is_valid = False    
        if not len(char['intelligence']) > 0:
            flash('You must roll for this stat!','err.int')
            is_valid = False
        if len(char['wisdom']) > 0: 
            if not int(char['wisdom']) > 5:
                flash('This is not a valid roll.','err.wis')
                is_valid = False     
        if not len(char['wisdom']) > 0:
            flash('You must roll for this stat!','err.wis')
            is_valid = False  
        if len(char['charisma']) > 0: 
            if not int(char['charisma']) > 5:
                flash('This is not a valid roll.','err.char')
                is_valid = False   
        if not len(char['charisma']) > 0:
            flash('You must roll for this stat!','err.char')
            is_valid = False   
        return is_valid