import requests
from flask import Flask
from flask import request
from flask import Response
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from pymongo import MongoClient
import os
import pyfiglet


#load trained models

MONGOHOSTNAME = os.environ.get('MONGO_ID')
MONGOHOSTNAME = str(MONGOHOSTNAME) + ':27017'

interpreter = RasaNLUInterpreter('./models/current/nlu')
ACTION_WEBHOOK = os.environ['ACTION_WEBHOOK']
ACTION_WEBHOOK = ACTION_WEBHOOK + "/webhook"
TELEGRAM_WEBHOOK = os.environ['TELEGRAM_WEBHOOK']
TELEGRAM_WEBHOOK = str(TELEGRAM_WEBHOOK)
SENDPDF_WEBHOOK = os.environ['SENDPDF_WEBHOOK']
SENDPDF_WEBHOOK = str(SENDPDF_WEBHOOK)
ROUTE_TELEGRAM_WEBHOOK = '/'



agent = Agent.load('./models/current/dialogue', interpreter=interpreter,
                   action_endpoint=EndpointConfig(url=ACTION_WEBHOOK))

token = os.environ['TELEGRAM_TOKEN']

app = Flask(__name__)

# accept telegram messages
@app.route(ROUTE_TELEGRAM_WEBHOOK, methods=['POST', 'GET'])
def index():
    if(request.method == 'POST'):
        msg = request.get_json()
        print(ACTION_WEBHOOK)
        if message:
            chat_id, message = parse_msg(msg)
        client = MongoClient(MONGOHOSTNAME, username='rasa',password='rasa')
        db = client.admin
        collection = db['dados-conversa-atual']
        collection.delete_many({})
        chat_data = { 'chat_id': chat_id,'token':token }
        collection.insert_one(chat_data)
        
        response_messages = applyAi(message)



        send_message(chat_id, response_messages)
        return Response('ok', status=200)

    else:
        return '<h1>Tino-Eps</h1>' + ACTION_WEBHOOK


# helper function to extract chat id and text
def parse_msg(message):
    try:
        # Checks if the message has been sended by button
        # (with 'callback_query' attribute)
        chat_id = message['callback_query']['message']['chat']['id']
        txt = message['callback_query']['data']
    except KeyError:
        # Here the message was directly sent by the user
        chat_id = message['message']['chat']['id']
        txt = message['message']['text']
    return chat_id, txt


# helper function to send message
def send_message(chat_id, messages=[]):
    url = 'https://api.telegram.org/bot' + token + '/sendMessage'
    if messages:
        for message in messages:
            payload = {'chat_id': chat_id, 'text': message}
            requests.post(url, json=payload)
    return True


# get response using rasa
def applyAi(message):
    responses = agent.handle_message(message)
    text = []
    if responses:
        for response in responses:
            text.append(response["text"])
    return text


def set_webhook():
    deleteWebhook = requests.get("https://api.telegram.org/bot"
                                 + token + "/deleteWebhook")
    createWebhook = requests.get("https://api.telegram.org/bot"
                                 + token + "/setWebhook?url="+TELEGRAM_WEBHOOK)
    print(deleteWebhook)

    if createWebhook.status_code == 200:
        return "web hook criado com sucesso"
    else:
        "falha ao criar o webhook"


if(__name__ == '__main__'):
    try:
        call_webhook = set_webhook()
    except KeyError:
        print("Ocorreu um erro no Webhook")

    print("Webhook atualizado com sucesso!")
    app.run(debug=True, host='0.0.0.0')
