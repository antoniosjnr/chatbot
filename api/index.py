from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    data = json.loads(str(request.body, encoding='utf-8'))

    return data['message']['text']