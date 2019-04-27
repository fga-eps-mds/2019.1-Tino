from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from typing import Dict, Text, Any, List
from rasa_core_sdk import Action
import requests
import json
import os

# url = os.environ['ACTION_WEBHOOK']
# url = str(url) #casting url

class ActionCallapi(Action):
  def name(self) -> Text:
    return 'action_callapi'

  def run(self, dispatcher, tracker, domain):	
    url = os.environ['SENDPDF_WEBHOOK']
    url = str(url) #casting url    
    request = requests.get(url).json() #make an api call
    json = request[0]
    # dispatcher.utter_message('O proximo intercampi vai sair de {} para: {}, com saida no horario: {}'.format(json[0][1], json[0][2], json[0][0])) #send the message back to the user
    dispatcher.utter_message('O proximo intercampi vai para: Darcy ribeiro')
    return []
