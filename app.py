from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/eat")
def eat():
    return render_template("eat.html")

@app.route("/move")
def move():
    return render_template("move.html")

@app.route("/rest")
def rest():
    return render_template("rest.html")

@app.route("/heart")
def heart():
    return render_template("heart.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)