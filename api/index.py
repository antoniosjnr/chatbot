from flask import Flask, request
import json
import nltk
from nltk.chat.util import Chat, reflections

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    data = json.loads(request.json)
    text = data['message']

    rules = {
        'oi': ['Olá!', 'Oi!'],
        'como você está?': ['Estou bem, obrigado!', 'Estou ótimo, e você?'],
        'eu estou bem': ['Que bom ouvir isso!', 'Ótimo!'],
        'o que você pode fazer?': ['Posso responder perguntas sobre nossos produtos e serviços.',
                                   'Posso ajudá-lo com qualquer dúvida que você tiver sobre nossos produtos e serviços.'],
        'adeus': ['Até mais!', 'Tchau!']
    }

    chatbot = Chat(rules, reflections)

    return text