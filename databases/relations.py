from werkzeug.security import generate_password_hash as g


commands = (
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
                CREATE TABLE IF NOT EXISTS categories(
                    category_id SERIAL PRIMARY KEY,
                    category_name VARCHAR(56) UNIQUE NOT NULL,
                    created_at TIMESTAMPTZ DEFAULT NOW()
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
                
                f"""
                INSERT INTO users(username, password, admin)      
                VALUES('admin','{g("testing123")}' ,True)
                """,
                f"""
                INSERT INTO users(username, password)
                VALUES('nonadmin','{g("testing123")}')
                
                """
)
