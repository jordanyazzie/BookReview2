import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    content = db.Column(db.Text)


    def __repr__(self):
        return '< Category %r >' % self.name

class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True, index=True)
    author = db.Column(db.String(64))
    description = db.Column(db.Text)

    def __repr__( self):
        return '< Books %r >' % self.title







@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mystery')
def mystery():
    return render_template('mystery.html')

@app.route('/mysteryBookOne')
def mysterybookone():
    return render_template('mysteryBookOne.html')

@app.route('/mysteryBookTwo')
def mysterybooktwo():
    return render_template('mysteryBookTwo.html')

@app.route('/mysteryBookThree')
def mysterybookthree():
    return render_template('mysteryBookThree.html')


@app.route('/nonFiction')
def nonfiction():
    return render_template('nonFiction.html')

@app.route('/nonFictionBookOne')
def nonfictionbookone():
    return render_template('nonFictionBookOne.html')

@app.route('/nonFictionBookTwo')
def nonfictionbooktwo():
    return render_template('nonFictionBookTwo.html')

@app.route('/nonFictionBookThree')
def nonfictionbookthree():
    return render_template('nonFictionBookThree.html')


@app.route('/poetry')
def poetry():
    return render_template('poetry.html')

@app.route('/poetryBookOne')
def poetrybookone():
    return render_template('poetryBookOne.html')

@app.route('/poetryBookTwo')
def poetrybooktwo():
    return render_template('poetryBookTwo.html')

@app.route('/poetryBookThree')
def poetrybookthree():
    return render_template('poetryBookThree.html')


if __name__ == '__main__':
    app.run()