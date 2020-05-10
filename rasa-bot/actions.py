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
                elif name == "support":
                    message = "To get support, please check out following link:"
                    link = "https://www.mastercard.us/en-us/personal/get-support.html"
                elif name == "find card":
                    message = "To find a card, please check out following link:"
                    link = "https://www.mastercard.us/en-us/personal/find-a-card.html"
                elif name == "ways to pay":
                    message = "To pay, please check out following link:"
                    link = "https://www.mastercard.us/en-us/personal/ways-to-pay.html"
                elif name == "business overview":
                    message = "For business, please check out following link:"
                    link = "https://www.mastercard.us/en-us/business/overview.html"
                elif name == "mastercard contactless":
                    message = "To try mastercard contactless, please check out following link:"
                    link = "https://www.mastercard.us/en-us/business/overview/grow-your-business/improve-checkout/mastercard-contactless.html"
                elif name == "bill payment service":
                    message = "For bill payment services, please check out following link:"
                    link = "https://www.mastercard.us/en-us/business/overview/grow-your-business/improve-checkout/bill-payment-services.html"
                elif name == "business cards":
                    message = "To get a business card, please check out following link:"
                    link = "https://www.mastercard.us/en-us/business/overview/cards.html"
                elif name == "start accepting":
                    message = "For knowing more about accepting, please check out following link:"
                    link = "https://www.mastercard.us/en-us/business/overview/start-accepting.html"
                elif name == "business support":
                    message = "For business support, please check out following link:"
                    link = "https://www.mastercard.us/en-us/business/overview/support.html"
                elif name == "merchant safety and security":
                    message = "For knowing more about safety and security, please check out following link:"
                    link = "https://www.mastercard.us/en-us/business/overview/safety-and-security.html"
                elif name == "grow your business":
                    message = "For growing your business, please check out following link:"
                    link = "https://www.mastercard.us/en-us/business/large-enterprise/grow-your-business.html"
                elif name == "manage employee expenses":
                    message = "For managing employee expenses, please check out following link:"
                    link = "https://www.mastercard.us/en-us/business/large-enterprise/manage-employee-expenses.html"
                elif name == "authentication services":
                    message = "For knowing more about authentication services, please check out following link:"
                    link = "https://www.mastercard.us/en-us/business/large-enterprise/safety-security/authentication-services.html"
                elif name == "manage customer needs":
                    message = "For managing your customer needs, please check out following link:"
                    link = "https://www.mastercard.us/en-us/business/issuers/manage-your-consumer-needs.html"
                elif name == "business payments":
                    message = "For knowing more about business payments, please check out following link:"
                    link = "https://www.mastercard.us/en-us/business/issuers/business-payments.html"
                elif name == "issuer safety and security":
                    message = "For knowing more about business payments, please check out following link:"
                    link = "https://www.mastercard.us/en-us/business/issuers/safety-security.html"
                elif name == "issuer support":
                    message = "To explore our issuer support resources, please check out following link:"
                    link = "https://www.mastercard.us/en-us/business/issuers/get-support.html"
                elif name == "government support":
                    message = "To learn more about how Mastercard supports government, please check out following link:"
                    link = "https://www.mastercard.us/en-us/business/governments/get-support.html"
                elif name == "global locations":
                    message = "For knowing Mastercard global locations, please check out following link:"
                    link = "https://www.mastercard.us/en-us/vision/who-we-are/global-locations.html"
                elif name == "career":
                    message = "To know career opportunities in Mastercard, please check out following link:"
                    link = "https://www.mastercard.us/en-us/vision/who-we-are/careers.html"
                elif name == "click to pay":
                    message = "To know more about Mastercard click to pay, please check out following link:"
                    link = "https://checkout.mastercard.com/clicktopay/en-us.html"
                else:
                    message = "Sorry, didn't get that"
                    link = None

                break

        dispatcher.utter_message(text=message, attachment=link)

        return []