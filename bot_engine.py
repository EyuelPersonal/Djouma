import constants as const
import DBuse
import telegram
from telegram.ext import ConversationHandler
from io import BytesIO
from image_handler import images
import os
from PIL import Image

curr = os.curdir
folder = 'Images'
images_path = os.path.join(curr,folder)


images = images()

const.__init__()

START,PHOTO, WITH_PHOTO, WITHOUT_PHOTO,SUBMIT,DELETE= range(6)

chat_info = dict()


# Include on previous wiht start that will serve as a CallBackQuery Handler, careate a fucntion that will be a Filet Image, and in start, make an if statement to go for the Filter text or filter image
def start(update,context):
    user = update.message.from_user.first_name

    options = [[telegram.InlineKeyboardButton('YES', url=None, callback_data='YES')], [telegram.InlineKeyboardButton('NO', url=None, callback_data='NO')] ]
    reply_markup = telegram.InlineKeyboardMarkup(options)

    update.message.reply_text("Hola {}, dinos se tu mensaje incluirá foto".format(user),
                              reply_markup = reply_markup)
    return PHOTO

def photo(update, context):
    query = update.callback_query
    photo = query.data

    if photo == 'YES':
        context.bot.edit_message_text(chat_id=query.message.chat_id,
                                     message_id=query.message.message_id,
                                     text='A continuación, adjunta tu foto.'
                                     )
        #update.message.reply_text("Para que podamos guardar tu foto y tu mensaje correctamente, porfavor, adjunta tu foto y escribe tu mensaje en el formato de siempre (Desde [tu ONG] informamos que [tu noticia])")
        return WITH_PHOTO
    else:
        context.bot.edit_message_text(chat_id=query.message.chat_id,
                                     message_id=query.message.message_id,
                                     text='Para que podamos guardar tu mensaje correctamente, sigue el formato de siempre (Desde [tu ONG] informamos que [tu noticia]'
                                     )

        #update.message.reply_text("Para que podamos guardar tu mensaje correctamente, sigue el formato de siempre (Desde [tu ONG] informamos que [tu noticia]")
        return WITHOUT_PHOTO

def store_message_without(update,context):

    news_id = update.message.message_id
    message = update.message.from_user
    user_id = message.id
    user_name = message.first_name
    text = update.message.text
    DBuse.add_news(int(news_id-2),int(user_id),str(user_name),str(text))
    update.message.reply_text("Tu noticia ha sido registrada correctamente, si deseas borrarla envía /delete y si deseas enviar otra noticia, envia /repeat y luego /start")
    return DELETE


def store_message_with(update,context):

    news_id = update.message.message_id
    message = update.message.from_user
    user_id = message.id
    user_name = message.first_name
    image = context.bot.get_file(update.message.photo[-1].file_id)
    file = BytesIO(image.download_as_bytearray())
    #file = Image.open(image)
    images.upload_image(file, news_id)

    update.message.reply_text("Tu foto ha sido guardada, ahora envianos la noticia con el formato: Desde [tu ONG] informamos que [tu noticia]")
    return WITHOUT_PHOTO

def delete(update,context):
    message = update.message.from_user
    user_id = message.id
    DBuse.delete_news(user_id)
    update.message.reply_text("Tu noticia ha sido borrada correctamente, si deseas enviar una nueva noticia envia /repeat y luego /start")
    return DELETE

def cancel(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Gracias, si deseas enviar otra noticia, envia /start")
    return ConversationHandler.END








