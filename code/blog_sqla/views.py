from flask import render_template
from sqlalchemy.orm import *
from blog import app
from models import Post, Author, Category


@app.route('/')
def index():
    posts = Post.query.join(Author).options(joinedload('author')).all()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>')
def single_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('single_post.html', post=post)


@app.route('/author/<int:author_id>')
def author(author_id):
    author = Author.query.get_or_404(author_id)
    posts = Post.query.filter(Post.author_id == author_id).all()
    return render_template('author.html', author=author, posts=posts)


@app.route('/category/<int:category_id>')
def category(category_id):
    category = Category.query.get_or_404(category_id)
    posts = Post.query.filter(Post.category_id == category_id).all()
    return render_template('category.html', category=category, posts=posts)
