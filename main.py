from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import ( 
                        handle_start,      handle_help,     handle_echo,    echo_photo, 
                        echo_contact,      echo_video,      echo_sticker,   echo_video_note, 
                        echo_animation,    echo_location,   echo_dice, echo_document, 
                        echo_voice,        echo_audio
                        )
from config import TOKEN

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # command handler
    dispatcher.add_handler(CommandHandler("start", handle_start))
    dispatcher.add_handler(CommandHandler("help", handle_help))

    # message handler
    dispatcher.add_handler(MessageHandler(Filters.text, handle_echo))
    dispatcher.add_handler(MessageHandler(Filters.contact, echo_contact))
    dispatcher.add_handler(MessageHandler(Filters.photo, echo_photo))
    dispatcher.add_handler(MessageHandler(Filters.sticker, echo_sticker))
    dispatcher.add_handler(MessageHandler(Filters.dice, echo_dice))
    dispatcher.add_handler(MessageHandler(Filters.video, echo_video))
    dispatcher.add_handler(MessageHandler(Filters.audio, echo_audio))
    dispatcher.add_handler(MessageHandler(Filters.voice, echo_voice))
    dispatcher.add_handler(MessageHandler(Filters.animation, echo_animation))
    dispatcher.add_handler(MessageHandler(Filters.location, echo_location))
    dispatcher.add_handler(MessageHandler(Filters.video_note, echo_video_note))
    dispatcher.add_handler(MessageHandler(Filters.document, echo_document))


    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()