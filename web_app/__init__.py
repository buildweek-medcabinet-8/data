from flask import Flask
from web_app.routes.home_routes import home_routes
from web_app.routes.insert_routes import insert_routes
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

db = SQLAlchemy()

migrate = Migrate()

def create_app():

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "temporary secret key"

    # app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL

    db.init_app(app)
    # # migrate.init_app(app, db)
    migrate = Migrate(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(insert_routes)

    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
