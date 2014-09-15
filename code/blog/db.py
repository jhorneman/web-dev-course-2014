import os
import codecs
import re
from contextlib import closing
import sqlite3
from config import DATABASE as db_path


def connect_db():
    return sqlite3.connect(db_path)


def init_db():
    with closing(connect_db()) as db:
        with open('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

        with closing(db.cursor()) as cursor:
            with open('data' + os.sep + 'authors.txt') as f:
                for data in f.readlines():
                    cursor.execute('insert into authors (name) values (?)', [data.strip()])

        with closing(db.cursor()) as cursor:
            with open('data' + os.sep + 'categories.txt') as f:
                for data in f.readlines():
                    cursor.execute('insert into categories (name) values (?)', [data.strip()])

        with closing(db.cursor()) as cursor:
            with codecs.open('data' + os.sep + 'posts.txt', 'r', 'utf-8') as f:
                regex = re.compile(r'^(\d+),\s*(\d+),\s*"(.*)",\s*"(.*)"')
                for data in f.readlines():
                    post_data = regex.match(data)
                    if post_data:
                        author_id = int(post_data.group(1))
                        category_id = int(post_data.group(2))
                        title = unicode(post_data.group(3))
                        content = unicode(post_data.group(4))
                        cursor.execute(u'insert into posts (author_id, category_id, title, content) values (?,?,?,?)',
                                       (author_id, category_id, title, content))
                    else:
                        print "Couldn't parse line."
        db.commit()


if __name__ == "__main__":
    init_db()
