from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook')
def webhook():
    return request.json