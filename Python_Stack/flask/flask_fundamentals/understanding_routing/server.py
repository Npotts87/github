from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def root():
    return ("Hello World")
@app.route("/dojo")
def dojo():
    return "<h1>Dojo!</h1>"
@app.route("/flask")
def flask():
    return "<h1><p style='color:lime'> Hi Flask! </p></h1>"
@app.route("/jim")
def jim():
    return ("Hi Jim!")
@app.route("/michael")
def michael():
    return ("Hi Michael!")
@app.route("/repeat/35")
def repeat():
    return int("*35")
@app.route("/hello")
def hello():
    return ("/hello")
if __name__ == "__main__":
    app.run(debug=True)