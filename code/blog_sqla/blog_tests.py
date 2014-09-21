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
        assert "Problems that aren’t actually solvable" in rv.data
        assert rv.data.count("in the category") == 4

    def test_category_404(self):
        rv = self.client.get('/category/10')
        assert rv.status_code == 404


if __name__ == '__main__':
    unittest.main()
