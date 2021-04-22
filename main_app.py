from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return "<h1>Hello, I'm Dong!</h1><h1>And I'm Liam!</h1>"


@app.route('/about')
def about():
    return "<h1>About Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
