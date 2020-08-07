from flask_testing import TestCase
from flask import current_app, url_for

from main import app


class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True

        return app

    def test_app_exist(self):
        self.assertIsNotNone(current_app)

    def test_index_get(self):
        self.client.get(url_for('index'))

        self.assertTemplateUsed('home.html')

    def test_about_get(self):
        self.client.get(url_for('about'))

        self.assertTemplateUsed('about.html')
