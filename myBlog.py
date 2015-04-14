#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, session, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:louis@localhost/blog'
db = SQLAlchemy(app)

@app.route('/')
def index():
    print "from index"
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run()
