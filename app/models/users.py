import string
from databases.server import DatabaseConnection
from werkzeug.security import generate_password_hash, check_password_hash
from app.utils import validate_registration_data


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
