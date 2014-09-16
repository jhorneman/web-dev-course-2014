from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<string:name>')
def index(name):
    return render_template("hello_world.jinja2", name=name)

app.debug = True
app.run()
