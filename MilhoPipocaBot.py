from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)

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
     
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))
    
def main():
    updater = Updater("168755507:AAHOZALQfHZ7qasSD1W6_Z_vCjqp8D4evbI")
    last_command = bot.getUpdates()[-1]
    updater.start_polling()
    updater.idle()
    if last_command.message.text == '\start':
        bot.sendMessage(last_command.message.chat_id, text="Welcome! :)")
    else:
        updates = [update for update in bot.getUpdates() if update.message.text != '/start' || update.message.text != '/change']
        for update in updates:
            message = update.message.text
            user_id = update.message.message_id
            chat_id = update.message.chat_id
            
    
if __name__ == '__main__':
    main()
    