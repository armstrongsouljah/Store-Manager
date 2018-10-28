import psycopg2
from psycopg2.extras import RealDictCursor
from app.config import env_config
from app import app as ap

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
            print("connection successful")
        except (Exception, psycopg2.DatabaseError) as E:
            print(f"{E}")


# class DatabaseConnection:
#     def __enter__(self):
#         self.db = ''
#         self.conn = None
#         self.cursor = None
#         self.credentials = dict(
#             dbname =self.db,
#             user = 'postgres',
#             password='testpwd',
#             host='localhost',
#             port = 5432
#             )
#         if ap.config.get('ENV') == 'development':
#             self.db = env_config['development'].DATABASE
            
#         if ap.config.get('ENV') == 'testing':
#             self.db = env_config['testing'].DATABASE
            
#         if ap.config.get('ENV') == 'production':
#             self.db = env_config['production'].DATABASE
#             self.credentials['host'] = env_config['production'].HOST
#             self.credentials['user'] = env_config['production'].USER
#             self.credentials['password'] = env_config['production'].PASSWORD
#             self.credentials['dbname'] = self.db
        
#         try:
#             self.conn = psycopg2.connect(**self.credentials, cursor_factory=RealDictCursor)
#             self.conn.commit()
#             self.cursor = self.conn.cursor()
#             print(f"connectted  to {self.db}")
            
#         except Exception as E:
#             print(f"Connection failed due to {E}")

#     def __exit__(self, exception_type, exception_val, exception_traceback):
#         self.conn.commit()
#         self.cursor.close()
#         self.conn.close()
        
#     # def fetch_one(self, query):
#     #     q = self.cursor.execute(query)
#     #     row = self.cursor.fetchone()
#     #     if row is not None:
#     #         return row
#     #     return "Item not founnd"        
        




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

        
        
        