from flask import Flask, render_template
app = Flask(__name__)


boxes = [
    {
        'source': 'New York Times',
        'title': 'News Box 1',
        'content': 'Dummy dummy news',
        'date': 'April 23, 2021'
    },
    {
        'source': 'Washington Post',
        'title': 'News Box 2',
        'content': 'Bezos Bezos news',
        'date': 'April 22, 2021'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', boxes=boxes)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)