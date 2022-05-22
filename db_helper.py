import sqlite3
from datetime import  datetime, timedelta
class DBUser:
    def __init__(self, db_name):
        self.conn=sqlite3.connect(db_name, check_same_thread=False)
        self.conn.row_factory=sqlite3.Row

    def db_exequite(self, sql, commit=False, fetchone=False, fechall=False):
        self.conn=sqlite3.connect('Data_base.db', check_same_thread=False)
        connection =self.conn
        cursor = connection.cursor()
        data=None
        cursor.execute(sql)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fechall:
            data = cursor.fetchall()

        connection.close()

        return data
    
     # Foydalanuvchi ma'lumotlar bazasida bor yoki yo'qligini tekshiradigan funksiya
    def check_user(self, id):
        sql = f"SELECT id FROM Users WHERE id={id}"
        res=self.db_exequite(sql,fechall=True)
        if len(res)==0: return True
        else : return False

    def check_phone(self, phone):
        sql = f"SELECT id FROM Users WHERE number={phone}"
        res=self.db_exequite(sql,fechall=True)
        if len(res)==0: return True
        else : return False
        
    # Faydalanuvchilarni qo'shuvchi funksiya
    def add_user(self, id, phone, name):
        sql = f""" INSERT INTO Users VALUES( {id}, '{name}', {phone},"empty", "User" )"""
        self.db_exequite(sql,commit=True)
    
    def set_position(self, id, position):
        sql = f""" UPDATE Users
                    SET position="{position}"
                    WHERE id={id} """
        self.db_exequite(sql,commit=True)
    
    def set_degreee(self, phone, degree):
        sql = f""" UPDATE Users
                    SET degree="{degree}"
                    WHERE number={phone} """
        self.db_exequite(sql,commit=True)
    
    def get_degree(self,id):
        sql = f""" SELECT degree FROM Users WHERE id={id}"""
        return self.db_exequite(sql, fetchone=True)[0]
    
    def get_position(self,id):
        sql = f""" SELECT position FROM Users WHERE id={id}"""
        return self.db_exequite(sql, fetchone=True)[0]
    
    def get_user_name(self, id):
        sql = f""" SELECT name FROM Users WHERE id={id}"""
        return self.db_exequite(sql, fetchone=True)[0]

    def get_user_id(self, phone):
        sql = f""" SELECT id FROM Users WHERE number={phone}"""
        return self.db_exequite(sql, fetchone=True)[0]
    
    def get_user_number(self, id):
        sql = f""" SELECT number FROM Users WHERE id={id}"""
        return self.db_exequite(sql, fetchone=True)[0]
    
    # Hamma foydalanuvchilarni id sini olib beraqdi
    def get_all_users(self):
        sql = """ SELECT id FROM Users """
        return self.db_exequite(sql, fechall=True)
    
    # qancha foydalanuvchi borligini qaytaradi
    def get_count_users(self):
        sql = " SELECT COUNT(id) FROM Users "
        return self.db_exequite(sql, fetchone=True)[0]
    
    def get_count_category(self, name):
        today=str(datetime.now()+timedelta(hours=5))[:10]
        sql = f""" SELECT COUNT(name) FROM Zakaz WHERE time like "{today}%" and name="{name}" """
        return self.db_exequite(sql, fetchone=True)[0]
    
    
    def get_ready_category(self, name):
        today=str(datetime.now()+timedelta(hours=5))[:10]
        sql = f""" SELECT COUNT(name) FROM Zakaz WHERE time like "{today}%"and  name="{name}"and not master=0 """
        return self.db_exequite(sql, fetchone=True)[0]

    def clean(self):
        sql = "DELETE FROM Users"
        self.db_exequite(sql,commit=True)
    ####################################### zakaz #############################

    def add_zakaz(self, name, clent, location):
        today=str(datetime.now()+timedelta(hours=5))[:-7]
        sql = f'''INSERT INTO Zakaz VALUES("{name}", {clent}, 0, "{today}", '{location}')'''
        self.db_exequite(sql,commit=True)

    def check_zakaz(self, name, clent):
        sql = f'''SELECT * FROM Zakaz WHERE name="{name}" AND clent={clent} AND master=0'''
        res=self.db_exequite(sql,fechall=True)
        if len(res)==0: return True
        else : return False

    def check_master(self, name):
        sql = f'''SELECT * FROM Zakaz WHERE name="{name}" AND master=0'''
        res=self.db_exequite(sql,fechall=True)
        if len(res)==0: return True
        else : return False
    def get_zakaz(self, name):
        sql = f'''SELECT clent,location FROM Zakaz WHERE name="{name}"'''
        return self.db_exequite(sql,fetchone=True)

    def set_master(self, name, clent, master):
        today=str(datetime.now()+timedelta(hours=5))[:10]
        sql = f""" UPDATE Zakaz 
                    SET master={master}
                    WHERE time like "{today}%" AND name="{name}" and clent={clent}"""
        self.db_exequite(sql,commit=True)

    # klentning bazada bor yoki yo'qligini tekshiradi agarda yo'q bolsa shu kiritgan mahsulotiga qo'shib qo'yadi. Agar bor bo'lsa false chiqaradi


    # def check_pair(self, name, number):
    #     sql = f""" SELECT * FROM Product WHERE pair_id_1=0 AND name="{name}" AND number="{number}" """
    #     res= self.db_exequite(sql, fechall=True)
    #     if len(res)==0:
    #         return False
    #     else: return True

    # def check_number(self, number):
    #     sql = f""" SELECT * from Product WHERE number="{number}" """
    #     res=self.db_exequite(sql,fechall=True)
    #     if len(res)==0:
    #         return True
    #     else:
    #         return False

    # def add_product(self, name, number):
    #     sql = f""" INSERT INTO Product VALUES("{name}", 0,0,"{number}")"""
    #     self.db_exequite(sql,commit=True)

    

    # def set_pair_2(self, name, id, number):
    #     sql = f""" UPDATE Product
    #                 SET pair_id_2={id}
    #                 WHERE name="{name}" and number="{number}" """
    #     self.db_exequite(sql,commit=True)
    
    # def get_pair_1(self, name, number):
    #     sql = f""" SELECT pair_id_1 FROM Product WHERE name="{name}" and number="{number}" """
    #     return self.db_exequite(sql, fetchone=True)[0]

    # def get_pair_2(self, name, number):
    #     sql = f""" SELECT pair_id_2 FROM Product WHERE name="{name}" and number="{number}" """
    #     return self.db_exequite(sql, fetchone=True)[0]
    
    # def check_pair_1(self, name, id, number):
    #     sql = f""" SELECT number FROM Product WHERE name="{name}" AND pair_id_1={id} and number="{number}" """
    #     res=self.db_exequite(sql,fechall=True)
    #     if len(res)==0:
    #         return True
    #     else:
    #         return False
        