from Buttons.reply_btn import *
from db_helper import DBUser
from const import ADMIN, STATE_ADD_CATEGORY_NUMBER, STATE_ADMIN, STATE_CATEGORIES, STATE_MASTER, STATE_REGISTER
from Buttons.inline_btn import *

db=DBUser('Data_base.db')
def start(update, context):
    id=update.message.from_user.id
    if id==ADMIN:
        context.bot.send_message(id, "Assalomu alaykum. Quyidagi tugmalardan birini tanlang.", reply_markup=admin_btn)
        return STATE_ADMIN
    elif db.check_user(id):
        context.bot.send_message(id,"Assalomu alaykum Hush kelibsiz. Ro'yxatdan o'tish uchun quyidagi tugmani bopsing", reply_markup=ask_phone)
        return STATE_REGISTER
    elif db.get_degree(id)=="Master":
        context.bot.send_message(id, "Zakazlarni tekshirish", reply_markup=master_categories)
        return STATE_MASTER
    else:
        context.bot.send_message(id, "Quyidagi kategoriyalardan birini tanlang", reply_markup=categories)
        return STATE_CATEGORIES

def aftor(update, context):
     update.message.reply_text("Yaratuvchi Tursunaliuyev Humoyunmirzo")

def add_master(update, context):
    update.message.reply_text("Ustani qo'shish uchun uning telefon raqamini to'liq kiriting.\n Masalan: +998930065969")
    return STATE_ADMIN

def clean(update, context):
    db.clean()