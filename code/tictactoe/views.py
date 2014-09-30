from flask import render_template, redirect, request, flash, url_for
from application import app
from models import GameState


@app.route('/')
def index():
    return render_template('layout.html')
