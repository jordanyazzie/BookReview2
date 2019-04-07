from flask import Flask, render_template

app = Flask(__name__)

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