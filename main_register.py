from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackContext,MessageHandler,Filters
import bot_engine
import constants

START,SUBMIT,DELETE= range(3)

constants.__init__()

API_KEY = constants.TELEGRAM_INPUT

def main ():
    #updater, recieves info from telegram and delivers this info to the dispacher class, which will classify the updates according to
    #handlers we specify and deliver them to a callback fucntion we specify
    updaterUser = Updater(token=API_KEY, use_context=True)
    dispatcherUser = updaterUser.dispatcher
    contextUser = CallbackContext(dispatcherUser)
    convHandlerUser = ConversationHandler(
        entry_points= [CommandHandler('start',bot_engine.start)],
        states={

            START: [MessageHandler(filters=[Filters.text, Filters.photo],callback=bot_engine.store_message)],

            DELETE: [CommandHandler('delete',bot_engine.delete)]

        },

        fallbacks = [CommandHandler(['cancel','repeat'], bot_engine.cancel)]

    )

    dispatcherUser.add_handler(convHandlerUser)
    updaterUser.start_polling()

#updater.start_polling()
if __name__ == '__main__':
    main()
