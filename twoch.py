#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import os
import logging
from collections import defaultdict
from flask import Flask, request, render_template, g, jsonify, request
from contextlib import closing

DATABASE = "/home/www-data/flask_app/twoch/downloaded.sqlite"
# DATABASE = "/tmp/twoch.db"
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

def get_db():
    db = getattr(g, "_db", None)
    if db is None:
        db = g._db = connect_db()
    db.row_factory = sqlite3.Row
    return db

def connect_db():
    return sqlite3.connect(app.config["DATABASE"])

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_db", None)
    if db is not None:
        db.close()

def query_db(query, args = (), one = False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route("/")
def hello():
    return render_template("start.html")

@app.route("/dat")
def dat():
    sidebar_contents = defaultdict(lambda: defaultdict(dict))
    for thread in query_db("SELECT * FROM downloaded_thread"):
        sidebar_contents[thread["download_date"]][thread["title"]] = thread["id"]
    return render_template("dat.html", sidebar_contents = sidebar_contents)

@app.route("/_get_dat")
def get_dat():
    thread_id = request.args.get("thread_id", 0, type=int)
    return jsonify(result = thread_id)

@app.route("/img")
def img():
    return render_template("img.html", sidebar = sidebar)

if __name__ == "__main__":
    app.run(host = "157.7.141.207", port = 3000)
