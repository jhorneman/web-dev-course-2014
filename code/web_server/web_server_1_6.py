"""A minimal web server using Flask. A better way to do the previous example."""

from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    if name:
        return 'Hello ' + name
    else:
        return 'Hello you'

app.debug = True
app.run()
