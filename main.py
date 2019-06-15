import requests
from flask import Flask
from flask import request
from flask import Response
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
import os
import pyfiglet

# load trained models

interpreter = RasaNLUInterpreter('./models/current/nlu')
ACTION_WEBHOOK = os.environ['ACTION_WEBHOOK']
ACTION_WEBHOOK = ACTION_WEBHOOK + "/webhook"
TELEGRAM_WEBHOOK = os.environ['TELEGRAM_WEBHOOK']
TELEGRAM_WEBHOOK = str(TELEGRAM_WEBHOOK)
SENDPDF_WEBHOOK = os.environ['SENDPDF_WEBHOOK']
SENDPDF_WEBHOOK = str(SENDPDF_WEBHOOK)


agent = Agent.load('./models/current/dialogue', interpreter=interpreter,
                   action_endpoint=EndpointConfig(url=ACTION_WEBHOOK))

token = os.environ['TELEGRAM_TOKEN']

app = Flask(__name__)

# accept telegram messages
@app.route('/', methods=['POST', 'GET'])
def index():
    if(request.method == 'POST'):
        msg = request.get_json()

        chat_id, message = parse_msg(msg)
        response_messages = applyAi(message)
        if 'todos' in message:
            requests.get(SENDPDF_WEBHOOK+"/?chat_id=" + str(chat_id))

        send_message(chat_id, response_messages)
        return Response('ok', status=200)

    else:
        return '<h1>Tino-Eps</h1>'


# helper function to extract chat id and text
def parse_msg(message):
    try:
        chat_id = message['callback_query']['message']['chat']['id']
        txt = message['callback_query']['data']
    except KeyError:
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
    call_webhook = set_webhook()
    ascii_banner = pyfiglet.figlet_format(call_webhook)
    print(ascii_banner)

    app.run(debug=True, host='0.0.0.0')
