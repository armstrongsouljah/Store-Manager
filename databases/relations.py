from werkzeug.security import generate_password_hash as g


commands = (
                """
                        CREATE TABLE IF NOT EXISTS  users(
                            user_id SERIAL PRIMARY KEY,
                            username VARCHAR(35) NOT NULL UNIQUE,
                            password VARCHAR(240) NOT NULL, 
                            role VARCHAR(23),
                            registered_at TIMESTAMP DEFAULT NOW()
                    )
                """,
                """
                CREATE TABLE IF NOT exists categories(
                    category_id SERIAL PRIMARY KEY,
                    category_name VARCHAR(49) UNIQUE,
                    date_added TIMESTAMPTZ DEFAULT NOW()
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS  products(
                    product_id SERIAL PRIMARY KEY,
                    product_name VARCHAR(38) NOT NULL UNIQUE,
                    category INTEGER references categories(category_id)
                    ON DELETE CASCADE,
                    quantity INTEGER NOT NULL,
                    unit_cost INTEGER NOT NULL,
                    created_at TIMESTAMP DEFAULT NOW()
                )
                """,

                """
                CREATE TABLE IF NOT EXISTS sales(
                    sale_id SERIAL PRIMARY KEY,
                    attendant INT references users(user_id)
                    ON DELETE CASCADE,
                    product_sold INT references products(product_id)
                    ON DELETE CASCADE,
                    quantity INT,
                    total_cost INT,
                    timestamp TIMESTAMPTZ DEFAULT NOW()
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS blacklisted(
                    token_id SERIAL PRIMARY KEY,
                    token_jti VARCHAR(90) UNIQUE
                )
                """,
                
                f"""
                INSERT INTO users(username, password, role)      
                VALUES('admin','{g("testing123")}' ,'admin')
                """,
                f"""
                INSERT INTO users(username, password, role)
                VALUES('nonadmin','{g("testing123")}', 'attendant')
                
                """,
                """
                INSERT INTO categories(category_name)
                VALUES('electronics')
                """,
                """
                INSERT INTO products(product_name, category, quantity, unit_cost)
                VALUES('samsung galaxy tab', 1, 34, 450000)
                """
)
