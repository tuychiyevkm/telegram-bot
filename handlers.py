from telegram import Update
from telegram.ext import CallbackContext


def handle_start(update:Update, context: CallbackContext):
    update.message.reply_text(
            "Assalomu alaykum! Botimizga xush kelibsiz! "
        )

        
def handle_help(update:Update, context: CallbackContext):
    update.message.reply_text(
        "Qanday yordam kerak?"
    )

def handle_echo(update:Update, context: CallbackContext):
    update.message.reply_text(update.message.text)
