from flask import (
    Flask,
    abort,
    flash,
    render_template,
    request,
    redirect,
    session,
    url_for,
)  # allows to return html templates instead of manually generated layouts
from werkzeug.utils import secure_filename
import json
import os.path

app = Flask(__name__)
app.secret_key = "sdhfosaljsafkjdal"


@app.route("/")
def hello_world():
    # passing a variable to the html placeholder, allows to present dynamic content for different users
    return render_template("home.html", name="by Roman")


@app.route("/hi")
def hi_there():
    return "Hi there, pretty!"


@app.route(
    "/your-url", methods=["GET", "POST"]
)  # the action after submitting the form in home.html leads to your-url
def your_url():
    # once the if/else defines that there is a POST or GET request,
    # the value of 'code' is passed to the template your-url.html without presenting parameters inside the request url
    if request.method == "POST":
        urls = {}

        if os.path.exists('urls.json'):
            with open('urls.json') as url_file:
                urls = json.load(url_file)

        if request.form['code'] in urls.keys():
            flash('This shortname has already been taken. Please select another one')
            return redirect(url_for('hello_world'))

        if 'url' in request.form.keys():
            urls[request.form["code"]] = {"url": request.form["url"]}
        else:
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename)
            f.save('/media/disertus/3CFE4AD4FE4A865C/Programming-Materials/Python-Programs/Flask-Link-shortener-app/' + full_name)
            urls[request.form["code"]] = {"file": full_name}

        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
        # args = dictionary for parameters that can be passed. here it represents the value passed to 'code' inside the home.html form
        return render_template(
            "your_url.html", code=request.form["code"]
        )  # .form is used with POST requests
    else:
        # redirect looks for url addresses to redirect the user
        # return redirect('/')

        # redirects to the home page as above, but instead of hardcoded url uses the value of the function 'home'
        return redirect(url_for("hello_world"))

@app.route('/<string:code>')
def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
    return abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == "__main__":
    app.run(debug=1)
