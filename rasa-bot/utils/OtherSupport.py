import csv
import json
from utils.TextProcessorAndSearch import TextProcessorAndSearch

class OtherSupport:
    @classmethod
    def checkValue(cls, entities, value):
        for e in entities:
            if e['value'] == value:
                return True
        return False

    @classmethod
    def getResponse(cls, entities):

        link = None
        message = "Sorry, I didn't get that. What can I do for you?"
        found = False

        if entities:
            with open('lookup-files/keywords-urls.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count != 0:
                        for e in entities:
                            if e['value'] == row[0]:
                                link = row[1]
                                message = row[2]
                                used_entity = e['value']
                                found = True
                                break
                        if found:
                            break
                    line_count += 1

        res = [message, link, used_entity]
        return res

    @classmethod
    def searchInFAQ(cls, msg):

        with open('scrapper/faq.json') as f:
            faq = json.load(f)
        
        msg = msg.lower()
        msg = TextProcessorAndSearch.tokenize(msg)
        msg = TextProcessorAndSearch.removePunctuations(msg)
        msg = TextProcessorAndSearch.removeStopWords(msg)
        answers = TextProcessorAndSearch.findAnswers(msg, faq)
        return answers

    @staticmethod
    def checkIfSentenceIsQuestion(msg) :

        msg = msg.lower()
        msg = TextProcessorAndSearch.tokenize(msg)
        msg = TextProcessorAndSearch.removeStopWords(msg)

        return (TextProcessorAndSearch.questionOrNot(msg))