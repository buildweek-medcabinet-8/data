from flask import Flask, Blueprint
# from flask import Blueprint
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from sqlalchemy import create_engine
# import psycopg2
# from psycopg2.extras import DictCursor
# # import pandas
# import os

# from dotenv import load_dotenv
# load_dotenv()
# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASS = os.getenv("DB_PASS")
# DB_HOST = os.getenv("DB_HOST")
# SQL_URL = os.getenv("SQL_URL")
# DB_NAME = 'cyarxgrz'
# DB_USER = 'cyarxgrz'
# DB_PASS = '2QQLDECBgrYioavOEavWO5X2Uv3VGu5A'
# DB_HOST = 'ruby.db.elephantsql.com'
# SQL_URL = 'postgres://cyarxgrz:2QQLDECBgrYioavOEavWO5X2Uv3VGu5A@ruby.db.elephantsql.com:5432/cyarxgrz'

insert_routes = Blueprint("insert_routes", __name__)

@insert_routes.route("/")
def index():
    return render_template("home.html")

@insert_routes.route("/insert_leafly")
def leafly_db():
    return ('Successfly Inserted CSV to Database')
