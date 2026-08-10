from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! IT's Danish Naeem world Enjoy the world of Flask APP"

@app.route("/about")
def about():
    return "This is the about page of the Flask APP. Created by Danish Naeem."




if __name__ == "__main__":
    app.run(debug=True)
