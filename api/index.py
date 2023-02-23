from flask import Flask, request
import json
import nltk
from nltk.chat.util import Chat, reflections
import requests

app = Flask(__name__)

BOT_TOKEN = "6180542426:AAFsMzPGAQShjGwwhqd-MLTXqYzIV44Fh2c"

pairs = [
    ['meu nome é (.*)', ['Olá ! % 1']],
    ['(oi|olá|ola|dai|eai)', ['E ai mano! !', 'Opa!', 'Olá!']],
    ['(.*) seu nome?', ['Meu nome é AntonioTesteBot']],
    ['(.*) o que você faz?', ['Sou apenas um bot para testes!']],
    ['(.*) quem te criou?', ['O Antônio está me ensinando a responder perguntas']]
]

chatbot = Chat(pairs, reflections)

@app.route('/webhook', methods=['POST'])
def webhook():
    textoMensagem = request.json['message']['text'].lower()
    chatId = request.json['message']['chat']['id']
    resposta = chatbot.respond(textoMensagem)
    urlCompleta = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=html".format(BOT_TOKEN,chatId,resposta)
    requests.post(urlCompleta)