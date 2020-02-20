#!/usr/bin/env python3

"""
Something I can throw tasks at
and then later maybe do them
starting with an API,
will do a web interface later
"""


from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    """Index route function"""
    return jsonify("Hello, World!")

if __name__ == '__main__':
    app.run()
