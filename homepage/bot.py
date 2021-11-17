from telebot import TeleBot
from django.conf import settings
from threading import Thread

bot = TeleBot(settings.BOT_TOKEN)


def send_form(subject, message):
    bot.send_message(settings.BOT_REC_ID, subject)
    bot.send_message(settings.BOT_REC_ID, message)


def send_form_threaded(subject, message):
    Thread(target=send_form, args=(subject, message)).start()
