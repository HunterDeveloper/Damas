from telegram.ext import Updater, ConversationHandler, CommandHandler,CallbackQueryHandler, MessageHandler, Filters
from telegram import BotCommand


from const import *

from Handlers.comm_hand import *
from Handlers.message_hand import *
from Handlers.query_hand import *
def main():
    updater = Updater(TOKEN)
    dispacher= updater.dispatcher
    dispacher.bot.set_my_commands([
        BotCommand('start', 'Foydalanishni boshlash')
    ])
    conv_hand=ConversationHandler( 
        entry_points=[CommandHandler('start', start)],
        states={
            STATE_REGISTER: [ 
                CommandHandler('start', start),
                CommandHandler('aftor', aftor),
                MessageHandler(Filters.contact, phone_contact)
            ],
            STATE_CATEGORIES: [ 
                CommandHandler('start', start),
                CommandHandler('aftor', aftor),
                CallbackQueryHandler(ans_category),
            ],
            STATE_LOCATION: [ 
                CommandHandler('start', start),
                CommandHandler('aftor', aftor),
                MessageHandler(Filters.location, send_location)
            ],
            STATE_ADMIN: [ 
                CommandHandler('start', start),
                CommandHandler('aftor', aftor),
                CommandHandler("clean",clean),
                CommandHandler("add",add_master),
                MessageHandler(Filters.text, master_add),
                CallbackQueryHandler(ans_admin),
            ],
            STATE_SEND: [ 
                CommandHandler('start', start),
                CommandHandler('aftor', aftor),
                MessageHandler(Filters.all, admin_send_message),
            ],
            STATE_MASTER: [ 
                CommandHandler('start', start),
                CommandHandler('aftor', aftor),
                CallbackQueryHandler(master_category_ansv)
            ]
        },
        fallbacks=[CommandHandler('start', start)]
    )
    dispacher.add_handler(conv_hand)
    updater.start_polling()
    updater.idle()
main()