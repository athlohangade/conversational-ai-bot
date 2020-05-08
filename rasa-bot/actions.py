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

                if name == "financial education":
                    message = "For financial support, please check out following link:"
                    link = "https://www.mastercard.us/en-us/personal/get-support/financial-education.html"
                elif name == "convert currency":
                    message = "For converting currency, please check out following link:"
                    link = "https://www.mastercard.us/en-us/personal/get-support/convert-currency.html"
                elif name == "reload a prepaid card":
                    message = "For reloading a prepaid card, please check out following link:"
                    link = "https://www.mastercard.us/en-us/personal/get-support/reload-a-prepaid-card.html"
                elif name == "pay tax":
                    message = "For paying tax, please check out following link:"
                    link = "https://www.mastercard.us/en-us/personal/get-support/pay-taxes.html"
                elif name == "report problem shopping":
                    message = "For reporting problem, please check out following link:"
                    link = "https://www.mastercard.us/en-us/personal/get-support/report-problem-shopping.html"
                elif name == "cash back store locator":
                    message = "To get access to your cash at checkout, please check out following link:"
                    link = "https://www.mastercard.us/en-us/personal/get-support/cash-back-store-locator.html"
                else:
                    message = "Sorry, didn't get that"
                    link = None

                break

        dispatcher.utter_message(text=message, attachment=link)

        return []