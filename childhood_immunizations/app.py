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

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app)

from .models import Measles

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# Query the database and send the jsonified results
@app.route("/data")
def data():
    sel = [Measles.States, Measles.Counts]
    results = db.session.query(*sel).\
        group_by(Measles.States).all()
    df = pd.DataFrame(results, columns=['States', 'Counts'])
    return jsonify(df.to_dict(orient="records"))



if __name__ == "__main__":
    app.run()
