import requests
from const import TOKEN_TG
from const import HOST_DNS

WEB_APP_URL = f"https://{HOST_DNS}"
WEB_HOOK_URL = f"https://{HOST_DNS}/bot"

def add_button():
    url = f"https://api.telegram.org/bot{TOKEN_TG}/setWebhook"

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
    url = f"https://api.telegram.org/bot{TOKEN_TG}/setChatMenuButton"

    payload = {
        "url": WEB_HOOK_URL
    }

    response = requests.post(url, json=payload)
    print(response.json())
    return


# add_button()

# set_webhook()