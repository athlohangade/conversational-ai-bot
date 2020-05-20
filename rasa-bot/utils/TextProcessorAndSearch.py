import json
import spacy

from string import punctuation
import re
from spacy.lang.en.stop_words import STOP_WORDS
from nltk.corpus import stopwords as STOP_WORDS_2
from itertools import combinations

# print(STOP_WORDS)
# print('I' in STOP_WORDS)
# print(STOP_WORDS_2.words('english'))
STOP_WORDS_2 = STOP_WORDS_2.words('english')
STOP_WORDS = list(STOP_WORDS)
stop_words = list(set(STOP_WORDS + STOP_WORDS_2))
whWords = list(filter(lambda x: x[0] == 'w' and x[1] == 'h', stop_words))
whWords.append('how')
stop_words = list(filter(lambda x: x not in whWords, stop_words))

class TextProcessorAndSearch :

    nlp = spacy.load('en')
    stopWords = stop_words
    whWords = whWords
    # print(stopWords)

    @classmethod
    def tokenize(cls, data) :

        tokens = []
        data = data.lower()
        document = cls.nlp(data)
        for token in document :
            tokens.append(token.text)

        print(tokens)
        return tokens

    @staticmethod
    def removePunctuations(data) :

        for token in data :
            if token in punctuation :
                data.remove(token)

        return data

    @classmethod
    def removeStopWords(cls, data) :

        data = list(filter(lambda x: x not in cls.stopWords, data))
        print(data)
        return data

    ### To be done
    @classmethod
    def __getPlainText(cls, originalData) :
        originalData = originalData.get("data")
        extracted = []
        if originalData:
            for i in originalData:
                for para in i["para"]:
                    extracted.append(para)
        return extracted

    ### To be done
    @classmethod
    def getSummary(cls, searchData, originalData) :
        # make a set of words in searchData so that they can be searched in less
        # than linear time 
        if type(searchData) == list:
            searchDataList = searchData
            searchData = set(searchData)

        # extract list of p tags from json data
        if type(originalData) == dict:
            text = cls.__getPlainText(originalData)
        elif type(originalData) == list:
            text = originalData
        
        search = TextProcessorAndSearch.regex_search(searchDataList, text)
        if search:
            return search
        
        totalWords = len(searchDataList)
        combinations = [searchDataList[i: i + j] for i in range(0, len(searchDataList)) for j in range(1, len(searchDataList) - i + 1) if j - i != totalWords]
        combinations = sorted(combinations, key = len, reverse = True)

        for wordlist in combinations:
            search = TextProcessorAndSearch.regex_search(wordlist, text)
            if search:
                return search

        return None

    @staticmethod
    def regex_search(wordlist, target, flags = re.IGNORECASE | re.UNICODE):
        '''finds and returns the paragraph containing the given words in wordlist
        in the order same in wordlist
        if there is no such paragraph in the target list, then it returns None'''

        # create n compile regular expression to find words in fixed order
        pat = '.*'.join(word for word in wordlist)
        pat = re.compile(pat, flags = flags)
        
        # find the relavant para from the given sequence in wordlist
        for para in target:
            for line in para.split('\n'):
                if re.search(pat, line):
                    return para

        return None
                    
    @classmethod
    def __getAppropriateQuestions(cls, keywords, question_list) :

        question_with_lengths = {}
        result = []
        for i in range(len(keywords), 1, -1) :
            combi = list(combinations(keywords, i))

            for individual_combi in combi :

                for question in question_list :
                    temp = question
                    found = 1

                    for j in individual_combi :
                        if j in temp :
                            index = temp.find(j)
                            temp = temp[index + len(j):]
                        else :
                            found = 0
                            break

                    if found :
                        question_with_lengths[question] = len(question)

            if question_with_lengths :
                break

        if not question_with_lengths :
            return result

        smallest_length = min(question_with_lengths.values())
        for x, y in question_with_lengths.items() :
            if y == smallest_length :
                result.append(x)

        if len(result) == 1 :
            return result
        else :
            question_with_ratio = {}
            threshold = 0.4
            for question in result :
                question_keywords = cls.tokenize(question)
                question_keywords = cls.removeStopWords(question_keywords)
                ratio = len(keywords) / len(question_keywords)
                if ratio >= threshold :
                    question_with_ratio[ratio] = question

            highest_ratio = max(question_with_ratio.keys())
            result.append(question_with_ratio[highest_ratio])

        return result

    @classmethod
    def findAnswers(cls, msg, faq) :

        #   get all question in a list
        question_scores = {}
        question_list = [f['Q'].lower() for f in faq]
        
        questions = cls.__getAppropriateQuestions(msg, question_list)

        answers = []
        for question in questions :
            for f in faq :
                if f['Q'].lower() == question :
                    answers.append(f['A'])
                    break

        print(questions)
        print(answers)
        return answers

    @classmethod
    def questionOrNot(cls, msg) :

        for keyword in msg :
            if keyword in cls.whWords :
                return True
            if keyword == '?' :
                return True

        return False
        

# tokens = TextProcessorAndSearch.tokenize(str('What if contactless card is lost'))
# # print(tokens)
# tokens = TextProcessorAndSearch.removePunctuations(tokens)
# # print(tokens)
# tokens = TextProcessorAndSearch.removeStopWords(tokens)
# # print(tokens)

# with open('../scrapper/faq.json') as f:
#     faq = json.load(f)

# TextProcessorAndSearch.findAnswers(tokens, faq)