from selenium import webdriver
from bs4 import BeautifulSoup
import json

#Add the path of webdriver on Chrome() if not globally installed
driver = webdriver.Chrome()
driver.get("https://www.mastercard.us/en-us/frequently-asked-questions.html")
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

soup = BeautifulSoup(res, 'lxml')
data = soup.find_all('div', {'class': 'acc-item'})

list_of_ques = []
for d in data:
    item = d.find('span', {'class': 'item-title'})
    #print(item.text)
    q_a = {}
    list_of_ans = []
    que_complete = False
    first_q = True
    faq = d.find_all('p')
    for f in faq:
        que = f.find('strong')
        if que:
            #print("Q " + f.text)
            if first_q:
                prev_q = f.text.replace("\u00ae", "")
                first_q = False
            else: 
                prev_q = curr_q
                que_complete = True
            curr_q = f.text
        else:
            #print("A " + f.text)
            list_of_ans.append(f.text.replace("\u00a0", ""))
        if que_complete:
            list_of_ques.append({"Q": prev_q, "A" : list_of_ans})
            list_of_ans = []
            que_complete = False
    list_of_ques.append({"Q": curr_q, "A" : list_of_ans})
    list_of_ans = []
    que_complete = False

# the json file where the output must be stored  
out_file = open("faq.json", "w")
json.dump(list_of_ques, out_file, indent = 2)
out_file.close()
