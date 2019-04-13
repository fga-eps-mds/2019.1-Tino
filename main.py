import requests 
import json
from flask import Flask 
from flask import request
from flask import Response
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

# load trained models
interpreter = RasaNLUInterpreter('./models/current/nlu')
agent = Agent.load('./models/current/dialogue', interpreter=interpreter,action_endpoint=EndpointConfig(url="https://b6f78eea.ngrok.io/webhook"))

token = '725793069:AAG70j101Fn6RdcNhmgLv_e--7SVCj83AEY'

# https://api.telegram.org/bot{token}/deleteWebhook

app = Flask(__name__)

# accept telegram messages
@app.route('/',methods=['POST','GET'])
def index():
    if(request.method == 'POST'):
        msg = request.get_json()
        print(msg)
        chat_id , message = parse_msg(msg) #message é a mensagem do usuario, chat_id do user
        
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
