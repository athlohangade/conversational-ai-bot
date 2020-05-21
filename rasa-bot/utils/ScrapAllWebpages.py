from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import json
import os

class  ScrapAllWebpages:
    @classmethod
    def scrap_all(cls):
        with open('lookup-files/keywords-urls.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    entity = row[0]
                    url = row[1]
                    print(entity, url)

                    if entity == "theft":
                        continue
                    # Open URL and get the source code

                    #Add the webdriver path in Chrome() if not installed globally
                    if os.name == 'posix':
                        driver = webdriver.Chrome("selenium-webdriver/chromedriver_linux64/chromedriver")
                    elif os.name == 'nt':
                        driver = webdriver.Chrome("selenium-webdriver/chromedriver_win32/chromedriver")
                    driver.get(url)
                    res = driver.execute_script("return document.documentElement.outerHTML")
                    driver.quit()
                    soup = BeautifulSoup(res, 'lxml')

                    #Fetching data
                    all_data = {}

                    # Get title of the page
                    title = soup.find('title').text
                    all_data['title'] = title

                    # Get description of the page
                    metadata = soup.find('meta', {'name' : 'description'})
                    description = ""
                    try:
                        description = metadata['content']
                        all_data['description'] = description
                    except:
                        pass

                    # Getting all other data
                    list_of_data = []

                    # div with class "content-text-wrapper"
                    data = soup.find_all('div', {'class': 'content-text-wrapper'})

                    for d in data:
                        each_para = {}
                        try:
                            heading = d.find('h3').text
                        except:
                            heading = ""
                        try:
                            para = []
                            para = d.find('p', {'class': 'description'}).text
                        except:
                            pass
                        if len(para):
                            each_para['heading'] = heading
                            each_para['para'] = [para]
                        if bool(each_para):
                            list_of_data.append(each_para)

                    # div with class "content-text"
                    data = soup.find_all('div', {'class': 'content-text'})

                    for d in data:
                        each_para = {}
                        heading = d.find('h3').text
                        try:
                            para = d.find('p', {'class': 'description'}).text

                            if len(para):
                                each_para['heading'] = heading
                                each_para['para'] = [para]

                        except:
                            para = d.find('p')
                            if para:
                                each_para['heading'] = para.text
                                each_para['para'] = [heading]
                        if bool(each_para):
                            list_of_data.append(each_para)

                    # div with class "text-article"
                    data = soup.find_all('div', {'class': 'text-article'})

                    for d in data:
                        each_para = {}
                        # Get heading if present
                        try:
                            heading = d.find('h2').text
                            each_para['heading'] = heading

                        except:
                            pass
                        # Get para
                        para = d.find_all('p')
                        if para:
                            each_para['para'] = []
                            for p in para:
                                if len(p.text):
                                    each_para['para'].append(p.text)

                            if not bool(each_para['para']):
                                del each_para['para']
                        # Get list if present
                        try:
                            li = d.find_all('li')
                            if li:
                                each_para['list'] = []
                            for l in li:
                                if len(l.text):
                                    each_para['list'].append(l.text)
                        except:
                            pass
                        if bool(each_para):
                            list_of_data.append(each_para)

                    all_data['data'] = list_of_data

                    # the json file where the output must be stored  
                    out_file = open("scrapper/" + entity + ".json", "w")
                    json.dump(all_data, out_file, indent = 2)
                    out_file.close()
                line_count += 1
