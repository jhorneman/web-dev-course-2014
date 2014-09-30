# coding: utf8

import unittest
# from lxml import etree
# from lxml.cssselect import CSSSelector
from application import create_app
from create_db import create_db


app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False


class FormsTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            create_db(app.db)

    def test_index_page(self):
        rv = self.client.get('/')
        assert "Registered users" in rv.data

    def test_add_user_works(self):
        rv = self.client.post('/full', data=dict(
            name="Jimmy",
            email_address="a@b.org"
        ), follow_redirects=True)
        assert "has been registered!" in rv.data

    def test_add_user_works_with_birthday(self):
        rv = self.client.post('/full', data=dict(
            name="Jimmy",
            email_address="a@b.org",
            birthday="23-01-1974"
        ), follow_redirects=True)
        assert "has been registered!" in rv.data

    def test_add_user_requires_name(self):
        rv = self.client.post('/full', data=dict(
            email_address="a@b.org"
        ), follow_redirects=True)
        # html = etree.HTML(rv.data)
        # errors = html.cssselect("")
        # sel = CSSSelector("ul.formerrors")
        # print [e for e in sel(html)]
        assert "This field is required" in rv.data


if __name__ == '__main__':
    unittest.main()
