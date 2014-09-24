import os
import re
import codecs
from blog import create_app
from models import Post, Author, Category


def create_db(db):
    db.drop_all()
    db.create_all()

    with codecs.open('data' + os.sep + 'authors.txt', 'r', 'utf-8') as f:
        for data in f.readlines():
            data = data.strip()
            if not data:
                continue
            new_author = Author()
            new_author.name = data
            db.session.add(new_author)

    with codecs.open('data' + os.sep + 'categories.txt', 'r', 'utf-8') as f:
        for data in f.readlines():
            data = data.strip()
            if not data:
                continue
            new_category = Category()
            new_category.name = data
            db.session.add(new_category)

    with codecs.open('data' + os.sep + 'posts.txt', 'r', 'utf-8') as f:
        regex = re.compile(r'^(\d+),\s*(\d+),\s*"(.*)",\s*"(.*)"')
        for data in f.readlines():
            data = data.strip()
            if not data:
                continue
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


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        create_db(app.db)
