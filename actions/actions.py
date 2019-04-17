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

    origem = "Darcy Ribeiro"
    
    
    request = requests.get(url_darcy).json() #make an api call
    json = request
    dispatcher.utter_message('Próximos Intercampis para o campus {}:'.format(origem))
   
    for y in json:
      dispatcher.utter_message('Destino: ...................... {}'.format(y['destino']))
      dispatcher.utter_message('Sai ás: ...................... {}'.format(y['horario_saida']))



    return []
