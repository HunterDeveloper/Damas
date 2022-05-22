from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
categories=InlineKeyboardMarkup( [ 
    [ InlineKeyboardButton('Klapn tortish:30 000', callback_data='klapn'),InlineKeyboardButton('Ressor ustanovka:300 000', callback_data='resor')]
])
master_categories=InlineKeyboardMarkup( [ 
    [ InlineKeyboardButton('Klapn tortish', callback_data='klapn'),InlineKeyboardButton('Ressor ustanovka', callback_data='resor')]
])

admin_categories=InlineKeyboardMarkup( [ 
   [ InlineKeyboardButton('Klapn tortish', callback_data='klapn'),InlineKeyboardButton('Ressor ustanovka', callback_data='resor')],
    [ InlineKeyboardButton('Hamma foydalanuvchilar soni.', callback_data='all')]
])

admin_btn=InlineKeyboardMarkup( [ 
    [ InlineKeyboardButton("📤 Xabar jo'natish", callback_data='send_message'),InlineKeyboardButton("📜 Xisobot", callback_data='xisobot')]]
)
 
 