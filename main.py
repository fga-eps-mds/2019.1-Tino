import requests 
import json
from flask import Flask 
from flask import request
from flask import Response
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
import os

# load trained models


interpreter = RasaNLUInterpreter('./models/current/nlu')
ACTION_WEBHOOK = os.environ['ACTION_WEBHOOK']
ACTION_WEBHOOK = ACTION_WEBHOOK + "/webhook"
print(ACTION_WEBHOOK)
agent = Agent.load('./models/current/dialogue', interpreter=interpreter,action_endpoint=EndpointConfig(url=ACTION_WEBHOOK))

token = os.environ['TELEGRAM_TOKEN']

# https://api.telegram.org/bot{token}/deleteWebhook

app = Flask(__name__)

# accept telegram messages
@app.route('/',methods=['POST','GET'])
def index():
    if(request.method == 'POST'):
        msg = request.get_json()
        print('mensagem:', msg)
        chat_id , message = parse_msg(msg) #message é a mensagem do usuario, chat_id do user
        print('message: {}'.format (message))
        response_messages = applyAi(message)
        send_message(chat_id,response_messages)
        return Response('ok',status=200)
    
    else:
        return '<h1>HELLO</h1>'

# helper function to extract chat id and text
def parse_msg(message):
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    return chat_id,txt

# helper function to send message 
def send_message(chat_id,messages=[]):
    print(token)
    print(ACTION_WEBHOOK)
    url = 'https://api.telegram.org/bot'+token+'/sendMessage' 
    if messages:
        for message in messages:
            payload = {'chat_id' : chat_id,'text' : message}
            requests.post(url,json=payload)
    return True

# get response using rasa
def applyAi(message):
    responses = agent.handle_message(message)
    text = []
    if responses:
        for response in responses:
            text.append(response["text"])
    return text


if(__name__ ==  '__main__'):
    app.run(debug=True, host='0.0.0.0')
