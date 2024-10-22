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
        used_entity = None
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
                                message = "Please checkout following link. It might help you."
                                used_entity = e['value']
                                found = True
                                break
                        if found:
                            break
                    line_count += 1

        res = [message, link, used_entity]
        return res

    @classmethod
    def searchInFAQ(cls, msg, flag):
        ''' Load the faq data and find answers for the question asked using that data '''

        # Open and load the faq file
        with open('scrapper/faq.json') as f:
            faq = json.load(f)
        
        # Do required operations like tokenizing and all
        msg = msg.lower()
        msg = TextProcessorAndSearch.tokenize(msg)
        msg = TextProcessorAndSearch.removePunctuations(msg)
        msg = TextProcessorAndSearch.removeStopWords(msg)

        # Get the answer for the question
        answers = TextProcessorAndSearch.findAnswers(msg, faq)
        if not answers and flag == 1:
            answers.append("Sorry, we couldn't find any answer to your question")
            return answers

        return answers

    @staticmethod
    def checkIfSentenceIsQuestion(msg) :
        ''' Check whether the sentence is question '''

        msg = msg.lower()
        msg = TextProcessorAndSearch.tokenize(msg)
        msg = TextProcessorAndSearch.removeStopWords(msg)

        return (TextProcessorAndSearch.questionOrNot(msg))
