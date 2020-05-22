#! /usr/bin/python3

'''
just to test the getSummary function of TextProcessorAndSearch class
not to be included in main project
'''

import json
import sys
from TextProcessorAndSearch import TextProcessorAndSearch as tps

def main():
    '''prints the summary'''
    with open('../scrapper/' + sys.argv[1], 'r') as jsonfile:
        loaded = json.load(jsonfile)
    summary = tps.getSummary(sys.argv[2:], loaded)
    print(summary)
    return 0

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: ./test.py [json-file-name.json] [[keywords]....]')
        sys.exit(1)
    else:
        sys.exit(main())
