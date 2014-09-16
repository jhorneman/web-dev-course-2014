import os
import re
import codecs
from high_score import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    posts = db.relationship('Post', backref='author',
                             lazy='dynamic')


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    posts = db.relationship('Post', backref='category',
                             lazy='dynamic')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))


def create_db():
    db.drop_all()
    db.create_all()

    with codecs.open('data' + os.sep + 'authors.txt', 'r', 'utf-8') as f:
        for data in f.readlines():
            new_author = Author()
            new_author.name = data.strip()
            db.session.add(new_author)

    with codecs.open('data' + os.sep + 'categories.txt', 'r', 'utf-8') as f:
        for data in f.readlines():
            new_category = Category()
            new_category.name = data.strip()
            db.session.add(new_category)

    with codecs.open('data' + os.sep + 'posts.txt', 'r', 'utf-8') as f:
        regex = re.compile(r'^(\d+),\s*(\d+),\s*"(.*)",\s*"(.*)"')
        for data in f.readlines():
            post_data = regex.match(data)
            if post_data:
                new_post = Post()
                new_post.title = unicode(post_data.group(3))
                new_post.content = unicode(post_data.group(4))
                new_post.author_id = int(post_data.group(1))
                new_post.category_id = int(post_data.group(2))
                db.session.add(new_post)
            else:
                print "Couldn't parse line."

    db.session.commit()
