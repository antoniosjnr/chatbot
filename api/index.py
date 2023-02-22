from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook',methods=['POST'])
def webhook():
    return request.json