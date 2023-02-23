from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    parsed_json = json.loads(data)

    return parsed_json['message']['text']