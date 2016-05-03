#from __future__ import unicode_literals
#import os
#from os.path import expanduser, join
#from urllib.request import urlopen

#import youtube_dl
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
#from bs4 import BeautifulSoup

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Welcome!')
    
def change(bot, update):
    f = open("channel.txt", 'r+')
    data = f.readlines()
    bot.sendMessage(update.message.chat_id, text='Current channel: %(data[0]) \nDo you wish to change?(Y/N)')
    if(bot.getUpdates()[-1] == 'Y'):
        bot.sendMessage(update.message.chat_id, text='Type the new channel:')
        old_channel = data[0]
        new_channel = bot.getUpdates()[-1]
        f.write(new_channel)
        bot.sendMessage(update.message.chat_id, text='changed from %(old_channel) to %(new_channel) successfully!')
    f.close()
     
   
def main():
    bot = Updater("168755507:AAHOZALQfHZ7qasSD1W6_Z_vCjqp8D4evbI")
    '''
    if last_command.message.text == '\start':
        bot.sendMessage(last_command.message.chat_id, text="Welcome! :)")
    else:
        updates = [update for update in bot.getUpdates() if update.message.text != '/start' or update.message.text != '/change']
        for update in updates:
            message = update.message.text
            user_id = update.message.message_id
            chat_id = update.message.chat_id
    '''
    dp = bot.dispatcher
    dp.addHandler(CommandHandler("start", start))
    dp.addHandler(CommandHandler("change", change))
    
if __name__ == '__main__':
    main()
    