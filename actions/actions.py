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
    url = "https://5fe66413.ngrok.io"
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

    for word in words:
      if(word == "darcy"):
        origem = "Darcy Ribeiro"
        request = requests.get(url_darcy).json() #api call
        break
      if(word == "gama"):
        origem = "Gama-FGA"
        request = requests.get(url_gama).json()
        break
      if(word == "ceilandia"):
        origem = "Ceilândia"
        request = requests.get(url_ceilandia).json()
        break
      if(word == "ceilândia"):
        origem = "Ceilândia"
        request = requests.get(url_ceilandia).json()
        break        
      if(word == "planaltina"):
        origem = "Planaltina"
        request = requests.get(url_planaltina).json()
        break
      if(word == "fup"):
        origem = "Planaltina"
        request = requests.get(url_planaltina).json()
        break        
      if(word == "fce"):
        origem = "Ceilândia"
        request = requests.get(url_ceilandia).json()
        break
      if(word == "fga"):
        origem = "Gama-FGA"
        request = requests.get(url_gama).json()
        break

    if(origem == ""):
      dispatcher.utter_message('Opção invalida')
      return []


    json = request
    dispatcher.utter_message('Próximos Intercampis saindo de {}:'.format(origem))
   
    for y in json:
      
      dispatcher.utter_message('Destino: ...................... {}'.format(y['destino']))
      dispatcher.utter_message('Sai ás: ...................... {}'.format(y['horario_saida']))
      dispatcher.utter_message('__________________________________')



    return []
