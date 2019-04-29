from rasa_core_sdk import Action
from datetime import datetime
import requests
import pytz
import logging

url = "https://02e74b19.ngrok.io"
url_darcy = url + "/darcy"
url_gama = url + "/gama"
url_planaltina = url + "/planaltina"
url_ceilandia = url + "/ceilandia"

logger = logging.getLogger(__name__)


class ActionCallapi(Action):
    def name(self):
        return 'action_callapi'

    def run(self, dispatcher, tracker, domain):
        tracker_state = tracker.current_state()
        text = tracker_state['latest_message']['text']
        text = text.lower()
        words = text.split(' ')

        for word in words:
            if('darcy' in word or "plano" in word):
                origem = "Darcy Ribeiro"
                local_embarque = "no Estacionamento do ICC sul"
                request = requests.get(url_darcy).json()  # api call
                break
            if("gama" in word or "fga" in word):
                origem = "Gama-FGA"
                local_embarque = "no Estacionamento do Prédio "
                request = requests.get(url_gama).json()
                break
            if("ceilandia" in word or "ceilândia" in word or "fce" in word):
                origem = "Ceilândia"
                local_embarque = "em frente a portaria central"
                request = requests.get(url_ceilandia).json()
                break
            if("planaltina" in word or "fup" in word):
                origem = "Planaltina"
                local_embarque = "em frente ao antigo Prédio"
                request = requests.get(url_planaltina).json()
                break

            if(origem == ""):
                dispatcher.utter_message('Desculpe, não consegui entender' +
                                         'onde você está... Pode falar de' +
                                         'maneira mais clara?')
                return []

            dispatcher.utter_message('Verificando se há intercampis saindo' +
                                     'de {}...'.format(origem))

            json = request

            time_zone = pytz.timezone('America/Sao_Paulo')
            hora_atual = datetime.now(time_zone)
            contador_proximos_intercampis = 0

            for y in json:
                hora_intercampi = y['horario_saida']
                hora_intercampi = hora_intercampi.split('h')

                if hora_atual.hour <= int(hora_intercampi[0]):
                    dispatcher.utter_message('Destino: ' + y['destino'] + '\n'
                                             + 'Horário de saída: ' +
                                             y['horario_saida'])
                    contador_proximos_intercampis += 1

            dispatcher.utter_message('O local de embarque é ' +
                                     local_embarque +
                                     '.\nSe tiver mais alguma pergunta,' +
                                     'é so mandar!')

            if contador_proximos_intercampis == 0:
                dispatcher.utter_message('Não há mais intercampis' +
                                         'saindo hoje :/')

            return []


class ActionCallapiAll(Action):
    def name(self):
        return 'action_callapi_all_intercampi'

    def run(self, dispatcher, tracker, domain):

        requests.get("https://bfaaaeb3.ngrok.io/?chat_id=487522674")
