from flask import Flask, Blueprint, render_template, request
from web_app.model import upload_leafly_data
from web_app.models import nlp_model 
# from nlp_model import Predictions

insert_routes = Blueprint("insert_routes", __name__)

predictor = nlp_model.Predictor()

@insert_routes.route("/")
def index():
    return render_template("home.html")

@insert_routes.route("/user_data")
def get_data():
    return render_template('effects_flavors.html')

@insert_routes.route("/print_data", methods=["POST"])
def display_data():
    # converts data from from into a dictionary
    data = dict(request.form)

    # extracts the list of flavors and effects from the dictionary
    user_data = data['Flavors/Effects'].split(sep=',')
    # you can pass user_data to ruby's model
    data = predictor.predict(user_data)
    print(type(data))
    # breakpoint()
    print(data)
    return "TODO"

@insert_routes.route("/insert_leafly")
def leafly_db():
    upload_leafly_data()
    
    return ('Successfly Inserted CSV to Database')
