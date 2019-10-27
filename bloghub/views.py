from flask import render_template, url_for, flash, redirect
from bloghub import app, db, bcrypt
from bloghub.forms import RegistrationForm, LoginForm
from bloghub.models import User, Post


posts = [
    {
        'author': 'Tyra Hans',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Ren Oyuo',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
def home():
    return render_template('index.html', posts=posts)

@app.route("/register", methods=['GET','POST'])

def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data , email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('Account created!, please log in','success')
        return redirect (url_for('login'))

    return render_template('register.html', title='Register', form=form)

@app.route("/login",methods=['GET','POST'])

def login():
    form= LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

