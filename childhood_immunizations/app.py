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

class Vaccines(db.Model):
    __tablename__ = 'Vaccines'

    id = db.Column(db.Integer, primary_key=True)
    State = db.Column(db.String(15))
    Measles_cases_2019 = db.Column(db.Integer)
    Mumps_cases_2019 = db.Column(db.String)
    Pertussis_cases_2018 = db.Column(db.Integer)
    Religious_Exemption = db.Column(db.String(10))
    Philosophical_Exemption = db.Column(db.String(10))

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# Query the database and send the jsonified results
@app.route("/maps")
def maps():
    return render_template("maps.html")

@app.route("/Mumps")
def mumps():
    return render_template("mumps.html")

@app.route("/Measles")
def measles():
    return render_template("measles.html")

@app.route("/Pertussis")
def pertussis():
    return render_template("pertussis.html")

@app.route("/PhilosophicalExemptions")
def philosophical():
    return render_template("philosophical.html")

@app.route("/ReligiousExemptions")
def religious():
    return render_template("religious.html")

if __name__ == "__main__":
    app.run()

@app.route("/vaccines")
def vaccines():
    cases = db.session.query(Vaccines.State, Vaccines.Count, Vaccines.Measles_cases_2019, Vaccines.Mumps_cases_2019, \
        Vaccines.Pertussis_cases_2018, Vaccines.Religious_Exemption, Vaccines.Philosophical_Exemption)\
            .all()
    print(jsonify(cases))