import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from nltk.corpus import stopwords as STOP_WORDS_2

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
    print(stopWords)

    @classmethod
    def tokenize(cls, data) :

        tokens = []
        document = cls.nlp(data)
        for token in document :
            tokens.append(token.text)

        print(tokens)
        return tokens

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
                extracted.append(i["para"])
        return extracted

    ### To be done
    @classmethod
    def getSummary(cls, searchData, originalData) :
        # make a set of words in searchData so that they can be searched in less
        # than linear time 
        if type(searchData) == list:
            searchData = set(searchData)

        # extract list of p tags from json data
        if type(originalData) == dict:
            text = cls.__getPlainText(originalData)
        elif type(originalData) == list:
            text = originalData
    
        # find number of occurences of words in searchData in each Description
        c = mx = 0 
        currentBest = None
        for ldes in text:
            for des in ldes: 
                for word in des.split():
                    if word in searchData:
                        c += 1
                if c >= mx:
                    mx = c
                    currentBest = des

        return currentBest
                    
    @classmethod
    def findAnswers(cls, msg, faq) :

        #   get all question in a list
        question_scores = {}
        question_list = [f['Q'].lower() for f in faq]

        #   Calculate score for each question based on keywords presence
        for question in question_list :
            for word in msg :
                if word in question :
                    question_scores[question] += question_scores.get(question, 0)

        print(question_scores)

        #   Sort the questions and answers in descending order 
        sorted_questions = []
        sorted_scores = []
        answers = []
        for question, score in sorted(question_scores.items(), key=lambda item: item[1], reverse = True) :
            sorted_questions.append(question)
            sorted_scores.append(score)

        print(sorted_questions)
        print(sorted_scores)

        #   get the answers
        for question in sorted_questions :
            for f in faq :
                if f['Q'].lower() == question :
                    answers.append(f['A'])
                    break

        print(answers)
        return answers
        

# tokens = TextProcessorAndSearch.tokenize(str('I want to grow business').lower())
# tokens = TextProcessorAndSearch.removeStopWords(tokens)