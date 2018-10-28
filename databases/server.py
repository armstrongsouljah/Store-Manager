import psycopg2
from psycopg2.extras import RealDictCursor
from app.config import env_config
from app import app as ap
from werkzeug.security import generate_password_hash as g

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
            dbname = env_config['production'].DATABASE
            self.credentials['host'] = env_config['production'].HOST
            self.credentials['user'] = env_config['production'].USER
            self.credentials['password'] = env_config['production'].PASSWORD
            self.credentials['dbname'] = dbname

        try:
            self.conn =  psycopg2.connect(**self.credentials, cursor_factory=RealDictCursor)
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()

            self.commands = (
                """
                        CREATE TABLE IF NOT EXISTS  users(
                            user_id SERIAL PRIMARY KEY,
                            username VARCHAR(35) NOT NULL UNIQUE,
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
                """,
                f"""
                INSERT INTO users(username, password, admin)
                VALUES('admin','{g("testing123")}' ,True)
                """
            )
            for command in self.commands:
                self.cursor.execute(command)
            print(f"connection successful on {dbname}")
        except (Exception, psycopg2.DatabaseError) as E:
            print(f"{E}")


    def drop_relation(self, tablename):
        q = f""" DROP TABLE IF EXISTS {tablename} """
        return self.cursor.execute(q)



        
        
        
        