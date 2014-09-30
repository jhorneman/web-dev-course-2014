from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from models import GameState


app = None


def create_app():
    global app
    app = Flask(__name__)
    app.config.from_object('config')

    import views

    import models
    app.gs = GameState()

    DebugToolbarExtension(app)

    return app
