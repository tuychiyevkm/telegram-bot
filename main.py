from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import handle_start, handle_help, handle_echo
from config import TOKEN

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # command handler
    dispatcher.add_handler(CommandHandler("start", handle_start))
    dispatcher.add_handler(CommandHandler("help", handle_help))

    # message handler
    dispatcher.add_handler(MessageHandler(Filters.text, handle_echo))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()