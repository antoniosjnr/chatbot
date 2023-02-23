from flask import Flask, request
from nltk.chat.util import Chat, reflections
import requests
import os
import pymongo

app = Flask(__name__)

def getMongoCollection():
    mongoClient = pymongo.MongoClient(os.environ['MONGODB_URI'])
    mongoDatabase = mongoClient[os.environ['DATABASE_NAME']]
    return mongoDatabase[os.environ['RULES_COLLECTION']]

def getRules():
    querySearch = {"token": os.environ['BOT_TOKEN']}
    mongoCol = getMongoCollection()
    rulesMongo = mongoCol.find(querySearch)
    rules = list()
    for x in rulesMongo:
        rules.append([x['pergunta'], x['respostas']])
    return rules

@app.route('/webhook', methods=['POST'])
def webhook():
    pairs = getRules()
    chatbot = Chat(pairs, reflections)
    textoMensagem = request.json['message']['text'].lower()
    chatId = request.json['message']['chat']['id']
    resposta = chatbot.respond(textoMensagem)
    urlCompleta = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=html".format(os.environ['BOT_TOKEN'],chatId,resposta)
    requests.post(urlCompleta)
    return 'ok'

@app.route('/insertRule', methods=['POST'])
def insertRule():
    mongoCol = getMongoCollection()
    mongoCol.insert_one(request.json)
    return 'ok'

@app.route('/testes', methods=['GET'])
def testes():
    return getRules()