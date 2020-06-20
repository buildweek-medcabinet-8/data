from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from sqlalchemy import create_engine
# import psycopg2
# from psycopg2.extras import DictCursor
# import os
# import pandas as pd

db = SQLAlchemy()
migrate = Migrate()

# DB_URL = os.getenv("DB_URL")
# connection = psycopg2.connect(DB_URL)
# cursor = connection.cursor(cursor_factory=DictCursor)
# engine = create_engine(SQL_URL)

class Strains(db.Model):
    strain_id = db.Column(db.Integer, primary_key=True)
    strain = db.Column(db.String(128))
    strain_type = db.Column(db.String(128))
    rating = db.Column(db.Integer)
    effects = db.Column(db.String(128))
    flavor = db.Column(db.String(128))
    description = db.Column(db.String(128))
    
    # def __repr__(self):
        # return jsonify(UserData)

def upload_leafly_data():

    print("TODO")
    # DB_FILEPATH = os.path.join(os.path.dirname(__file__), "cannabis.csv")
    # df = pd.read_csv(DB_FILEPATH)
    # df.to_sql('leafly', engine, if_exists='replace', index=False)
    # connection.commit()

    # connection.close()

def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON

    Param: database_records (a list of db.Model instances)

    Example: parse_records(User.query.all())

    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records


    # def insert_leafly():
    # connection = psycopg2.connect(
    #     dbname=DB_NAME,
    #     user=DB_USER,
    #     password=DB_PASS,
    #     host=DB_HOST
    #     )
    # cursor = connection.cursor(cursor_factory=DictCursor)
    # engine = create_engine(SQL_URL)

    # query = """CREATE TABLE IF NOT EXISTS
    #             leafly(strain VARCHAR(50),
    #             type VARCHAR(50),
    #             rating FLOAT,
    #             effects VARCHAR(50),
    #             flavor VARCHAR(50),
    #             description VARCHAR(3000));"""

    # cursor.execute(query)
    # connection.commit()

    # DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "cannabis.csv")
    # df = pandas.read_csv(DB_FILEPATH)
    # df.to_sql('leafly', engine, if_exists='replace', index=False)
    # connection.commit()
    # connection.close()