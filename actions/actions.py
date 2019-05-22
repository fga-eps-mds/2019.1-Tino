from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from typing import Text
from rasa_core_sdk import Action
import requests
import json
import os
from datetime import datetime
import pytz
import logging
from pymongo import MongoClient

mongo_host = os.environ['MONGO_ID']
mongo_host = mongo_host + ':27017'
url = os.environ['INTERCAMPI_WEBHOOK']
url_darcy = url + "/darcy"
url_gama = url + "/gama"
url_planaltina = url + "/planaltina"
url_ceilandia = url + "/ceilandia"

logger = logging.getLogger(__name__)


class ActionCallapi(Action):

    def name(self) -> Text:
        return 'action_callapi'

    def run(self, dispatcher, tracker, domain):

        tracker_state = tracker.current_state()
        text = tracker_state['latest_message']['text']
        text = text.lower()
        words = text.split(' ')

        for word in words:
            if('darcy' in word or "plano" in word):
                origin = "Darcy Ribeiro"
                boarding_location = "no Estacionamento do ICC sul"
                break
            if("gama" in word or "fga" in word):
                origin = "Gama-FGA"
                boarding_location = "no Estacionamento do Prédio"
                break
            if("ceilandia" in word or "ceilândia" in word or "fce" in word):
                origin = "Ceilândia-FCE"
                boarding_location = "em frente a portaria central"
                break
            if("planaltina" in word or "fup" in word):
                origin = "Planaltina-FUP"
                boarding_location = "em frente ao antigo Prédio"
                break

        if(origin == ""):
            dispatcher.utter_message('Desculpe, não consegui entender onde' +
                                     'você está... Pode falar de maneira' +
                                     'mais clara?')
            return []

        dispatcher.utter_message('Verificando se há intercampis saindo de ' +
                                 origin + '...')

        # Do request according the 'origin'.
        if(origin == "Darcy Ribeiro"):
            request = requests.get(url_darcy).json()
        if(origin == "Gama-FGA"):
            request = requests.get(url_gama).json()
        if(origin == "Ceilândia-FCE"):
            request = requests.get(url_ceilandia).json()
        if(origin == "Planaltina-FUP"):
            request = requests.get(url_planaltina).json()

        json_result = request

        time_zone = pytz.timezone('America/Sao_Paulo')
        current_time = datetime.now(time_zone)
        intercampi_count = 0

        for y in json_result:
            intercampi_time = y['horario_saida']
            intercampi_time = intercampi_time.split('h')

            if current_time.hour <= int(intercampi_time[0]):
                dispatcher.utter_message('Destino: ' + y['destino'] +
                                         '\n' + "Horário de saída: " +
                                         y['horario_saida'])
                intercampi_count += 1

        if intercampi_count == 0:
            dispatcher.utter_message('Não há mais intercampis saindo hoje :/')
        if(boarding_location != "" and intercampi_count != 0):
            dispatcher.utter_message('O local de embarque é ' + 
                                     boarding_location)

        return []


class ActionCallapiAll(Action):
    def name(self):
        return 'action_callapi_all_intercampi'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Pronto! Aqui está um documento com ' +
                                 'o horário de todos intercampi. Precisa ' +
                                 'de mais alguma coisa?')
        requests.get("https://bfaaaeb3.ngrok.io/?chat_id=487522674")


class ActionFindProfessor(Action):
    def name(self) -> Text:
        return 'action_find_professor'

    def run(self, dispatcher, tracker, domain):

        # Access in 'professor' slot.
        professor = ""
        professor = tracker.current_slot_values()['professor']

        # Connection with 'professor-contato' collection in data bank
        client = MongoClient(mongo_host, username='rasa', password='rasa')
        db = client.admin
        collection = db['professor-contato']
        name = ""
        room = ""
        email = ""
        exist = False
        # Verificando se ha algum registro do professor informado
        for y in collection.find():
            if (professor in y['name']):
                name = y['name']
                room = y['room']
                email = y['email']
                coordination = y['coordination']
                exist = True
                break
        if(exist):
            dispatcher.utter_message('Deixa comigo! ...')
            dispatcher.utter_message('Nome : {}'.format(name))
            dispatcher.utter_message('Sala : {}'.format(room))
            dispatcher.utter_message('E-mail : {}'.format(email))
            if(coordination != "F"):
                dispatcher.utter_message('Coordenação: {}'.format(coordination))    
                            
            return []

        dispatcher.utter_message('Não foi possivel encontrar este ' +
                                 'professor... Verifique se o nome ' +
                                 'está correto e com as iniciais ' +
                                 'maiúsculas!')

        return []
