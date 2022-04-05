from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello sravani"


@app.route("/index")
def show():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
