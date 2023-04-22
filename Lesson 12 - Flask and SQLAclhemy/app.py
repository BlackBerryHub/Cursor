from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.secret_key = 'very_secret_key'
db.init_app(app)

with app.app_context():
    from routes import *
    from models import User

    migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)
