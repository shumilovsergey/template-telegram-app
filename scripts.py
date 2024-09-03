import requests
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN_TG = os.getenv("TOKEN_TG")
HOST_DNS = os.getenv("HOST_DNS")


WEB_APP_URL = f"https://{HOST_DNS}"
WEB_HOOK_URL = f"https://{HOST_DNS}/bot"

def add_button():
    print(TOKEN_TG)
    print(WEB_APP_URL)
    
    url = f"https://api.telegram.org/bot{TOKEN_TG}/setChatMenuButton"

    payload = {
        "menu_button": {
            "type": "web_app",
            "text": "Open My Web App",
            "web_app": {
                "url": WEB_APP_URL
            }
        }
    }

    response = requests.post(url, json=payload)
    print(response.json())
    return

def set_webhook():
    url = f"https://api.telegram.org/bot{TOKEN_TG}/setWebhook"

    payload = {
        "url": WEB_HOOK_URL
    }

    response = requests.post(url, json=payload)
    print(response.json())
    return


add_button()

# set_webhook()