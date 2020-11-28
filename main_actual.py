import constants
import DBuse
import telegram

constants.__init__()

API_KEY = constants.TELEGRAM_OUTPUT

def main ():
    news = DBuse.get_news()
    bot = telegram.Bot(token=API_KEY)
    a = 0
    if len(news) > 0:
        for i in news:
            bot.send_message(chat_id='@djouma_canal', text="{}".format(i))
            a += 1
        if a == len(news):
            bot.send_message(chat_id='@djouma_canal',
                                     text="Gracias por tu interés en Djouma, solo ese hecho es un gran placer para nosotros. Como ya sabrás, una de las cosas con las que proveemos a los niñ@s becados por Djouma, es el desayudo diario, un desayuno tiene un coste de tan solo 0.20€, te gustaría empezar el día invitando a desayunar a un@ niñ@? Haz click aquí {} para invitar.",
                                     )

if __name__ == '__main__':
    main()