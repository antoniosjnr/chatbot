from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    parsed_json = str(data, encoding='utf-8')

    return parsed_json['message']['text']