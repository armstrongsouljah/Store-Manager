import psycopg2
from psycopg2.extras import RealDictCursor
from app.config import env_config
from app import app as ap
from .relations import commands
from urllib.parse import urlparse

result = urlparse(env_config['production'].DATABASE_URI)

class DatabaseConnection:

    def __init__(self):
        self.credentials = dict(
                dbname ='',
                user = 'postgres',
                password='testpwd',
                host='localhost',
                port = 5432
            )

        if ap.config.get('ENV') == 'development':
            dbname = env_config['development'].DATABASE
            self.credentials['dbname'] = dbname
            
        if ap.config.get('ENV') == 'testing':
            dbname = env_config['testing'].DATABASE
            self.credentials['dbname'] = dbname
            
        if ap.config.get('ENV') == 'production':
            dbname = result.path[1:]
            self.credentials['host'] = result.hostname
            self.credentials['user'] = result.username
            self.credentials['password'] = result.password
            self.credentials['dbname'] = dbname

        try:
            self.conn =  psycopg2.connect(**self.credentials, cursor_factory=RealDictCursor)
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()

            for command in commands:
                self.cursor.execute(command)
            # print(f"connection successful on {dbname}")
        except Exception as error:
            print(f"error: {error}")


    def drop_relation(self, tablename):
        delete_relation_query = f""" DROP TABLE IF EXISTS {tablename} CASCADE """
        return self.cursor.execute(delete_relation_query)



        
        
        
        