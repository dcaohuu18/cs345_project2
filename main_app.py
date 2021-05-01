from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import TagManagerForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '2bef5d15c401ca68c97d70bf8ead5998'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class Tag(db.Model):
    tag_text = db.Column(db.String(500), primary_key=True)
    tag_status = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"Tag('{self.tag_text}', '{self.tag_status}')"


class Article(db.Model):
    article_url = db.Column(db.String(2048), primary_key=True)
    article_source = db.Column(db.String(500))
    article_title = db.Column(db.String(200), nullable=False)
    article_date = db.Column(db.DateTime)
    article_content = db.Column(db.Text, nullable=False)
    article_thumbnail_url = db.Column(db.String(2048), default="default_thumbnail.jpeg")
    # foreign key:
    # other table references:
    # col = db.relationship('other_table', backref='other_table_col', lazy=True)

    # references other table:
    # col = db.Column(db.type, db.ForeignKey('other_table.col'))

    def __repr__(self):
        return f"Article('{self.article_title}', '{self.article_date}')"


boxes = [
    {
        'source': 'New York Times',
        'title': 'News Box 1',
        'content': 'Dummy dummy news',
        'thumbnail_url': 'http://i3.ytimg.com/vi/snAhsXyO3Ck/maxresdefault.jpg',
        'date': 'April 23, 2021'
    },
    {
        'source': 'Washington Post',
        'title': 'News Box 2',
        'content': 'Bezos Bezos news',
        'thumbnail_url': 'https://www.thecoderpedia.com/wp-content/uploads/2020/06/Coding-Meme-Code-Comments-be-Like-925x1024.jpg?x78269',
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


@app.route('/tag-manager', methods=['GET', 'POST'])
def tag_manager():
    tag_manager_form = TagManagerForm()
    if tag_manager_form.validate_on_submit():
        flash('Your interest tags were successfully updated!', 'success')
        return redirect(url_for('home')) # redirect to home
    return render_template('tag_manager.html', 
                            title='Tag Manager', 
                            form=tag_manager_form)


if __name__ == '__main__':
    app.run(debug=True)
