import string


def validate_username(username):
        if len(username) < 5:
            raise ValueError("username must be 5 and above characters")
            
        if username == " ":
            raise ValueError("Name cannot be spaces")

        if not isinstance(username, str):
            raise TypeError("Username must be a string")

        if username.startswith(string.digits):
            raise ValueError("Username cannot start with a number")
        return username

class User:
    """ stores user details """
    def __init__(self, user_id, username, admin=False, password=None):
        self.user_id = int(user_id)
        self.username = str(validate_username(username))
        self.admin = bool(admin)
        self.password = str(password)

    

    @property
    def is_admin(self):
        return self.admin