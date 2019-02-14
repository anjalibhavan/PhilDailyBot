import telepot
import lxml
import os
from telegram.ext import Updater, Dispatcher, CommandHandler
import requests
from bs4 import BeautifulSoup
import random
import urllib.request

def get_ald():
    url = "https://www.aldaily.com/random/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'lxml')

    mydiv = soup.find('div',class_='col-xs-12 col-sm-10 col-md-8 col-lg-6')
    links = [] 
    headers = []
    headers.append(mydiv.find('p').find_next_sibling(name='p'))
    links.append(headers[0].find('a').get('href'))   
    return links[0]




    '''

    commands=msg['text']
    if commands=='/start':
        bot.sendMessage()

    elif commands=='/brainpickings':
        final_reply = pickings()
    elif commands=='/aeon':
        final_reply = aeon()
    elif commands=='/ald':
        final_reply = ald()
    return final_reply

    
updater = Updater(bot=mybot)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', my_start))
dispatcher.add_handler(CommandHandler('brainpickings', brain_pickings))
dispatcher.add_handler(CommandHandler('aeon', aeonco))
dispatcher.add_handler(CommandHandler('ald', aldaily))

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return

@app.route('/webhookpath', methods=['GET', 'POST'])
def pass_update():
    webhook.feed(request.data)
    return 'OK'



bot = telepot.Bot(token=YOUR_TOKEN)
webhook = OrderedWebhook(bot, handle)

webhook.run_as_thread()


updater.start_polling()
'''