import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def hello(name):
    return render_template("hello.html", name=name)


@app.route("/omikuji/")
def omikuji():
    fortune = [ "大吉", "吉", "凶" ]
    chose = random.randint(0, 2)
    result = fortune[ chose ]
    return render_template("omikuji.html", omikuji=result)


@app.route("/dice")
def dice():
    result = random.choice([ 1, 2, 3, 4, 5, 6 ])
    return render_template("dice.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
