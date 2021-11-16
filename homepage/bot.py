from telebot import TeleBot
from django.conf import settings

bot = TeleBot(settings.BOT_TOKEN)


def send_form(subject, message):
    bot.send_message(settings.BOT_REC_ID, subject)
    bot.send_message(settings.BOT_REC_ID, message)
