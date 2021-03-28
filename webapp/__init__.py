from flask import Flask, jsonify, make_response, request
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

@app.route("/")
@app.route("/index")
def index():
    return "Hello World! "+ app.config['SLACK_OAUTH_TOKEN']

@app.route('/echo')
def echo():
    return jsonify(text="Hello")

if __name__ == "__main__":
    app.run()
