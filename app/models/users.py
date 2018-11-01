import string
from databases.server import DatabaseConnection
from werkzeug.security import generate_password_hash, check_password_hash


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
    
    def validate_registration_data(self, username, password,role):
        message = None
        if not username or not password or not role:
            message = {'mesage':'username/password fields not allowed'}
        if username == "" or username ==" " or password == "":
            message = {'message':'username/password cannot be spaces'}
        if username and username[0] in string.digits:
            message = {'message':'Username/password cannot startwith a number'}

        if not isinstance(username, str) or not isinstance(password, str):
            message = {'message': 'Username/password must be a word'}
        if not isinstance(role, str):
            message = {'message': 'User role must be a string'}

        if username and len(username) < 5 or password and len(password) < 5:
            message = {'message': 'Username/password must be 6 characters and above'}
        return message

    
    def register_user(self, username, password, role):
        message = self.validate_registration_data(username, password, role)        
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
            



        


        


 