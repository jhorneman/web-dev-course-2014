"""A minimal web server using Flask. A third page shows a run-time error, and the in-browser debugger."""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/other')
def other():
    return 'Another page!'

@app.route('/wrong')
def wrong():
    return 1 / 0


app.debug = True
app.run()
