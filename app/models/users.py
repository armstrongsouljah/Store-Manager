import string
from flask import jsonify
from databases.server import DatabaseConnection
from werkzeug.security import generate_password_hash, check_password_hash
from app.utils import validate_registration_data, check_item_exists, fetch_all


class User:
    """ Class for creating and authenticating users in the database """
    def __init__(self, admin=False, password=None, **kwargs):
        self.username = kwargs.get("username")
        self.admin = admin
        self.password = password
        self.cursor = DatabaseConnection().cursor

    def check_password(self, hash, password):
        return check_password_hash(hash, password)

    def fetch_user(self, username, password=None):
        
        fetch_user_query = f""" SELECT user_id, username, password, role FROM users
               WHERE username='{username}'
        """
        response = None
        # 1 query db
        self.cursor.execute(fetch_user_query)
        # 2 fetch result
        fetched_user = self.cursor.fetchone()
        if fetched_user:
            response = fetched_user
        else:
            response = {"error":"user does not exist"}
        return response
    
    

    
    def register_user(self, username, password, role):
        message = validate_registration_data(username, password, role)        
        if message:
            return message
        
        password = generate_password_hash(password)
        user_exists_query = f"""
            SELECT username from users WHERE username='{username}'
        """
        self.cursor.execute(user_exists_query)
        returned_user = self.cursor.fetchone()
        
        reqister_user_query = f""" INSERT INTO users (username, password, role) 
        VALUES('{username}', '{password}', '{role}')
             """
        if returned_user is not None:
            message = {'message': 'Username already taken'}
        else:
            try:
                self.cursor.execute(reqister_user_query)
                message = {'message':'Successfully registered'}

            except Exception as error:
                message = {'message':f'Query failed due to {error}'}
        return message

    def do_the_logout(self, token_jti):
        response = None
        token_already_revoked = check_item_exists('token_jti', 'blacklisted', token_jti, self.cursor)
        token_blacklist_query = f"""
        INSERT INTO blacklisted(token_jti)
        VALUES('{token_jti}')
        """

        if token_already_revoked:
            response = jsonify({'message':'You have already logged out'}), 400
        else:
            try:
                self.cursor.execute(token_blacklist_query)
                response = jsonify({'message': 'You have successfully logged out'}), 200
            except Exception as error:
                response =jsonify({'message':f'{error}'}), 401
        return response

    def all_revoked(self):
        return fetch_all('blacklisted', self.cursor)

    def is_token_revoked(self, token_jti):
        revoked_token_query = f"""
        SELECT token_jti FROM blacklisted 
        WHERE token_jti='{token_jti}'
        """
        self.cursor.execute(revoked_token_query)
        returned_token = self.cursor.fetchone()

        if returned_token:
            return True
        return False
        

