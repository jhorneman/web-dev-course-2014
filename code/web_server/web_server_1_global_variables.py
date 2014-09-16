"""A minimal web server using Flask. An attempt to show how not to handle persistent data in a web server."""

from flask import Flask

app = Flask(__name__)

counter = 0

@app.route('/')
def hello_world():
    global counter
    msg = 'Hello! The counter value is ' + str(counter)
    counter += 1
    return msg

app.debug = False
app.run()
