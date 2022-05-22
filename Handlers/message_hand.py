from const import ADMIN, STATE_CATEGORIES
from db_helper import DBUser
from Buttons.inline_btn import *
from telegram import ReplyKeyboardRemove
import time
db=DBUser('Data_base.db')

def send_location(update, context):
    id=update.message.from_user.id
    if db.check_zakaz(db.get_position(id),id):
        adress=str(update.message.location.longitude)+" "+str(update.message.location.latitude)
        db.add_zakaz(db.get_position(id),id,adress)
        context.bot.send_message(id,"Sizning buyurtmangiz qabul qilindi.Tez orada javob olasiz.", reply_markup=ReplyKeyboardRemove(True))

        ############################### Masterlarga zakaz haqida xabar yuboradi. #####################
        users=db.get_all_users()
        message_id=update.message.message_id
        j=0
        for i in users:
            try:
                if db.get_degree(i[0])=='Master':
                    context.bot.send_message(i[0], "Yangi buyurtma keldi. /startni bosib tekshirib ko'ring.")
                j+=1
                if j==30:
                    time.sleep(1)
                    j=0
            except Exception as e:
                context.bot.send_message(ADMIN, f"Xabar yuborishda xatolik. {e}\n{i[0]}")
                continue
    else:
        context.bot.send_message(id,"Sizning buyurtmangiz qabul qilingan!")

    

def phone_contact(update, context):
    id=update.message.from_user.id
    if db.check_user(id):
        db.add_user(id, update.message.contact.phone_number, update.message.contact.first_name)
        context.bot.send_message(id, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz", reply_markup=ReplyKeyboardRemove())
    context.bot.send_message(id, "O'zingizga kerak bo'lgan xizmatlardan birini tanlang", reply_markup=categories)
    return STATE_CATEGORIES

def admin_send_message(update, context):
    users=db.get_all_users()
    message_id=update.message.message_id
    j=0
    for i in users:
        try:
            context.bot.copy_message(i[0], ADMIN, message_id)
            j+=1
            if j==30:
                time.sleep(1)
                j=0
        except Exception as e:
            context.bot.send_message(ADMIN, f"Xabar yuborishda xatolik. {e}\n{i[0]}")
            continue
      
def master_add(update, context):
    id=update.message.from_user.id
    text=update.message.text
    try:
        number=int(text)
        if id==ADMIN:
            if db.check_phone(number):
                context.bot.send_message(ADMIN, "Bunday raqamdagi foydalanuvchi mavjud emas. Ustani qo'shish uchun usta botga azo bo'lgan bo'lishi kerak.Iltimos /add ni bosib qaytatdan urinib ko'ring.")
            else:  
                db.set_degreee(number,"Master")
                context.bot.send_message(ADMIN, "Qo'shildi.")
                
                context.bot.send_message(db.get_user_id(number), "Tabriklaymiz sizga Masterlik darajasi berildi. /start ni bosib o'z faoliyatingizni boshlashingiz mumkin,.")
        else:
            context.bot.send_message(id, "Bu funksiyani faqatgina adminlar ishlata oladi.")
    except Exception as e:
        context.bot.send_message(ADMIN, "Telefon raqam kiritishda xatolik. Iltimos /add ni bosib qaytatdan urinib ko'ring.")
