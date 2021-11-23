from django.conf import settings
import requests
from threading import Thread


def send_form(subject, message):
    telegram_url = f"https://api.telegram.org" \
                   f"/bot" \
                   f"{settings.BOT_TOKEN}" \
                   f"/sendMessage"

    data = {"chat_id": settings.BOT_REC_ID,
            "text": f"{subject}\n\n{message}"}
    requests.post(url=telegram_url, data=data)


def send_form_threaded(subject, message):
    Thread(target=send_form, args=(subject, message)).start()
