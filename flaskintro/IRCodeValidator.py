# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# IRCodeValidator.py

import flask
app = flask.Flask(__name__)

@app.route('/')
def home():
    return "ID:12345"

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
