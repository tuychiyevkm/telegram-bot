from telegram import Contact, Update
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


def echo_photo(update:Update, context: CallbackContext):
    photo = update.message.photo[0]
    update.message.reply_photo(photo=photo)


def echo_contact(update:Update, context: CallbackContext):
    contact = update.message.contact
    update.message.reply_contact(contact=contact)
   
def echo_video(update:Update, context:CallbackContext):
    video = update.message.video
    update.message.reply_video(video=video)


def echo_sticker(update:Update, context: CallbackContext):
    sticker = update.message.sticker
    update.message.reply_sticker(sticker=sticker)


def echo_video_note(update: Update, context: CallbackContext):
    video_note = update.message.video_note
    update.message.reply_video_note(video_note=video_note)

def echo_audio(update: Update, context: CallbackContext):
    audio = update.message.audio
    update.message.reply_audio(audio=audio)

def echo_animation(update: Update, context: CallbackContext):
    animation = update.message.animation
    update.message.reply_animation(animation=animation)


def echo_location(update: Update, context: CallbackContext):
    location = update.message.location
    update.message.reply_location(
        latitude=location.latitude,
        longitude=location.longitude
    )


def echo_dice(update: Update, context: CallbackContext):
    dice = update.message.dice
    update.message.reply_dice(emoji=dice.emoji)


def echo_document(update: Update, context: CallbackContext):
    document = update.message.document
    update.message.reply_document(document=document)


def echo_voice(update: Update, context: CallbackContext):
    voice = update.message.voice
    update.message.reply_voice(voice=voice)








