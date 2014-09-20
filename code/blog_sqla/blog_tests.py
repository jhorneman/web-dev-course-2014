# coding: utf8

import unittest
from blog import create_app
from db import create_db


app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['TESTING'] = True


class BlogTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            create_db(app.db)

    def test_index_page(self):
        rv = self.client.get('/')
        assert rv.data.count("in the category") == 4

    def test_single_post_page(self):
        rv = self.client.get('/post/1')
        assert "Problems that aren’t actually solvable" in rv.data

    def test_author_page(self):
        rv = self.client.get('/author/1')
        assert rv.data.count("in the category") == 2
        assert "Paris is a huge place" in rv.data
        assert "George Buckingham" in rv.data

    def test_category_page(self):
        rv = self.client.get('/category/1')
        assert "Problems that aren’t actually solvable" in rv.data

    def test_single_post_404(self):
        rv = self.client.get('/post/10')
        assert rv.status_code == 404

    def test_author_404(self):
        rv = self.client.get('/author/10')
        assert rv.status_code == 404

    def test_category_404(self):
        rv = self.client.get('/category/10')
        assert rv.status_code == 404


if __name__ == '__main__':
    unittest.main()
