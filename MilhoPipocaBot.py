from __future__ import unicode_literals
import os
from os.path import expanduser, join
from urllib.request import urlopen

import youtube_dl
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
from bs4 import BeautifulSoup
import json
    
def get_title(channel):
    f = open(channel+".txt")
    data = f.readlines()[0]
    f.close()
    return data
    
def check_title(title):
    return get_title() == title
    
def get_url(channel):
    url = "https://www.youtube.com/user/{}/videos".format(channel)
    content = urlopen(url).read()
    soup = BeautifulSoup(content, "lxml")
    tag = soup.find('a', {'class': 'yt-uix-sessionlink yt-uix-tile-link  spf-link  yt-ui-ellipsis yt-ui-ellipsis-2'})
    title = tag.get('title')
    url = "https://www.youtube.com" + tag.get('href')
    #print(title + url)
    return title, url
    
def song_down(url, title):
    ydl_opts = {
        'outtmpl': '{}.%(ext)s'.format(title),
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Welcome!')
    
def new(bot,update):
    author = get_channel()
    title, url = get_url()
    if check_title(title): 
        bot.sendMessage(update.message.chat_id, text='No new videos :(')
        return
    bot.sendMessage(update.message.chat_id, text=url)
    song_down(url,title)
    bot.sendAudio(update.message.chat_id, audio=open('{}.mp3'.format(title), 'rb'), title=title)
    change_title(bot,update,title)
    os.remove('{}.mp3'.format(title))
    
def channel(bot,update):
    bot.sendMessage(update.message.chat_id, text='Current channel: {}'.format(get_channel))
    
def change_title(bot, update, args):
    channel = get_channel()
    old_title = get_title()
    new_title = "{}\n".format(channel) + old_title.replace(old_title, args)
    f = open("database.txt", 'w')
    f.write(new_title)
    f.close()
    bot.sendMessage(update.message.chat_id, text='changed from {} to {} successfully!'.format(old_title, args))
    
'''
def change_channel(bot, update, args):
    old_channel = get_channel()
    title = get_title()
    new_channel = old_channel.replace(old_channel, args[0]) + '\n{}'.format(title)
    f = open("database.txt", 'w')
    f.write(new_channel)
    f.close()
    bot.sendMessage(update.message.chat_id, text='changed from {} to {} successfully!'.format(old_channel, args))
'''
def add_channel(bot, update, args):
    if os.path.exists(args[0] + ".txt"):
        bot.sendMessage(update.message.chat_id, text='Channel already added!')
        return
    f = open("{}.txt".format(args[0]), 'w')
    title, url = get_url(args[0])
    f.write(title)
    f.close()
    bot.sendMessage(update.message.chat_id, text='Added {} successfully!'.format(args[0]))
   
def main():
    updater = Updater("168755507:AAHOZALQfHZ7qasSD1W6_Z_vCjqp8D4evbI")
    dp = updater.dispatcher
    dp.addHandler(CommandHandler("start", start))
    dp.addHandler(CommandHandler("new",new))
    dp.addHandler(CommandHandler("channel", channel))
    dp.addHandler(CommandHandler("add_channel", add_channel, pass_args=True))
    #dp.addHandler(CommandHandler("change_channel", change, pass_args=True))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
    #change_title('TehIshter')
    