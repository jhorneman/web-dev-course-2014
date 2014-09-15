from flask import Flask, render_template
from db import connect_db


app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    db = connect_db()
    cursor = db.execute('select authors.name, posts.title, posts.content from authors, posts where authors.id = posts.author_id')
    posts = [dict(author_name=row[0], title=row[1], content=row[2]) for row in cursor.fetchall()]
    db.close()
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run()
