import constants
import DBuse
import telegram
from datetime import datetime, date
from image_handler import images
from io import BytesIO

images = images()

constants.__init__()

API_KEY = constants.TELEGRAM_OUTPUT

def main ():
    tod = datetime.today()
    tod_num = tod.day
    news = DBuse.get_news()[0]
    news_ids = DBuse.get_news()[1]
    bot = telegram.Bot(token=API_KEY)
    a = 0
    if len(news) > 0:
        for i in news.keys():
            im = DBuse.get_image(news_ids[news[i]])
            if len(im) == 0:
                bot.send_message(chat_id='@djouma_canal', text="{}".format(news[i]))
                a += 1
            elif len(im) > 0:
                image = images.download_image(news_ids[news[i]])
                bot.send_message(chat_id='@djouma_canal', text="{}", image = image).format(news[i])
                a += 1
        if a == len(news) and tod_num == 3:
            bot.send_message(chat_id='@djouma_canal',
                                 text="Gracias por tu interés en Djouma, solo ese hecho es un gran placer para nosotros. Como ya sabrás, una de las cosas con las que proveemos a los niñ@s becados por Djouma, es el desayudo diario, un desayuno tiene un coste de tan solo 0.20€, 1 EURO equivale al desayuno de 5 niños, te gustaría empezar el día invitando a desayunar a un@ niñ@? Haz click aquí {} para invitar.".format(
                                     constants.TIP_LINK),
                                 )

if __name__ == '__main__':
    main()