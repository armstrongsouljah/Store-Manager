class User:
    """ stores user details """
    def __init__(self, user_id, username, admin=False, password=None):
        self.user_id = user_id
        self.username = username
        self.admin = admin
        self.password = password

    @property
    def is_admin(self):
        return self.admin