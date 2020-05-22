import json
import spacy
import re

from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
from nltk.corpus import stopwords as STOP_WORDS_2
from itertools import combinations, chain
from io import TextIOWrapper

STOP_WORDS_2 = STOP_WORDS_2.words('english')
STOP_WORDS = list(STOP_WORDS)
stop_words = list(set(STOP_WORDS + STOP_WORDS_2))
whWords = list(filter(lambda x: x[0] == 'w' and x[1] == 'h', stop_words))
whWords.append('how')
stop_words = list(filter(lambda x: x not in whWords, stop_words))

class TextProcessorAndSearch:

    nlp = spacy.load('en')
    stopWords = stop_words
    whWords = whWords

    @classmethod
    def tokenize(cls, data):

        tokens = []
        data = data.lower()
        document = cls.nlp(data)
        for token in document:
            tokens.append(token.text)

        return tokens

    @staticmethod
    def removePunctuations(data):

        for token in data:
            if token in punctuation:
                data.remove(token)

        return data

    @classmethod
    def removeStopWords(cls, data):

        data = list(filter(lambda x: x not in cls.stopWords, data))
        return data

    @classmethod
    def __getPlainText(cls, originalData):
        '''parses the json originalData and returns the list of all paragraphs 
        parsed from the json data'''

        originalData = originalData.get("data")
        extracted = []
        if originalData:
            for i in originalData:
                if "para" in i:
                    for para in i["para"]:
                        extracted.append(para)
        return extracted

    @classmethod
    def getSummary(cls, searchData, originalData):
        '''returns most relevant paragrah from the scrapped originalData (json format or
        plain text list) it finds most relevant paragrah by matching with maximum
        possible words in the searchData in the same sequence if not such paragraph
        found then it returns the paragraph with most matching words, ignoring sequence'''

        # make a set of words in searchData so that they can be searched in less
        # than linear time
        if isinstance(searchData, list):
            searchDataList = searchData
            searchData = set(searchData)

        # extract list of p tags from json data
        if isinstance(originalData, dict):
            text = cls.__getPlainText(originalData)
        elif isinstance(originalData, list):
            text = originalData
        elif isinstance(originalData, TextIOWrapper):
            text = cls.__getPlainText(json.load(originalData))

        totalcombinations = TextProcessorAndSearch.make_all_combinations(searchDataList)
        totalcombinations = list(filter(lambda x: len(x) > 1, totalcombinations))

        for wordlist in totalcombinations:
            search = TextProcessorAndSearch.regex_search(wordlist, text)
            try:
                return next(search)
            except StopIteration:
                continue

        return None

    @staticmethod
    def make_all_combinations(keywords):
        '''returns the combinations of all lengths from the given parameter keywords'''
        return sorted(
            list(
                chain.from_iterable(
                    combinations(keywords, i)
                    for i in range(1, len(keywords) + 1)
                )
            ),
            key = len,
            reverse = True
        )

    @staticmethod
    def regex_search(wordlist, target, flags = re.IGNORECASE | re.UNICODE):
        '''finds and yields the paragraphs containing the given words in wordlist
        in the order same in wordlist
        if there are no such paragraphs in the target list, then it yields nothing'''

        # create n compile regular expression to find words in fixed order
        pat = re.compile(
            '.*'.join(
                list(map(r'\b{}\b'.format, wordlist))
            ),
            flags = re.IGNORECASE
        )

        # find the relavant para from the given sequence in wordlist
        # using yield so that if caller wants only first matching paragraph,
        # it should not waste time to find all paragraphs
        # and user can only take first paragraph and leave
        for para in target:
            for line in para.split('\n'):
                if re.search(pat, line):
                    yield para

    @classmethod
    def __getAppropriateQuestions(cls, keywords, question_list):

        question_with_lengths = {}
        result = []

        combi = cls.make_all_combinations(keywords)
        print(combi)
        for individual_combi in combi :
            questions = list(TextProcessorAndSearch.regex_search(individual_combi, question_list))
            if (len(questions) > 0) :
                break

        if (len(questions) == 1) :
            return questions

        smallest_length = min([len(question) for question in questions])
        return = [ result for result in questions if len(result) == smallest_length ]

        # for i in range(len(keywords), 1, -1):
        #     combi = list(combinations(keywords, i))

        #     for individual_combi in combi:

        #         for question in question_list:
        #             temp = question
        #             found = 1

        #             for j in individual_combi:
        #                 if j in temp:
        #                     index = temp.find(j)
        #                     temp = temp[index + len(j):]
        #                 else:
        #                     found = 0
        #                     break

        #             if found:
        #                 question_with_lengths[question] = len(question)

        #     if question_with_lengths:
        #         break

        # if not question_with_lengths:
        #     return result

        # smallest_length = min(question_with_lengths.values())
        # for x, y in question_with_lengths.items():
        #     if y == smallest_length:
        #         result.append(x)

        # if len(result) == 1:
        #     return result
        # else:
        #     question_with_ratio = {}
        #     threshold = 0.4
        #     for question in result:
        #         question_keywords = cls.tokenize(question)
        #         question_keywords = cls.removeStopWords(question_keywords)
        #         ratio = len(keywords) / len(question_keywords)
        #         if ratio >= threshold:
        #             question_with_ratio[ratio] = question

        #     highest_ratio = max(question_with_ratio.keys())
        #     result.append(question_with_ratio[highest_ratio])

        # return result

    @classmethod
    def findAnswers(cls, msg, faq):

        #   get all question in a list
        question_scores = {}
        question_list = [f['Q'].lower() for f in faq]

        questions = cls.__getAppropriateQuestions(msg, question_list)

        answers = []
        for question in questions:
            for f in faq:
                if f['Q'].lower() == question:
                    answers.append(f['A'])
                    break

        return answers

    @classmethod
    def questionOrNot(cls, msg):

        for keyword in msg:
            if keyword in cls.whWords:
                return True
            if keyword == '?':
                return True

        return False
