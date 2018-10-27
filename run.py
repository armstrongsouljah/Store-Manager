from flask import Flask
from app import app
from app.database.server import DatabaseConnection

if __name__ == '__main__':
    DatabaseConnection()
    app.run(debug=True, port=5400)
    


