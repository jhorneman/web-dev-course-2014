"""A minimal web server using Flask, with a second page."""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/other')
def other():
    return 'Another page!'


app.debug = True
app.run()
