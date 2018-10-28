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

    def authenticate(self, username, password=None):
        
        query = f""" SELECT username, password, admin FROM users
               WHERE username='{username}'
        """
        message = None
        # 1 query db
        self.cursor.execute(query)
        # 2 fetch result
        user = self.cursor.fetchone()
        if user is not None:
            message = user
        else:
            message = {"msg":"user does not exist"}
        return message
    

    
    def register_user(self, username, password):
        message = None
        if not username or not password:
            message = {'msg':'username/password fields not allowed'}
        if username == "" or username ==" " or password == "":
            message = {'msg':'username/password cannot be spaces'}
        if username and username[0] in string.digits:
            message = {'msg':'Username/password cannot startwith a number'}

        if not isinstance(username, str) or not isinstance(password, str):
            message = {'msg': 'Username/password must be a word'}

        if username and len(username) < 5 or password and len(password) < 5:
            message = {'msg': 'Username/password must be 6 characters and above'}
        if message:
            return message
        
        password = generate_password_hash(password)
        
        query = f""" INSERT INTO users (username,password) VALUES('{username}', '{password}')

             """
        
        try:
            self.cursor.execute(query)
            message = {'msg':'Successfully registered'}

        except Exception as E:
            message = {'msg':f'Query failed due to {E}'}
        return message
            



        


        


 