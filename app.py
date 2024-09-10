from flask import Flask

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def welcome():
    return "<h1> This is my firs web application </h1>"

@app.route("/index", methods = ["GET"])
def index():
    return "<h1>Welcome to the Index page</h1>"





if __name__ == "__main__":
    app.run(debug=True)