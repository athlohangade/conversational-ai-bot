'''
just to test the getSummary function of TextProcessorAndSearch class
not to be included in main project
'''

import json
from TextProcessorAndSearch import TextProcessorAndSearch as tps

with open('../scrapper/career.json', 'r') as f:
    c = json.load(f)
summary = tps.getSummary(['I', 'want', 'work', 'mastercard'], c)
print(summary)
