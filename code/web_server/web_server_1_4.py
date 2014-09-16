"""A minimal web server using Flask. The view gets a parameter."""

from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
    return 'Hello ' + name

app.debug = True
app.run()
