import telepot
import lxml
import os
from telegram.ext import Updater, Dispatcher, CommandHandler
import requests
from bs4 import BeautifulSoup
import random
import urllib.request

def get_aeon():
    url = "https://www.aeon.co/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'lxml')

    mydiv = soup.find_all('article',class_='article-card')
    links = [] 
    headers = []
    for elements in mydiv:
        headers.append(elements.find('div',class_='article-card__inner'))
    for items in headers:
        links.append(items.find('a'))
    for i in range(0,len(links)):
        links[i] = 'https://www.aeon.co'+links[i].get('href')   
        
    return random.choice(links)

    