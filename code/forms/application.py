from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension


app = None
db = SQLAlchemy()


def create_app():
    global app
    app = Flask(__name__)
    app.config.from_object('config')

    import views

    global db
    db.init_app(app)
    app.db = db

    import models

    DebugToolbarExtension(app)

    return app
