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

     url = os.environ['INTERCAMPI_WEBHOOK']
     url = str(url) #casting url
     url_darcy = url + "/darcy"
     url_gama = url + "/gama"
     url_planaltina = url + "/planaltina" 
     url_ceilandia = url + "/ceilandia" 
    
     

     request = requests.get(url_darcy).json() #make an api call
     json = request[0]
     dispatcher.utter_message('Próximos Intercampis em {}: ')
     dispatcher.utter_message('Destino: {} Sai ás: {}'.format(json[0][1], json[0][2], json[0][0])) #send the message back to the user
   
    return []
