# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.forms import FormAction
from rasa_sdk.events import UserUtteranceReverted
from utils.RetrieveLocation import RetrieveLocation
from utils.OtherSupport import OtherSupport

import csv

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
        print("In support action")

        report_type = tracker.get_slot('report_type')
        print(report_type)
        if report_type is not None:
            # Report_type is set
            print("report_type is set")
            res = OtherSupport.getResponse([{'entity':'report_type', 'value': report_type}])
        elif OtherSupport.checkValue(entities, "report"):
            print("wrong path")
            dispatcher.utter_message(template="utter_ask_reporttype")
            return [AllSlotsReset()]
        else:
            res = OtherSupport.getResponse(entities)
        
        dispatcher.utter_message(text=res[0], attachment=res[1])

        return [AllSlotsReset()]

class ActionGetATMLocation(Action):

    def name(self) -> Text:
        return "action_get_atm_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]] :

        entities = tracker.latest_message['entities']
        print(entities)

        addresses = []
        toFind = {}
        toFind['location'] = tracker.get_slot('location')
        if toFind['location'] is None :
            message = "Location cannot be None"
            print(message)
            dispatcher.utter_message(text = message)
            return [AllSlotsReset()]

        # toFind['postalCode'] = None
        # entities = tracker.latest_message['entities']
        # for entity in entities :
        #     if entity['entity'] == 'pincode' :
        #         toFind['postalCode'] = entity['value']
        #         break

        locationsData = RetrieveLocation.requestData(toFind['location'])
        if locationsData is None :
            message = "Location not found"
            print(message)
            dispatcher.utter_message(text = message)
            return [AllSlotsReset()]

        locationsData = RetrieveLocation.parseXML(locationsData.text)

        addresses = RetrieveLocation.getAddress(locationsData, toFind)
        if not addresses :
            dispatcher.utter_message(text = "Sorry, I didn't find any atm locations")
        else :
            for number, address in enumerate(addresses, 1) :
                message = str(number) + ") " + ", ".join(address)
                dispatcher.utter_message(text = message)

        return [AllSlotsReset()]

class ActionDefaultAskAffirmation(Action):
    
    def name(self):
        return "action_default_ask_affirmation"

    def __init__(self):
        self.intent_mappings = {}
        # read the mapping from a csv and store it in a dictionary
        with open('intent-fallback.csv') as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                self.intent_mappings[row[0]] = row[1]

    def run(self, dispatcher, tracker, domain):
        # get the most likely intent
        last_intent_name = tracker.latest_message['intent']['name']

        # get the prompt for the intent
        intent_prompt = self.intent_mappings[last_intent_name]

        # Create the affirmation message and add two buttons to it.
        # Use '/<intent_name>' as payload to directly trigger '<intent_name>'
        # when the button is clicked.
        message = "Did you mean '{}'?".format(intent_prompt)
        buttons = [{'title': 'Yes',
               'payload': '/{}'.format(last_intent_name)},
              {'title': 'No',
               'payload': '/out_of_scope'}]
        dispatcher.utter_button_message(message, buttons=buttons)

        return [UserUtteranceReverted()]
    
class ActionDefaultAskRephrase(Action):

    def name(self) -> Text:
        return "action_default_ask_rephrase"

    def run(self, dispatcher: 'Dispatcher', tracker: 'DialogueStateTracker',
        domain: 'Domain'):
        dispatcher.utter_template("utter_ask_rephrase", tracker,
                                        silent_fail=True)

        return [UserUtteranceReverted()]
