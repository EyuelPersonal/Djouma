import json

TELEGRAM_INPUT = TELEGRAM_OUTPUT = HOST = USER = DATABASE = PASS = ""

def __init__():
    global TELEGRAM_INPUT, TELEGRAM_OUTPUT, HOST, USER, DATABASE, PASS
    with open("/Users/Eyuel/PycharmProjects/Djouma/settings.json") as data:
        data = json.load(data)
    TELEGRAM_INPUT = data['API_KEYS']['TELEGRAM_INPUT']
    TELEGRAM_OUTPUT = data['API_KEYS']['TELEGRAM_OUTPUT']
    HOST = data['db']['host']
    USER = data['db']['user']
    DATABASE = data['db']['data_base']
    PASS = data['db']['pass']