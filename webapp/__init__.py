from flask import Flask, jsonify, make_response, request
import json
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


@app.route('/sayhello', methods=['POST'])
def sayhello():
    # make sure the request is a post
    # all slack requests with post wiith a json payload
    if request.method == 'POST':
        payload = json.loads(request.form.get('payload', None))
        token = payload['token']
        # make sure the token sent from slack matches
        if token != app.config['SLACK_VERIFICATION_TOKEN']:
            return jsonify(text="No authorization")

        # do stuff here ---


if __name__ == "__main__":
    app.run()
