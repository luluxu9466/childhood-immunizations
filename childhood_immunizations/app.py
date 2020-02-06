# import necessary libraries
import os
import pandas as pd
from sqlalchemy import func
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)

class Measles(db.Model):
    __tablename__ = 'Measles Data'

    id = db.Column(db.Integer, primary_key=True)
    States = db.Column(db.String(15))
    Counts = db.Column(db.Integer)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# Query the database and send the jsonified results
@app.route("/data")
def data():
    data = db.session.query(Measles.States, Measles.Counts).all()

@app.route("/maps")
def maps():
    return render_template("maps.html")

if __name__ == "__main__":
    app.run()
