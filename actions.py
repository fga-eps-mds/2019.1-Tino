from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

from rasa_core_sdk import Action


class ActionCallapi(Action):
  def name(self) -> Text:
    return 'action_callapi'

  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_message('Perai, ainda não consigo chamar nenhuma api, mas eu ainda vou dominar o mundo!!!!')
    dispatcher.utter_message("Call third party api here")
    
