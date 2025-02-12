from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/products")
def hello_products():
    return "<p>This is Products page</p>"

@app.route("/about")
def about():
    return "<p>This is about us page</p>"

if __name__ == "__main__":
    app.run(debug=True, port=8000)
