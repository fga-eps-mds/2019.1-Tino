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
import telegram

mongo_host = os.environ['MONGO_ID']
mongo_host = mongo_host + ':27017'
url = os.environ['INTERCAMPI_WEBHOOK']
url_darcy = url + "/darcy"
url_gama = url + "/gama"
url_planaltina = url + "/planaltina"
url_ceilandia = url + "/ceilandia"
logger = logging.getLogger(__name__)


class ActionGreet(Action):
    def name(self) -> Text:
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):

        message = ('Fala aí, beleza?\nSou o Tino e estou aqui '
                   'para te ajudar com os seguintes assuntos:\n'
                   ' - Horários dos Intercampi\n' +
                   ' - Informações dos Professores')

        buttons = []

        # Defines the buttons.
        buttons.append(telegram.InlineKeyboardButton(
                text="Horários dos Intercampi",
                callback_data="Quero saber sobre o intercampi"))

        buttons.append(telegram.InlineKeyboardButton(
                text="Informações dos Professores",
                callback_data="Informações dos professores"))

        # Defines the bot from bot_token
        options = [[buttons[0], buttons[1]]]
        client = MongoClient(mongo_host, username='rasa',password='rasa')
        db = client.admin
        collection = db['dados-conversa-atual']
        chat_id = collection.find()[0]['chat_id']
        token = collection.find()[0]['token']
        bot = telegram.Bot(token=token)

        # Defines the options in reply_markup
        reply_markup = telegram.InlineKeyboardMarkup(options)

        

        bot.send_message(chat_id=chat_id,
                         text=message,
                         reply_markup=reply_markup)

        return []


class ActionCallapi(Action):

    def name(self) -> Text:
        return 'action_callapi'

    def run(self, dispatcher, tracker, domain):

        tracker_state = tracker.current_state()
        text = tracker_state['latest_message']['text']
        text = text.lower()
        words = text.split(' ')

        # Searchs the key words in user message to define 'origin'
        for word in words:
            if ('darcy' in word or "plano" in word):
                origin = "Darcy Ribeiro"
                boarding_location = "no Estacionamento do ICC sul"
                break
            if ("gama" in word or "fga" in word):
                origin = "Gama-FGA"
                boarding_location = "no Estacionamento do Prédio"
                break
            if ("ceilandia" in word or "ceilândia" in word or "fce" in word):
                origin = "Ceilândia-FCE"
                boarding_location = "em frente a portaria central"
                break
            if ("planaltina" in word or "fup" in word):
                origin = "Planaltina-FUP"
                boarding_location = "em frente ao antigo Prédio"
                break

        # If don't finds the key word, sends this message to user.
        if (origin == ""):
            dispatcher.utter_message('Desculpe, não consegui entender onde' +
                                     'você está... Pode falar de maneira' +
                                     'mais clara?')
            return []

        dispatcher.utter_message('Verificando se há intercampis saindo de ' +
                                 origin + '...')

        # Do request according the 'origin'.
        if (origin == "Darcy Ribeiro"):
            request = requests.get(url_darcy).json()
        if (origin == "Gama-FGA"):
            request = requests.get(url_gama).json()
        if (origin == "Ceilândia-FCE"):
            request = requests.get(url_ceilandia).json()
        if (origin == "Planaltina-FUP"):
            request = requests.get(url_planaltina).json()

        json_result = request

        # Sets current time according with the time zone.
        time_zone = pytz.timezone('America/Sao_Paulo')
        current_time = datetime.now(time_zone)
        intercampi_count = 0

        for y in json_result:
            intercampi_time = y['horario_saida']
            intercampi_time = intercampi_time.split('h')

            if (current_time.hour <= int(intercampi_time[0])):
                dispatcher.utter_message('Destino: ' + y['destino'] +
                                         '\n' + "Horário de saída: " +
                                         y['horario_saida'])
                intercampi_count += 1

        if (intercampi_count == 0):
            dispatcher.utter_message('Não há mais intercampis saindo hoje :/')
        if (boarding_location != "" and intercampi_count != 0):
            dispatcher.utter_message('O local de embarque é ' +
                                     boarding_location)

        return []


