from app import create_app
from flask import render_template, url_for, redirect
from app.forms import PasteBinForm
import unittest

app = create_app()


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')

    unittest.TextTestRunner().run(tests)


@app.route('/', methods=['GET', 'POST'])
def index():
    paste_bin_form = PasteBinForm()

    context = {
        'paste_bin_form': paste_bin_form
    }

    if paste_bin_form.validate_on_submit():
        paste_bin = paste_bin_form.paste.data
        return redirect(url_for('paste_bin', paste_id=paste_bin))

    return render_template('home.html', **context)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/<paste_id>')
def paste_bin(paste_id):
    context = {
        'paste_id': paste_id
    }

    return render_template('paste_bin.html', **context)
