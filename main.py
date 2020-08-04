from app import create_app


app = create_app()


@app.route('/')
def index():
    return "Hello World"


@app.route('/about')
def about():
    return 'About'


@app.route('/<paste_id>')
def paste_bin(paste_id):
    return paste_id
