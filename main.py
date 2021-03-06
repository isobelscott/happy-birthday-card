#!/usr/bin/python

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/30ans")
def trente():
    return render_template("trente.html")

if __name__ == "__main__":
    app.run(debug=True)