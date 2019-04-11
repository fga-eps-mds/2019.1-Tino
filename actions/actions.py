from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from typing import Dict, Text, Any, List
from rasa_core_sdk import Action
import requests
import json


class ActionCallapi(Action):
  def name(self) -> Text:
    return 'action_callapi'

  def run(self, dispatcher, tracker, domain):
    request = requests.get('https://11cbadc9.ngrok.io').json() #make an api call
    intercampi_destino = request[0]['Destino'] #extract a joke from returned json response
    intercampi_horario = request[0]['Horário'] #extract a joke from returned json response
    intercampi_origem = request[0]['Origem'] #extract a joke from returned json response
    dispatcher.utter_message('O proximo intercampi vai sair de {} para: {}, com saida no horario: {}'.format(intercampi_origem, intercampi_horario, intercampi_destino)) #send the message back to the user
    return []
