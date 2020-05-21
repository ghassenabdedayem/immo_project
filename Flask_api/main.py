import flask
from flask import request, jsonify, render_template
import pandas as pd
import time

app = flask.Flask(__name__)
app.config["DEBUG"] = True

start = time.time()

file_name = '../Data_assets/Processed/Paris_selection/reduced_data.csv'

df = pd.read_csv(
    file_name,
    low_memory=False,
    parse_dates=[2],
    squeeze=True
)

dictionaty = df.to_dict()


@app.route('/', methods=['GET'])
def home():
    return render_template("template.html", 
                            name = 'Immo DataFrame',
                            data = df)

app.run()