from bs4 import BeautifulSoup
import requests
import modules.config
import json


def getLinks(url='', identificator=''):
    page_count = config.page_count
    news_count = 0
    links = []

    while page_count <= config.pages_limit:
        url = str(config.page_url) + str(page_count)
        page = requests.get(url)
        if page.status_code == 200:
            soup = BeautifulSoup(page.text, 'html.parser')
            els = soup.find_all(class_=str(identificator))
            for el in els:
                news_count += 1
                ###
                ###
                ###
                link = el.find('a')
                title = link.text
                href = link.get('href')
                full_path = config.site_url + href
                links.append([title, href])
                ###
                ###
                ###
                print(news_count)

            page_count = int(page_count) + 1
        else:
            print('Не удалось получить страницу ' + str(page_count))
    return links


def getContent():
    pass
