# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests
import json


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class ActionJoke(Action):
  def name(self):
    return "action_joke"

  def run(sself, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
    request = requests.get('https://v2.jokeapi.dev/joke/Any?lang=pt').json()  # make an api call
    #pergunta = request[0]['setup']  # extract a joke from returned json response
    pergunta = request['setup']
    resposta = request['delivery']
    print(request)
    print(pergunta)
    print(resposta)
    dispatcher.utter_message(text=pergunta)  # send the message back to the user
    dispatcher.utter_message(text=resposta)
    print("\n\n\n")
    print(request)
    return []
