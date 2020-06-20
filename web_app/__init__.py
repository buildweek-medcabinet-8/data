# web_app/__init__.py
from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()


from web_app.models import db
from web_app.routes.insert_routes import insert_routes
from flask_migrate import Migrate

DATABASE_URL = os.getenv("DB_URL")


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    db.init_app(app)
    # migrate.init_app(app, db)
    migrate = Migrate(app, db)

    app.register_blueprint(insert_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)