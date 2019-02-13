import telepot
import lxml
import os
import random
from telegram.ext import Updater, Dispatcher, CommandHandler
import requests
from bs4 import BeautifulSoup
import urllib.request

def get_pickings():
    url = "https://www.brainpickings.org/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'lxml')

    mydiv = soup.find_all('div',class_='post_content')

    links = [] 
    headers = []
    for elements in mydiv:
        headers.append(elements.find('h1',class_='entry-title'))
    for items in headers:
        links.append(items.find('a').get('href'))

    return random.choice(links)
    
