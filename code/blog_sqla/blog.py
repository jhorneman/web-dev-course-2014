from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import *
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from db import *
toolbar = DebugToolbarExtension(app)


@app.route('/')
def index():
    posts = Post.query.join(Author).options(joinedload('author')).all()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>')
def single_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('single_post.html', post=post)


if __name__ == '__main__':
    app.run()
