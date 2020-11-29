from flask import Flask, render_template  #allows to return html templates instead of manually generated layouts

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html', name='Roman') #passing a variable to the html placeholder, allows to present dynamic content for different users

@app.route('/hi')
def hi_there():
    return 'Hi there, pretty!'


if __name__ == '__main__':
    app.run(debug=1)
