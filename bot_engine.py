import constants as const
import DBuse
import telegram
from telegram.ext import ConversationHandler
from io import BytesIO
from image_handler import images
images = images()

const.__init__()

START,SUBMIT,DELETE= range(3)

chat_info = dict()

def start(update,context):
    user = update.message.from_user.first_name
    options = [telegram.InlineKeyboardButton('YES','NO')]
    reply_markup = telegram.InlineKeyboardMarkup(options)
    update.message.reply_text("Hola {}, ¿cuales son las noticias de hoy? Por favor, sigue el siguiente formato: Desde [tu ONG] informamos que: [tu noticia], y a continuacion dinos si tu noticia lleva foto, gracias!".format(user))
    return START

def store_message(update,context):
    query = update.callback_query
    photo = query.data
    news_id = update.message.message_id
    message = update.message.from_user
    user_id = message.id
    user_name = message.first_name
    if photo == 'NO':
        text = update.message.text
        DBuse.add_news(int(news_id),int(user_id),str(user_name),str(text))
        update.message.reply_text("Tu noticia ha sido registrada correctamente, si deseas borrarla envía /delete y si deseas enviar otra noticia, envia /repeat y luego /start")
    elif photo == 'YES':
        image = context.bot.get_file(message.photo[-1].file_id)
        file = BytesIO(image.download_as_bytearray())
        images.upload_image(file,news_id)

        text = update.message.text
        DBuse.add_news(int(news_id), int(user_id), str(user_name), str(text))
        update.message.reply_text("Tu noticia ha sido registrada correctamente, si deseas borrarla envía /delete y si deseas enviar otra noticia, envia /repeat y luego /start")

    return DELETE

def delete(update,context):
    user_id = update.message.from_user.id
    DBuse.delete_news(user_id)
    update.message.reply_text("Tu noticia ha sido borrada correctamente, si deseas enviar una nueva noticia envia /repeat y luego /start")
    return DELETE

def cancel(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Gracias, si deseas enviar otra noticia, envia /start")
    return ConversationHandler.END








