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
            for data in [\
                ("Jurie", 3000),
                ("Jurie", 2000),
                ("Jurie", 1000),
                ("Jurie", 4000)
            ]:
                cursor.execute('insert into scores (player_name, score) values (?,?)', data)
        db.commit()


if __name__ == "__main__":
    init_db()
