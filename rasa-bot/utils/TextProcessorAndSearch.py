import json
import re
import spacy

from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
#from nltk.corpus import stopwords as STOP_WORDS_2
from itertools import combinations, chain
from io import TextIOWrapper
from math import floor
from utils.HTMLParsed import HTMLParsed

# Create a list of stop words such that wh-words are not considered
# to be the stopwords
#STOP_WORDS_2 = STOP_WORDS_2.words('english')
STOP_WORDS = list(STOP_WORDS)
STOP_WORDS_2 = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
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
        ''' Get word tokens from sentence '''

        tokens = []
        data = data.lower()
        document = cls.nlp(data)
        for token in document:
            tokens.append(token.text)

        return tokens

    @staticmethod
    def removePunctuations(data):
        ''' Remove punctuations '''

        for token in data:
            if token in punctuation:
                data.remove(token)

        return data

    @classmethod
    def removeStopWords(cls, data):
        ''' Remove unnecessary words (Eg : helping verbs) '''

        data = list(filter(lambda x: x not in cls.stopWords, data))
        return data

    @classmethod
    def __getPlainText(cls, originalData):
        '''parses the json originalData and returns the list of all paragraphs 
        parsed from the json data'''

        originalData = originalData.get("data")
        extracted = HTMLParsed()
        if originalData:
            for i in originalData:
                if "para" in i:
                    heading = i.get("heading")
                    extracted.addParsed(i["para"], heading)
        return extracted

    @classmethod
    def getSummary(cls, searchData, originalData):
        '''returns most relevant paragrah from the scrapped originalData (json format or
        plain text list) it finds most relevant paragrah by matching with maximum
        possible words in the searchData in the same sequence if not such paragraph
        found then it returns None'''
        
        # make a set of words in searchData so that they can be searched in less
        # than linear time
        if isinstance(searchData, list):
            searchDataList = searchData
            searchData = set(searchData)

        # extract list of p tags from json data
        if isinstance(originalData, dict):
            text = cls.__getPlainText(originalData)
        elif isinstance(originalData, list):
            text = HTMLParsed(originalData)
        elif isinstance(originalData, TextIOWrapper):
            text = cls.__getPlainText(json.load(originalData))

        totalcombinations = TextProcessorAndSearch.make_all_combinations(searchDataList, threshold = 0.3)
        l = floor(len(searchDataList) / 2)
        combinationsforheading = list(filter(lambda x: len(x) > l, totalcombinations))

        for wordlist in combinationsforheading:
            search = list(TextProcessorAndSearch.regex_search(wordlist, text.getheadings()))
            if search:
                return '\n'.join(text.getParagraphForheading(min(search, key = min)))

        for wordlist in totalcombinations:
            search = TextProcessorAndSearch.regex_search(wordlist, text.getparagraphs())
            try:
                return next(search)
            except StopIteration:
                continue

        return None

    @staticmethod
    def make_all_combinations(keywords, threshold = 0, lower_bound = 2):
        '''returns the combinations of all lengths from the given parameter keywords
        if threshold value is provided, then it returns all combinations with number of
        words greater than or equal to the (threshold value * length of keywords)'''

        return sorted(
            list(
                chain.from_iterable(
                    combinations(keywords, i)
                    for i in range(
                        max(
                            lower_bound,
                            floor(len(keywords) * threshold)
                        ), 
                        len(keywords) + 1)
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
                map(
                    r'\b{}e?s?\b'.format,
                    map(
                        lambda word:
                            word[:-2] if word.endswith('es')
                            else word[:-1] if word.endswith('s')
                            else word,
                        wordlist
                    )
                )
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
        '''Do various combinations of the keywords, do searching and return
        appropriate matched question. If more than one questions are extracted
        then return the question with the smallest length'''

        # question_with_lengths = {}
        result = []
        questions = []

        # Do combinations with given threshold and lower_bound
        combi = cls.make_all_combinations(keywords, 0.3, 3)
        print(combi)

        # Search the individual combination
        for individual_combi in combi :
            questions = list(TextProcessorAndSearch.regex_search(individual_combi, question_list))
            if (len(questions) > 0) :
                break

        # If no question or only one question is extracted return it
        if (len(questions) <= 1) :
            return questions

        # If more than one, return the question with smallest length
        smallest_length = min([len(question) for question in questions])
        return [ result for result in questions if len(result) == smallest_length ]

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
        '''return the appropriate answers given the query and dict of 
        possible faqs. Most of the time only one question is extracted
        but there might be case that more than one question in extracted'''

        #   get all question in a list
        question_scores = {}
        question_list = [f['Q'].lower() for f in faq]

        questions = set(cls.__getAppropriateQuestions(msg, question_list))

        # Find answers to the extracted questions and return
        answers = []
        for question in questions:
            for f in faq:
                if f['Q'].lower() == question:
                    answers.append(f['A'])
                    break

        answers = list(chain(*answers))
        print(answers)
        return answers

    @classmethod
    def questionOrNot(cls, msg):
        '''returns whether the sentence is question by checking
        whether sentence contains wh-type word or "?"'''

        for keyword in msg:
            if keyword in cls.whWords:
                return True
            if keyword == '?':
                return True

        return False
