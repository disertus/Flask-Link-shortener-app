from flask import (
    Flask,
    flash,
    render_template,
    request,
    redirect,
    url_for,
)  # allows to return html templates instead of manually generated layouts
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

        urls[request.form["code"]] = {"url": request.form["url"]}
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


if __name__ == "__main__":
    app.run(debug=1)
