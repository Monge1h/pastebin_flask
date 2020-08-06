from app import create_app
from flask import render_template
import unittest

app = create_app()


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')

    unittest.TextTestRunner().run(tests)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return 'About'


@app.route('/<paste_id>')
def paste_bin(paste_id):
    return paste_id
