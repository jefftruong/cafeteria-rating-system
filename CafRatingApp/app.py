# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# app.py
from flask import Flask, render_template, request, redirect, url_for
import time

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/s0', methods=['GET', 'POST'])
def s0():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        print("inside s0 python function")
        return redirect(url_for('home'))

    # show the form, it wasn't submitted
    return render_template('s0')


if __name__ == '__main__':
    app.run(debug=True, port=9000)
