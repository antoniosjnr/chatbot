from flask import Flask, request

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    # handle the Telegram message here
    return data