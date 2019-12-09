from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "This is the Index page"


@app.route('/hello')
def hello():
    return "Hello World!"


@app.route('/member')
def members(member):
    return 'Members Page'


@app.route('/scores/<int:scr>')
def scores(scr):
    return render_template('index.html', score=scr)


@app.route('/three')
def exercise3():
    return render_template('index3.html')


if __name__ == '__main__':
    app.run(debug=False)
