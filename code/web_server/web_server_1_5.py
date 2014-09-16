"""A minimal web server using Flask. The view gets a parameter but also works with without one."""

from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
def hello_world():
    return 'Hello you'

@app.route('/hello/<name>')
def hello_world_name(name):
    return 'Hello ' + name

app.debug = True
app.run()
