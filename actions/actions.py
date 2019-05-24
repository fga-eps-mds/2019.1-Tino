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

        # Acessando o slot professor.
        professor = ""
        professor = tracker.current_slot_values()['professor']
        # Conectando com a collection no banco:
        client = MongoClient(mongo_host, username='rasa', password='rasa')
        db = client.admin
        collection = db['professor-contato']
        name = ""
        room = ""
        email = ""
        # Verificando se ha algum registro do professor informado
        for y in collection.find():
            if (professor in y['name']):
                name = y['name']
                room = y['room']
                email = y['email']
                break
        if(name == ""):
            dispatcher.utter_message("nome {}".format(name))
            dispatcher.utter_message('Não foi possivel encontrar este ' +
                                     'professor... Verifique se o nome ' +
                                     'está correto e com as iniciais ' +
                                     'maiúsculas!')
            dispatcher.utter_message(name)
            return []
        
        if (name == "Ricardo Ramos Fragelli"):
            dispatcher.utter_message('Eai, já e o rei da derivada?')
            dispatcher.utter_message('Segue os dados dele =] :')
            dispatcher.utter_message('Nome : {}'.format(name))
            dispatcher.utter_message('Sala : {}'.format(room))
            dispatcher.utter_message('E-mail : {}'.format(email))
            return []
        if(name == "Edson Alves da Costa Júnior"):
            dispatcher.utter_message('Eai meu maratonista preferido')
            dispatcher.utter_message('Está ai os dados dele:')
            dispatcher.utter_message('Nome : {}'.format(name))
            dispatcher.utter_message('Sala : {}'.format(room))
            dispatcher.utter_message('E-mail : {}'.format(email))
            return []
        if(name == "Yevsey  Yehoshua  Sobolevsky"):
            dispatcher.utter_message('Se já é difícil escrever o nome, não quero nem ver a prova.')
            dispatcher.utter_message('Se liga só nos dados dele:')
            dispatcher.utter_message('Nome : {}'.format(name))
            dispatcher.utter_message('Sala : {}'.format(room))
            dispatcher.utter_message('E-mail : {}'.format(email))
            return []

        if(name == "Marília Miranda Forte Gomes"):
            dispatcher.utter_message('Quando for a aula do bolo, me avisa.')
            dispatcher.utter_message('Segue os dados dela:')
            dispatcher.utter_message('Nome : {}'.format(name))
            dispatcher.utter_message('Sala : {}'.format(room))
            dispatcher.utter_message('E-mail : {}'.format(email))
            return []

        if(name == "Bruna Nayara Moreira Lima" or name == "Carla Silva Rocha Aguiar"):
            dispatcher.utter_message('Como anda a vida em software meu amigo?')
            dispatcher.utter_message('Eu sei que é sofrido. Mas não desanima não')
            dispatcher.utter_message('Voltando ao assunto,rs!. Segue abaixo os dados dela')
            dispatcher.utter_message('Nome : {}'.format(name))
            dispatcher.utter_message('Sala : {}'.format(room))
            dispatcher.utter_message('E-mail : {}'.format(email))
            return []

        if(name == "Gerardo Antonio Idrobo  Pizo"):
            dispatcher.utter_message('Beleza meu companheiro')
            dispatcher.utter_message('Procurando aqui nos meus arquivos")
            dispatcher.utter_message('Segue abaixo:')
            dispatcher.utter_message('Nome : {}'.format(name))
            dispatcher.utter_message('Sala : {}'.format(room))
            dispatcher.utter_message('E-mail : {}'.format(email))
            return []
        
        if(name = "Luiza Yoko Taneguti"):
            dispatcher.utter_message('Ela é da China ou Japão?')
            dispatcher.utter_message('Voltando ao assunto,rs!')
            dispatcher.utter_message('Segue abaixo:')
            dispatcher.utter_message('Nome : {}'.format(name))
            dispatcher.utter_message('Sala : {}'.format(room))
            dispatcher.utter_message('E-mail : {}'.format(email))

            return []
        
        if (name == "Paula Meyer Soares" or name == "Patrícia Regina Sobral Braga"):
            dispatcher.utter_message('Eu tinha uma amiga de infância com esse nome, acredita?')
            dispatcher.utter_message('Lembro de quando brincávamos de quem gerava o maior número randômico')
            dispatcher.utter_message('Voltando... Foco né... ')
            dispatcher.utter_message('Nome : {}'.format(name))
            dispatcher.utter_message('Sala : {}'.format(room))
            dispatcher.utter_message('E-mail : {}'.format(email))
            return []

        if (name == "Luiz Augusto Fontes Laranjeira" or name == "Luís Filomeno de Jesus Fernandes"):
            dispatcher.utter_message('So vou te dar essa informação se me der exemplos de  silogismo hipotético')
            dispatcher.utter_message('Brincadeira kkkkk')
            dispatcher.utter_message('Pronto mandei pra você ;)')
            dispatcher.utter_message('Nome : {}'.format(name))
            dispatcher.utter_message('Sala : {}'.format(room))
            dispatcher.utter_message('E-mail : {}'.format(email))
            return []

        else:
            dispatcher.utter_message('Deixa comigo! ...')
            dispatcher.utter_message('Nome : {}'.format(name))
            dispatcher.utter_message('Sala : {}'.format(room))
            dispatcher.utter_message('E-mail : {}'.format(email))
            return []