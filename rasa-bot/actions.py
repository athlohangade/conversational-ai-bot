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
from rasa_sdk.events import FollowupAction
from utils.RetrieveLocation import RetrieveLocation
from utils.OtherSupport import OtherSupport
from utils.TextProcessorAndSearch import TextProcessorAndSearch
from utils.ThreadToScrap import ThreadToScrap
from MastercardConfig import MastercardConfig

import csv
import json
from datetime import datetime, timedelta
import _thread
import time

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
    
    now = datetime.now()
    #prev_time = now - timedelta(days=1)
    prev_time = now

    def name(self) -> Text:
        return "action_get_support"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)
        print("In support action")

        ## For Periodic Scrapping
        current_time = datetime.now()
        print(current_time)
        if (current_time > (ActionGetSupport.prev_time + timedelta(hours=MastercardConfig.hours))):
            ActionGetSupport.prev_time = current_time
            print("In thread create")
            try:
                # Create new threads
                thread1 = ThreadToScrap(1, "Thread-1")

                # Start new Threads
                thread1.start()
            except:
                print("Thread not created")

        # For handling the FAQ part (if intent is classified with above
        # threshold confidence but question is asked)
        msg = tracker.latest_message.get('text')
        if (OtherSupport.checkIfSentenceIsQuestion(msg)) :
            answers = OtherSupport.searchInFAQ(msg)
            answers = answers[0]
            for answer in answers :
                dispatcher.utter_message(text = answer) 
            return [AllSlotsReset()]

        to_reset = False

        report_type = tracker.get_slot('report_type')
        card_type = tracker.get_slot('card_type')
        print(report_type, card_type)

        if report_type:
            # Report_type is set
            entities = [{'entity':'report_type', 'value': report_type}]
            to_reset = True
        elif OtherSupport.checkValue(entities, "report"):
            print("wrong path")
            dispatcher.utter_message(template="utter_ask_reporttype")
            return [FollowupAction('action_listen')]

        elif card_type:
            # Card_type is set
            entities = [{'entity':'card_type', 'value': card_type}]
            to_reset = True
        elif OtherSupport.checkValue(entities, "cards"):
            print("wrong path card")
            dispatcher.utter_message(template="utter_ask_cardtype")
            return [FollowupAction('action_listen')]
            
        res = OtherSupport.getResponse(entities)

        # adding the relevant paragraph from json file

        msglist = TextProcessorAndSearch.removeStopWords(TextProcessorAndSearch.removePunctuations(TextProcessorAndSearch.tokenize(msg)))
        with open('scrapper/' + res[2] + '.json', 'r') as data:
            additional_para = TextProcessorAndSearch.getSummary(msglist, json.load(data))
        if additional_para:
            res[0] += '\n'
            res[0] += additional_para
        
        dispatcher.utter_message(text=res[0], attachment=res[1])

        if to_reset:
            return [AllSlotsReset(),FollowupAction('action_listen')]

        return [FollowupAction('action_listen')]

class ActionGetATMLocation(Action):

    def name(self) -> Text:
        return "action_get_atm_location"

    def __setLocationValue(self, tracker) :

        location = None
        entities = tracker.latest_message['entities']
        print(entities)

        # get the location value from entities
        for element in entities :
            if element['entity'] == 'location' or element['entity'] == 'GPE' :
                location = element['value']
                return location

        # get the location value from slots if not present in entity
        location = tracker.get_slot('location')
        if location is None : 
            location = tracker.get_slot('GPE') 
            print(location)

        return location

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]] :

        addresses = []
        location = None

        print(tracker.get_slot('location'))
        print(tracker.get_slot('GPE'))

        # set the location variable to the values extracted from
        # respective entity
        location = self.__setLocationValue(tracker)
        if location is None :
            message = "Location cannot be None"
            print(message)
            dispatcher.utter_message(text = message)
            return [AllSlotsReset()]

        # Request the ATM data given the location
        locationsData = RetrieveLocation.requestData(location)
        if locationsData is None :
            message = "Location not found"
            print(message)
            dispatcher.utter_message(text = message)
            return [AllSlotsReset()]

        # Parse the requested atm data and get addresses of locations
        locationsData = RetrieveLocation.parseXML(locationsData.text)
        addresses = RetrieveLocation.getAddress(locationsData)

        # If no location is found, else output the address data
        if not addresses :
            dispatcher.utter_message(text = "Sorry, I didn't find any atm locations")
        else :
            for number, address in enumerate(addresses, 1) :
                message = str(number) + ") " + ", ".join(address)
                dispatcher.utter_message(text = message)

        # Reset the slot for location and GPE entity
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

        entities = tracker.latest_message['entities']
        print(entities)
        print("In fallback function")

        # For handling the FAQ part (if intent is classified with below 
        # threshold confidence but question is asked)
        msg = tracker.latest_message.get('text')
        if (OtherSupport.checkIfSentenceIsQuestion(msg)) :
            answers = OtherSupport.searchInFAQ(msg)
            print('adadfa')
            answers = answers[0]
            for answer in answers :
                dispatcher.utter_message(text = answer) 
            return [AllSlotsReset()]

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
