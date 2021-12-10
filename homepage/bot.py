from django.conf import settings
import requests
from threading import Thread


def send_form(subject, message):
    """
    Sends the data filled in the form to telegram API
    So that the telegram bot sends it to the owner of the site

    Gets the Bot Token and Owner ID from the settings
    Sends it as POST request
    """
    telegram_url = f"https://api.telegram.org" \
                   f"/bot" \
                   f"{settings.BOT_TOKEN}" \
                   f"/sendMessage"

    data = {"chat_id": settings.BOT_REC_ID,
            "text": f"{subject}\n\n{message}"}
    requests.post(url=telegram_url, data=data)


def send_form_threaded(subject, message):
    """
    Sends the request using a thread
    """
    Thread(target=send_form, args=(subject, message)).start()
