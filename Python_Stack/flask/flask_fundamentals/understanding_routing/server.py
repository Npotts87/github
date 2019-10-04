from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return ("Hello World")
@app.route("/dojo")
def index():
    return ("Dojo!")
@app.route("/flask")
def index():
    return ("Hi Flask!")
@app.route("/jim")
def index():
    return ("Hi Jim!")
@app.route("/michael")
def index():
    return ("Hi Michael!")

if __name__ == "__main__":
    app.run(debug=True)