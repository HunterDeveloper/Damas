from const import *
from Buttons.inline_btn import *
from Buttons.reply_btn import *
from db_helper import DBUser
db=DBUser('Data_base.db')
def ans_category(update, context):
    query=update.callback_query
    id=query.message.chat.id
    context.bot.send_message(id, "Buyurtmangiz qabul qilinishi uchun lokatsiyangizni jo'nating shu lokatsiya bo'yicha Master boradi.\nLokatsiyangizni jo'natish uchun quyidagi tugmani bosing.", reply_markup=location)
    db.set_position(id, query.data)
    return STATE_LOCATION

def ans_admin(update, context):
    query=update.callback_query
    id=query.message.chat.id
    if query.data=='send_message':
        context.bot.send_message(id, "Yubormoqchi bo'lgan xabaringizni yozing")
        return STATE_SEND

    elif query.data=="xisobot":
        context.bot.send_message(id, "Qaysi kategoriyadagi ma'lumotlarni ko'rmoqchisiz.", reply_markup=admin_categories)
    elif query.data=="all":
        context.bot.send_message(id, f"Umumiy foydalanuvchilar soni: {db.get_count_users()}")
    else:
        context.bot.send_message(id, f"Tanlagan kategoriyangizda bugungi tushgan  zakazlar soni {db.get_count_category(query.data)} \n Bajarilgan: {db.get_ready_category(query.data)}\n")
        

def master_category_ansv(update, context):
    query=update.callback_query
    id=query.message.chat.id

    if query.data=="klapn":
        if db.check_master("klapn"):
            context.bot.send_message(id, "Zakaz berganlar mavjud emas.", reply_markup=master_categories)
        else:
            clent=db.get_zakaz(query.data)[0]
            phone=db.get_user_number(clent)
            adress=(db.get_zakaz(query.data)[1]).split()
            x=float(adress[0])
            y=float(adress[1])
            context.bot.send_contact(id, phone_number=phone,first_name=db.get_user_name(clent))
            context.bot.send_location(id, x, y)
            context.bot.send_message(clent, "Buyurtmangizni master qabul qildi tez orada berilgan manzilga yetib boradi.")
            # context.bot.send_contact(clent, phone_number=db.get_user_number(id),first_name=db.get_user_name(id))
            db.set_master(query.data,clent,id)

    elif query.data=="gaz":
        if db.check_master("gaz"):
            context.bot.send_message(id, "Zakaz berganlar mavjud emas.", reply_markup=master_categories)
        else:
            clent=db.get_zakaz(query.data)[0]
            phone=db.get_user_number(clent)
            adress=(db.get_zakaz(query.data)[1]).split()
            x=float(adress[0])
            y=float(adress[1])
            context.bot.send_contact(id, phone_number=phone,first_name=db.get_user_name(clent))
            context.bot.send_location(id, x, y)
            context.bot.send_message(clent, "Buyurtmangizni master qabul qildi tez orada berilgan manzilga yetib boradi.")
            # context.bot.send_contact(clent, phone_number=db.get_user_number(id),first_name=db.get_user_name(id))
            db.set_master(query.data,clent,id)

    elif query.data=="resor":
        if db.check_master("resor"):
            context.bot.send_message(id, "Zakaz berganlar mavjud emas.", reply_markup=master_categories)
        else:
            clent=db.get_zakaz(query.data)[0]
            phone=db.get_user_number(clent)
            adress=(db.get_zakaz(query.data)[1]).split()
            x=float(adress[0])
            y=float(adress[1])
            context.bot.send_contact(id, phone_number=phone,first_name=db.get_user_name(clent))
            context.bot.send_location(id, x, y)
            context.bot.send_message(clent, "Buyurtmangizni master qabul qildi tez orada berilgan manzilga yetib boradi.")
            # context.bot.send_contact(clent, phone_number=db.get_user_number(id),first_name=db.get_user_name(id))
            db.set_master(query.data,clent,id)
    
    if query.data=="gaz_regr":
        if db.check_master("gaz_regr"):
            context.bot.send_message(id, "Zakaz berganlar mavjud emas.", reply_markup=master_categories)
        else:
            clent=db.get_zakaz(query.data)[0]
            phone=db.get_user_number(clent)
            adress=(db.get_zakaz(query.data)[1]).split()
            x=float(adress[0])
            y=float(adress[1])
            context.bot.send_contact(id, phone_number=phone,first_name=db.get_user_name(clent))
            context.bot.send_location(id, x, y)
            context.bot.send_message(clent, "Buyurtmangizni master qabul qildi tez orada berilgan manzilga yetib boradi.")
            # context.bot.send_contact(clent, phone_number=db.get_user_number(id),first_name=db.get_user_name(id))
            db.set_master(query.data,clent,id)


        
    