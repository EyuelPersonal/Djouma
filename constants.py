import json

TELEGRAM_INPUT = TELEGRAM_OUTPUT = HOST = USER = DATABASE = PASS = WPNAME = WPPASS = URL = TIP_LINK = ""

def __init__():
    global TELEGRAM_INPUT, TELEGRAM_OUTPUT, HOST, USER, DATABASE, PASS, WPNAME, WPPASS, URL, TIP_LINK
    try:
        with open("/Users/eyuelmelese/Djouma/settings.json") as data:
            data = json.load(data)
    except Exception as e:
        try:
            with open("/home/eyuelwolde_gmail_com/Djouma/settings.json") as data:
                data = json.load(data)
        except Exception as eb:
            print(eb)
    TELEGRAM_INPUT = data['API_KEYS']['TELEGRAM_INPUT']
    TELEGRAM_OUTPUT = data['API_KEYS']['TELEGRAM_OUTPUT']
    HOST = data['db']['host']
    USER = data['db']['user']
    DATABASE = data['db']['data_base']
    PASS = data['db']['pass']
    WPNAME = data['wp']['user_name']
    WPPASS = data['wp']['password']
    URL = data['wp']['url']
    TIP_LINK = data['tip_link']