from modules.pickings import *
from modules.aeon import *
from modules.ald import *
import lxml
import os
import random
from telegram.ext import Updater, Dispatcher, CommandHandler
import requests
import telepot
from bs4 import BeautifulSoup
import urllib.request
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

YOUR_TOKEN = 'secret!'
WELCOME = 'Welcome! I am PhilDailyBot, here to give you your dose of philosophy, life, love and everything else in between! Type /brainpickings for an article from Brain Pickings, /aeon for an article from Aeon and /ald for an article from Arts and Letters Daily.'


def brain_pickings(bot,update):
    final_reply = get_pickings()
    bot.send_message(chat_id=update.message.chat_id,text=final_reply)
    

def my_start(bot,update):
    final_reply = WELCOME
    bot.send_message(chat_id=update.message.chat_id,text=final_reply)
    

def aeonco(bot,update):
    final_reply = get_aeon()
    bot.send_message(chat_id=update.message.chat_id,text=final_reply)
    

def aldaily(bot,update):
    final_reply = get_ald()
    bot.send_message(chat_id=update.message.chat_id,text=final_reply)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)
    
    

#mybot = telepot.Bot()

updater = Updater(token=YOUR_TOKEN)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', my_start))
dispatcher.add_handler(CommandHandler('brainpickings', brain_pickings))
dispatcher.add_handler(CommandHandler('aeon', aeonco))
dispatcher.add_handler(CommandHandler('ald', aldaily))
dispatcher.add_error_handler(error)

updater.start_polling()
print('it is happening!')
updater.idle()
print('it is idle!')
