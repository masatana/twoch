#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
app = Flask(__name__)


# Configuration
DATABASE = None
DEBUG = True
SECRET_KEY = "development key"

@app.route("/")
def hello():
    return render_template("start.html")

@app.route("/dat")
def dat():
    return render_template("dat.html")

@app.route("/img")
def img():
    return render_template("img.html")

if __name__ == "__main__":
    app.run(host = "157.7.141.207", port = 3000)
