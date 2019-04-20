from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from typing import Dict, Text, Any, List
from rasa_core_sdk import Action
import requests
import json
import os
from datetime import datetime, timezone
import pytz

url = 'https://8a0cb889.ngrok.io'  # url da porta 5002 (ngrok)

class ActionCallapi(Action):
  def name(self) -> Text:
    return 'action_callapi'

  def run(self, dispatcher, tracker, domain):
    url_darcy = url + "/darcy"
    url_gama = url + "/gama"
    url_planaltina = url + "/planaltina" 
    url_ceilandia = url + "/ceilandia" 

    tracker_state = tracker.current_state()
    text = tracker_state['latest_message']['text']
    text = text.lower()
    words = text.split(' ')
    origem = ""
    request = ""
    local_embarque = ""

    for word in words:
      if(word == "darcy" or word == "plano"):
        origem = "Darcy Ribeiro"
        local_embarque = "no Estacionamento do ICC sul"
        request = requests.get(url_darcy).json()  # api call
        break
      if(word == "gama" or word == "fga"):
        origem = "Gama-FGA"
        local_embarque = "no \"Estacionamento\" do Prédio "
        request = requests.get(url_gama).json()
        break
      if(word == "ceilandia" or word == "ceilândia" or word == "fce"):
        origem = "Ceilândia"
        local_embarque = "em frente a portaria central"
        request = requests.get(url_ceilandia).json()
        break 
      if(word == "planaltina" or word == "fup"):
        origem = "Planaltina"
        local_embarque = "em frente ao antigo Prédio"
        request = requests.get(url_planaltina).json()
        break

    if(origem == ""):
      dispatcher.utter_message('Desculpe, não consegui entender onde você está... Pode falar de maneira mais clara?')
      return []

    dispatcher.utter_message('Verificando se há intercampis saindo de {} ...'.format(origem))

    json = request
   
    time_zone = pytz.timezone('America/Sao_Paulo')
    hora_atual = datetime.now(time_zone)
    contador_proximos_intercampis = 0

    for y in json:
      hora_intercampi = y['horario_saida']
      hora_intercampi = hora_intercampi.split('h')

      if hora_atual.hour <= int(hora_intercampi[0]):
        dispatcher.utter_message('Destino: ' + y['destino'] + '\n' + "Horário de saída: " + y['horario_saida'])
        contador_proximos_intercampis += 1

    dispatcher.utter_message('O local de embarque é ' + local_embarque)

    if contador_proximos_intercampis == 0:
      dispatcher.utter_message('Não há mais intercampis saindo hoje :/')


    return []
