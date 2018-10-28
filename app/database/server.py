import psycopg2
from psycopg2.extras import RealDictCursor
from app.config import env_config

from app.__init__ import  app


class DatabaseConnection:
    """ Creates a connection to the application database """
    def __init__(self):
        self.db = ''

        self.credentials = dict(
                dbname =self.db,
                user = 'postgres',
                password='testpwd',
                host='localhost',
                port = 5432
            )

        self.commands = (
            """
            CREATE TABLE IF NOT EXISTS  users(
                user_id SERIAL PRIMARY KEY,
                user_name VARCHAR(35) NOT NULL UNIQUE,
                password VARCHAR(240) NOT NULL, 
                admin BOOL DEFAULT False,
                registered_at TIMESTAMP DEFAULT NOW()
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS  products(
                product_id SERIAL PRIMARY KEY,
                product_name VARCHAR(38) NOT NULL UNIQUE,
                quantity INTEGER NOT NULL,
                unit_cost INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT NOW()
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS categories(
                category_id SERIAL PRIMARY KEY,
                category_name VARCHAR(56) UNIQUE NOT NULL,
                created_at TIMESTAMPTZ DEFAULT NOW()
            )
            """
        )

        try:
            if app.config.get('ENV') == 'development':
                self.db = env_config['development'].DATABASE
            
            if app.config.get('ENV') == 'testing':
                self.db = env_config['testing'].DATABASE
            
            if app.config.get('ENV') == 'production':
                self.db = env_config['production'].DATABASE
                self.credentials['host'] = env_config['production'].HOST
                self.credentials['user'] = env_config['production'].USER
                self.credentials['password'] = env_config['production'].PASSWORD

            self.credentials['dbname'] = self.db            
            self.db_connection = psycopg2.connect(**self.credentials, cursor_factory=RealDictCursor)

            self.cursor = self.db_connection.cursor()
            self.db_connection.autocommit = True

            # create all tables in one go

            for command in self.commands:
                self.cursor.execute(command)
            print(f"Connection successful, connected to {self.db}")
        except Exception as E:
            print(f"connection failed due to {E}")
