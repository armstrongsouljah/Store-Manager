from databases.server import DatabaseConnection


class User:
    """ Class for creating and authenticating users in the database """
    def __init__(self, admin=False, password=None, **kwargs):
        self.username = kwargs.get("username")
        self.admin = admin
        self.password = password
        self.cursor = DatabaseConnection().cursor

    def get_all(self):
        self.cursor.execute('SELECT * FROM users')
        rows = self.cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
            return "Found users"
        else:
            return "Database empty"