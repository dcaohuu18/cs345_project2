from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LogInForm
app = Flask(__name__)

#This is for security related things, but we can probably remove this later since this won't be a full site.
app.config["SECRET_KEY"] = "ce3849517d955c046577533c679b0a5e"

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Failed. Check your info and try again.', 'danger')
    return render_template('login.html', title='Log In', form=form)

if __name__ == '__main__':
    app.run(debug=True)
