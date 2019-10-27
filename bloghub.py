from flask import Flask, render_template, url_for
app = Flask(__name__)

app.config['SECRET_KEY']= '1371ce8114eac4891b9b92bcea6ecd46'

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


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)