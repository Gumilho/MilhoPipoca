from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')
    
def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')
   
def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)
    
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))
    
def main():
    updater = Updater("168755507:AAHOZALQfHZ7qasSD1W6_Z_vCjqp8D4evbI")
    dp = updater.dispatcher
    dp.addHandler(CommandHandler("start", start))
    dp.addHandler(CommandHandler("helo", help))
    dp.addHandler(CommandHandler([Filters.text], echo))
    dp.addErrorHandler(error)
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
    