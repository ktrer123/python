from flask import Flask, render_template

app = Flask("SuperScrapper")

@app.route("/")
def hello_world():
    return render_template("potato.html")

@app.route("/<username>")
def contact():
    return "Hello your name is"

app.run(host="")