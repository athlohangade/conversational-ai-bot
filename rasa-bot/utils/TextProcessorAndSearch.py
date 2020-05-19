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
    def __getPlainText(originalData) :
        pass

    ### To be done
    @classmethod
    def getSummary(cls, searchData, originalData) :
        if (type(originalData) == type(dict)) :
            text = cls.__getPlainText(originalData)
        #sentence_list = [ sentence for sentence in ]
        pass

    @classmethod
    def findAnswers(cls, msg, faq) :
        question_list = []
        question_scores = {}

        for f in faq :
            question_list.append(f['Q'].lower())

        for question in question_list :
            for word in msg :
                if word in question :
                    if question in question_scores.keys() :
                        question_scores[question] += 1
                    else :
                        question_scores[question] = 1

        print(question_scores)

        sorted_questions = []
        sorted_scores = []
        answers = []
        for question, score in sorted(question_scores.items(), key=lambda item: item[1]) :
            sorted_questions.append(question)
            sorted_scores.append(score)

        sorted_scores.reverse()
        sorted_questions.reverse()
        print(sorted_questions)
        print(sorted_scores)

        for question in sorted_questions :
            for f in faq :
                if f['Q'].lower() == question :
                    answers.append(f['A'])
                    break

        print(answers)
        return answers
        

# tokens = TextProcessorAndSearch.tokenize(str('I want to grow business').lower())
# tokens = TextProcessorAndSearch.removeStopWords(tokens)
