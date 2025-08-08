from telegram import Update
from telegram.ext import CallbackContext


def start(update:Update, context: CallbackContext):
    update.message.reply_text(
            "Assalomu alaykum! Botimizga xush kelibsiz! "
        )


def help(update:Update, context: CallbackContext):
    update.message.reply_text(
        "Qanday yordam kerak?"
    )
    

def echo(update:Update, context: CallbackContext):
    update.message.reply_text(update.message.text)