class ActionCallapiAll(Action):
    def name(self):
        return 'action_callapi_all_intercampi'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Pronto! Aqui está um documento com '
                                 'o horário de todos intercampi. Se precisar'
                                 ' de mais alguma coisa, é só falar!')
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

        # Checks if exists register of professor
        for y in collection.find():
            if (professor in y['name']):
                name = y['name']
                room = y['room']
                email = y['email']
                coordination = y['coordination']
                break

        # If does not exist, sends this message to user
        if (name == ""):
            dispatcher.utter_message('Não foi possivel encontrar este ' +
                                     'professor... Verifique se o nome ' +
                                     'está correto e com as iniciais ' +
                                     'maiúsculas')
            dispatcher.utter_message(name)
            return []

        if (name == "Ricardo Ramos Fragelli"):
            dispatcher.utter_message('Eai, já e o rei da derivada?')
            dispatcher.utter_message('Segue os dados dele =] :')

        elif (name == "Edson Alves da Costa Júnior"):
            dispatcher.utter_message('Eai meu maratonista preferido')
            dispatcher.utter_message('Está ai os dados dele:')

        elif (name == "Yevsey Yehoshua Sobolevsky"):
            dispatcher.utter_message('Se já é difícil escrever o nome, não'
                                     ' quero nem ver a prova.')
            dispatcher.utter_message('Se liga só nos dados dele:')

        elif (name == "Marília Miranda Forte Gomes"):
            dispatcher.utter_message('Quando for a aula do bolo, me avisa.')
            dispatcher.utter_message('Segue os dados dela:')

        elif (name == "Bruna Nayara Moreira Lima" or
              name == "Carla Silva Rocha Aguiar"):
            dispatcher.utter_message('Como anda a vida em software meu amigo?')
            dispatcher.utter_message('Eu sei que é sofrido. Mas não desanima')
            dispatcher.utter_message('Voltando ao assunto,rs!. Segue abaixo os'
                                     ' dados dela')

        elif (name == "Gerardo Antonio Idrobo Pizo"):
            dispatcher.utter_message('Beleza meu companheiro')
            dispatcher.utter_message('Procurando aqui nos meus arquivos...')
            dispatcher.utter_message('Segue abaixo:')

        elif (name == "Luiza Yoko Taneguti"):
            dispatcher.utter_message('Ela é da China ou Japão?')
            dispatcher.utter_message('Voltando ao assunto,rs!')
            dispatcher.utter_message('Segue abaixo:')

        elif (name == "Paula Meyer Soares" or
              name == "Patrícia Regina Sobral Braga"):
            dispatcher.utter_message('Eu tinha uma amiga de infância com esse'
                                     ' nome, acredita?')
            dispatcher.utter_message('Lembro de quando brincávamos de quem'
                                     ' gerava o maior número randômico')
            dispatcher.utter_message('Voltando... Foco né...')

        elif (name == "Luiz Augusto Fontes Laranjeira" or
              name == "Luís Filomeno de Jesus Fernandes"):
            dispatcher.utter_message('So vou te dar essa informação se me der'
                                     ' exemplos de silogismo hipotético')
            dispatcher.utter_message('Brincadeira kkkkk')
            dispatcher.utter_message('Pronto mandei pra você ;)')

        elif (name == "Renato Coral Sampaio"):
            dispatcher.utter_message('Opa, desse eu sou fã')
            dispatcher.utter_message('Deixa eu dar uma olhadinha aqui nos meus'
                                     ' arquivos...')
            dispatcher.utter_message('Pronto mandei pra você =)')

        elif (name == "Leandro Xavier Cardoso"):
            dispatcher.utter_message('Um carro a 80km/h e um Leopardo a '
                                     '80km/h, quem vence?')
            dispatcher.utter_message('Brincadeira kkkkk')
            dispatcher.utter_message('Prontinho, aí estão os seus dados!')

        elif (name == "Ronni Geraldo Gomes de Amorim"):
            dispatcher.utter_message('O que será que o Ronni pensa '
                                     'dos terraplanistas?!')
            dispatcher.utter_message('kkkkkkkkk, é cada uma viu... vou '
                                     'procurar aqui nos meus arquivos')
            dispatcher.utter_message('Pronto, encontrei =)')

        elif (name == "Wander Cleber Maria Pereira da Silva"):
            dispatcher.utter_message('Faça felicidade com o Wander, é legal '
                                     'demais! uma dica do seu amiguinho Tino'
                                     ' kkkk')
            dispatcher.utter_message('Pronto, encontrei os dados que você '
                                     'me pediu =)')

        elif (name == "Nilton Correia da Silva"):
            dispatcher.utter_message('Isaac Nilton?!')
            dispatcher.utter_message('Brincadeira kkkkk')
            dispatcher.utter_message('Pronto mandei os dados pra você =)')

        elif (name == "Glauceny Cirne de Medeiros"):
            dispatcher.utter_message('Falo sério, tenho medo de MecSol kkkkk')
            dispatcher.utter_message('Pronto mandei pra você ;)')

        elif (name == "Tatiane da Silva Evangelista"):
            dispatcher.utter_message('Gosto demais! ótima professora!')
            dispatcher.utter_message('Olhando aqui meus arquivos...')
            dispatcher.utter_message('Pronto mandei pra você =)')

        elif (name == "Eneida González Valdés"):
            dispatcher.utter_message('Tem q instalar o catia v5r19')
            dispatcher.utter_message('Brincadeira kkkkk')
            dispatcher.utter_message('Pronto mandei pra você ;)')

        elif (name == "Olexiy Shynkarenko"):
            dispatcher.utter_message('Que nome dificil! kkkkkkkk')
            dispatcher.utter_message('vou olhar aqui nos meus arquivos...')
            dispatcher.utter_message('Pronto mandei pra você =)')

        else:
            dispatcher.utter_message('Deixa comigo! ...')

        dispatcher.utter_message('Nome: {}'.format(name))
        dispatcher.utter_message('E-mail: {}'.format(email))
        dispatcher.utter_message('Sala: {}'.format(room))

        if (coordination != "F"):
            dispatcher.utter_message('Coordenação: {}'.format(coordination))

        dispatcher.utter_message('Como sou legal, vou te ajudar a chegar lá.')
        if (room < "19"):
            dispatcher.utter_message('Tendo como rêferencia a rampa, a '
                                     'sala fica ao lado direito.')
        if (room >= "19"):
            dispatcher.utter_message('Tendo como rêferencia a rampa, a '
                                     'sala fica ao lado esquerdo.')
