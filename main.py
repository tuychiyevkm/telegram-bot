from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import start, help, echo
from config import TOKEN

updater = Updater(TOKEN)
dispatcher = updater.dispatcher

# command handler
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))

# message handler
dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
updater.idle()