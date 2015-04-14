#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, session, request, render_template, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
