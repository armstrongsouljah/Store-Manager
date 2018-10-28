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

 