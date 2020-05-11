# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
from utils.OtherSupport import OtherSupport
from utils.RetrieveLocation import RetrieveLocation

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionGetSupport(Action):

    def name(self) -> Text:
        return "action_get_support"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity'] == 'support_type':
                name = e['value']
                res = OtherSupport.getResponse(name)
                break

        dispatcher.utter_message(text=res[0], attachment=res[1])

        return []

class ActionGetATMLocation(Action):

    def name(self) -> Text:
        return "action_get_atm_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]] :

        toFind = {}
        toFind['location'] = tracker.get_slot('location')
        toFind['postalCode'] = None

        entities = tracker.latest_message['entities']
        for entity in entities :
            if entity['entity'] == 'pincode' :
                toFind['postalCode'] = entity['value']
                break

        locationsData = RetrieveLocation.requestData()
        locationsData = RetrieveLocation.parseXML(locationsData.text)

        addresses = RetrieveLocation.getAddress(locationsData, toFind)
        if not addresses :
            dispatcher.utter_message(text = "Sorry, I didn't find any atm locations")
        else :
            for number, address in enumerate(addresses, 1) :
                message = str(number) + ") " + ", ".join(address)
                dispatcher.utter_message(text = message)

        return []