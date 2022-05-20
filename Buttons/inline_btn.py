from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
categories=InlineKeyboardMarkup( [ 
    [ InlineKeyboardButton('Klapn tortish:20 000', callback_data='klapn'),InlineKeyboardButton('Gaz legirofka:10 000', callback_data='gaz')],
    [ InlineKeyboardButton('Ressor ustanovka:50 000', callback_data='resor'),InlineKeyboardButton('Gaz regr:40 000', callback_data='gaz_regr')],
])
master_categories=InlineKeyboardMarkup( [ 
    [ InlineKeyboardButton(f'Klapn tortish:', callback_data='klapn'),InlineKeyboardButton('Gaz legirofka:10 000', callback_data='gaz')],
    [ InlineKeyboardButton('Ressor ustanovka:50 000', callback_data='resor'),InlineKeyboardButton('Gaz regr:40 000', callback_data='gaz_regr')],
])

admin_btn=InlineKeyboardMarkup( [ 
    [ InlineKeyboardButton("📤 Xabar jo'natish", callback_data='send_message'),InlineKeyboardButton("📜 Sonini ko'rish", callback_data='show_users')]]
)
number_users=InlineKeyboardMarkup( [ 
    [InlineKeyboardButton("Umumiz soni", callback_data="all")],
    [ InlineKeyboardButton('📚 Kitoblar', callback_data='konstavar'),InlineKeyboardButton('👕 Kiyimlar', callback_data='clothes')],
    [InlineKeyboardButton("👟 Oyoq kiyimlar", callback_data='shoes')]
])