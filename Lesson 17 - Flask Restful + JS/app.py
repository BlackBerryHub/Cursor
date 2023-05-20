from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api


app = Flask(__name__)
api = Api(app)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1111@db:3306/blog"
app.secret_key = "very_very_secret_key"
db.init_app(app)

with app.app_context():
    from routes import *
    from models import User

    migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)

