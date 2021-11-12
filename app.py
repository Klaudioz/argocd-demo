from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def index():
    return "Hello world"

@app.route("/")
def home():
    return "This is the homepage"

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)