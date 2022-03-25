import sqlite3
# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы
db_name="dbb.db"
conn = sqlite3.connect(db_name)

# Создаем курсор - это специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()




#общие
#запрос к бд
def db_insert(a,b):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()# курсор
    cursor.execute(f"INSERT INTO {b} (name) VALUES ({a}) ")#Делаем INSERT запрос к базе данных
    conn.commit()#сохранить транзакцию
    conn.close()#закрыть соединение с базой данных
#получение всего
def db_select(b):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()# курсор
    cursor.execute(f"SELECT * FROM {b}")#Делаем INSERT запрос к базе данных
    results = cursor.fetchall()
    conn.close()#закрыть соединение с базой данных
    return results
def dell_db(name_table,column,val):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()  # курсор
    cursor.execute(f"DELETE FROM {name_table} WHERE {column} = '{val}';")  # Делаем INSERT запрос к базе данных
    conn.commit()#сохранить транзакцию
    conn.close()  # закрыть соединение с базой данных




###########################################################################
###########################################################################
###########################################################################
###########################################################################
####################################################################
#раздел администрации,данные  [index,name,date]
#добавление админа
def db_insert_admins(a):
    db_insert(a,'\'admins\'')


#админы
#скальп с базы админов
def db_select_admins():
    db_select('\"admins\"')

#вывод индексов админов
def all_ind_adm():
    admin_db = db_select_admins()
    comm=[]
    for i in range(0,(len(admin_db))):
        comm.append(admin_db[i][0])
    return comm

#вывод админов
def all_adm_name():
    admin_db = db_select_admins()
    comm=[]
    for i in range(0,(len(admin_db))):
        comm.append(admin_db[i][0])
    return comm


#удаление админа\"index\"
def dell_admins(val):
    dell_db("admins","\"index\"",val)



###########################################################################
###########################################################################
###########################################################################
###########################################################################

#группы
#########################################################
#добавление групп
def db_insert_groups(a,c):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()# курсор
    cursor.execute(f"INSERT INTO groups (id,name) VALUES ({a},{c})")#INSERT INTO {b} (id,name) VALUES ({a,c}) ")#Делаем INSERT запрос к базе данных
    conn.commit()#сохранить транзакцию
    conn.close()#закрыть соединение с базой данных
#db_insert_groups(7854858,"64564")

#скальп с базы групп
def db_select_group():
    return db_select('\"groups\"')
#вывод индексов групп
def all_ind_group():
    group_db = db_select_group()
    comm=[]
    for i in range(0,(len(group_db))):
        comm.append(group_db[i][0])
    return comm
#даление группы
def dell_group(val):
    dell_db("groups", "\"ind\"", val)

def groups_untable():
    groups=db_select_group()
    grop__=""
    i=0
    while i<(len(groups)):
        grop__+=f"{groups[i][0]}. {groups[i][2]}\n"
        i+=1
    return (grop__)
###########################################################################
###########################################################################
###########################################################################
###########################################################################


#добавление поста
def db_insert_posts(a,name,b,c):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()# курсор
    cursor.execute(f"INSERT INTO {name} (dat,text_,group_id) VALUES ({a,b,c},) ")#Делаем INSERT запрос к базе данных
    conn.commit()#сохранить транзакцию
    conn.close()#закрыть соединение с базой данных
#посты

def db_select_posts(a):
    db_select(a)

#посты в ожидании

def db_select_posts_in_exp(a):
    db_select(a)