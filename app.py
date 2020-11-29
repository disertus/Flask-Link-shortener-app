from flask import (
    Flask,
    render_template,
    request,
)  # allows to return html templates instead of manually generated layouts

app = Flask(__name__)


@app.route("/")
def hello_world():
    # passing a variable to the html placeholder, allows to present dynamic content for different users
    return render_template("home.html", name="by Roman")


@app.route("/hi")
def hi_there():
    return "Hi there, pretty!"


@app.route(
    "/your-url", methods=['GET', 'POST']
)  # the action after submitting the form in home.html leads to your-url
def your_url():
    if request.method == 'POST':
        # args = dictionary for parameters that can be passed. here it represents the value passed to 'code' inside the home.html form
        return render_template("your_url.html", code=request.form["code"]) #.form is used with POST requests
    else:
        return 'This is not valid'


if __name__ == "__main__":
    app.run(debug=1)
