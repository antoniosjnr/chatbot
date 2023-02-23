from flask import Flask, request
import json
import nltk
from nltk.chat.util import Chat, reflections
import requests

app = Flask(__name__)

BOT_TOKEN = "6180542426:AAFsMzPGAQShjGwwhqd-MLTXqYzIV44Fh2c"

@app.route('/webhook', methods=['POST'])
def webhook():
    textoMensagem = request.json['message']['text'].lower()
    chatId = request.json['message']['chat']['id']
    rules = getRules()
    chatbot = Chat(rules, reflections)
    resposta = chatbot.respond(textoMensagem)
    urlCompleta = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=html".format(BOT_TOKEN,chatId,resposta)
    requests.post(urlCompleta)

def getRules():
    with open('..\rules.json') as rulesFile:
        return json.load(rulesFile)
