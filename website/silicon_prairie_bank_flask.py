from flask import Flask, render_template, jsonify, send_from_directory, request
import pandas as pd
import numpy as np
import os
import pickle
from modelHelper import ModelHelper
from modelHelperld import ModelHelperld
import json

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
model_helper = ModelHelper()
model_helper_ld = ModelHelperld()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data_cc")
def data_cc():
    return render_template("data_cc.html")

@app.route("/data_l")
def data_l():
    return render_template("data_l.html")

@app.route("/references")
def references():
    return render_template("references.html")

@app.route("/credit_card")
def credit_card():
    return render_template("credit_card.html")

@app.route("/loan")
def loan():
    return render_template("loan.html")

@app.route("/tableau_cc")
def tableau_cc():
    return render_template("tableau_cc.html")

@app.route("/tableau_cc2")
def tableau_cc2():
    return render_template("tableau_cc2.html")

@app.route("/tableau_ld")
def tableau_ld():
    return render_template("tableau_ld.html")

@app.route("/tableau_ld_map")
def tableau_ld_map():
    return render_template("tableau_ld_map.html")

@app.route("/tableau_ld_map2")
def tableau_ld_map2():
    return render_template("tableau_ld_map2.html")



@app.route("/makePredictions", methods=["POST"])
def makePredictions():
    content = request.json["data"]
    print(content)
    pred = model_helper.makePredictionss(content)
    return(jsonify({"ok": True, "prediction": pred}))

@app.route("/makePredictionsld", methods=["POST"])
def makePredictionsld():
    content = request.json["data"]
    print(content)
    pred = model_helper_ld.makePredictionssld(content)
    print(pred)
    #pred = [1, 0.65]
    return(jsonify({"ok": True, "prediction": pred}))


#####################################################################
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)
