from flask import Flask, request
import json
import nltk
from nltk.chat.util import Chat, reflections
import requests

app = Flask(__name__)

BOT_TOKEN = "6180542426:AAFsMzPGAQShjGwwhqd-MLTXqYzIV44Fh2c"

rules = {
        'oi': ['Olá!', 'Oi!'],
        'como você está?': ['Estou bem, obrigado!', 'Estou ótimo, e você?'],
        'eu estou bem': ['Que bom ouvir isso!', 'Ótimo!'],
        'o que você pode fazer?': ['Posso responder perguntas sobre nossos produtos e serviços.',
                                   'Posso ajudá-lo com qualquer dúvida que você tiver sobre nossos produtos e serviços.'],
        'adeus': ['Até mais!', 'Tchau!']
    }
chatbot = Chat(rules, reflections)

@app.route('/webhook', methods=['POST'])
def webhook():
    textoMensagem = request.json['message']['text'].lower()
    chatId = request.json['message']['chat']['id']
    resposta = chatbot.respond(textoMensagem)
    urlCompleta = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=html".format(BOT_TOKEN,chatId,resposta)
    requests.post(urlCompleta)