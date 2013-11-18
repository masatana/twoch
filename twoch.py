#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import os
import logging
from collections import defaultdict, OrderedDict
from flask import Flask, request, render_template, g, jsonify, request
from contextlib import closing
import xml.sax.saxutils as xss

#DATABASE = "/home/www-data/flask_app/twoch/downloaded.sqlite"
DATABASE = "/home/masatana/2ch_crawler/downloaded.sqlite"
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
    return render_template("dat.html", sidebar_contents = sidebar_contents, data = {})

@app.route("/_get_dat")
def get_dat():
    sidebar_contents = defaultdict(lambda: defaultdict(dict))
    for thread in query_db("SELECT * FROM downloaded_thread"):
        sidebar_contents[thread["download_date"]][thread["title"]] = thread["id"]
    g.sidebar_contents = sidebar_contents
    thread_id = request.args.get("thread_id", 0, type=int)
    t = (thread_id,)
    res = query_db("SELECT * FROM downloaded_thread WHERE id=?", args=t)
    data = defaultdict(dict)
    with open("/home/masatana/2ch_crawler/dat/" + res[0]["download_date"] + "/" + res[0]["title"] + ".dat", "r") as f:
        return jsonify(result = f.read())

@app.route("/img")
def img():
    return render_template("img.html", sidebar = sidebar)

if __name__ == "__main__":
    app.run(host = "157.7.141.207", port = 3000)
