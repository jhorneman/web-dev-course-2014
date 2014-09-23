from flask import render_template, jsonify, url_for
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


@app.route('/gen')
def gen():
    # return render_template('gen.html')
    # return render_template('gen_with_handlebars.html')
    return render_template('gen_with_localstorage.html')


@app.route('/api/posts')
def api():
    posts = Post.query.limit(2).all()

    post_ids = [post.id for post in posts]
    author_ids = set([post.author.id for post in posts])
    category_ids = set([post.category.id for post in posts])

    authors = Author.query.\
        filter(Author.id.in_(author_ids)).\
        all()

    authors = {author.id: dict(
        name=author.name,
        url=url_for('author', author_id=post.author.id)
    ) for author in authors}

    categories = Category.query.\
        filter(Category.id.in_(category_ids)).\
        all()

    categories = {category.id : dict(
        name=category.name,
        url=url_for('category', category_id=post.category.id)
    ) for category in categories}

    posts = {post.id : dict(
        id=post.id,
        title=post.title,
        content=post.content,
        author_id=post.author.id,
        category_id=post.category.id,
        url=url_for('single_post', post_id=post.id)
    ) for post in posts}

    data = {
        'authors': authors,
        'categories': categories,
        'posts': posts
    }

    return jsonify(data)
