from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor

import conf
from bd import db_insert_admins,all_adm_name,db_select_group,groups_untable
import buttons as butt
from datetime import datetime
#настройки
bot = Bot(token=conf.KEY)
dp = Dispatcher(bot, storage=MemoryStorage())
if not bot:
    exit("Error: no token provided")

###########################################################################
###########################################################################
#админская часть
@dp.callback_query_handler(text="back")
async def back_2(call: types.CallbackQuery):#message: types.Message
    await call.message.answer(f'Это бот для управления группами\n'
                         f'Выбери меню какое тебе необходимо и выполни свою задачу',reply_markup=butt.admin_start_butts)
    await call.message.delete()

@dp.callback_query_handler(text="back")
async def back(message: types.Message):#message: types.Message
    await message.answer(f'Это бот для управления группами\n'
                         f'Выбери меню какое тебе необходимо и выполни свою задачу',reply_markup=butt.admin_start_butts)
    await message.delete()

###########################################################################
###########################################################################
##############################################################################
#проверка пороля
class check_pussword(StatesGroup):
    start_state = State()
@dp.message_handler(commands=['start'])
async def buttons_start(message: types.Message):
    ADMINS = all_adm_name()
    us = message.from_user.id
    if us in ADMINS:
        await back(message)
    else:
        await message.answer(f'Пожалуйста подтвердите что вы админ.\n'
                         f'Введите пороль.')
        await message.delete()
        await check_pussword.start_state.set()

@dp.message_handler(state=check_pussword.start_state)
async def check_puss(message: types.Message,state:FSMContext):
    puss=message.text
    ps=conf.PASSWORD
    while puss != ps:
        await message.answer("Пожалуйста введите верный пароль.")
        return

    adm=message.from_user.id
    db_insert_admins(adm)
    print(adm)

    await state.finish()
    await message.answer("Пароль подтвержден.")
    await message.delete()
    await back(message)

###########################################################################
###########################################################################
###########################################################################
###########################################################################

#публикации

##################меню публикации
@dp.callback_query_handler(text="posts")
async def posts(call: types.CallbackQuery):
    await call.message.answer(f'Выберите действие с постами.',reply_markup = butt.new_post_menu)
    await call.message.delete()

#новая публикации
class new_post(StatesGroup):
    date=State()
    text=State()
    group=State()
    finish=State()
#информация по созданию
@dp.callback_query_handler(text="new_post")
async def new_post_(call: types.CallbackQuery):
    await call.message.answer(f'Создание новой публикации.'
                         f'Необходимо указать:\n'
                         f'1.Дату(Сейчас\дата и время)\n'
                         f'2.Текст\n'
                         f'3.ID группы из списка.\n'
                         f'(список будет дан позже)\n\n\n\n'
                         f'Пожалуйста укажите дату:'
                         f'Сейчас/Дату и время\n'
                         f'Формат(дд.мм*час:минут)  ',reply_markup = butt.mark_beck_butt)#,reply_markup=butt.
    await call.message.delete()
    await new_post.date.set()
#ввод даты
@dp.message_handler(state=new_post.date)
async def date__vv(message: types.Message,state:FSMContext):
    date_=message.text
    if date_.lower()=="сейчас":
        await message.answer("Пост будет опубликован после его отправки.")
        await state.update_data(data=message.text())
        await message.delete()
        await new_post.next()
    else:
        #нахождение знаков
        star_ind=date_.index("*")
        point_ind=date_.index(".")
        tp_ind = date_.index(":")
        #получение цифр дня
        day=date_[:point_ind]
        #получение цифр месяца
        month=date_[point_ind:star_ind]
        #получение цифр часы
        hour=date_[star_ind:tp_ind]
        #получение цифр минут
        min=date_[tp_ind:]
        #получение сегодняшней даты
        dat=str(datetime.today())
        #сегодняшний день
        d2=int(dat[8:10])
        #получение сегодняшнего месяца
        m2=int(dat[5:7])
        #получение минуты
        min_=int(dat[14:16])
        #получение часа
        hour_= int(dat[11:13])
        x=0
        while x!=1:
            try:
                day=int(day)
                month = int(month)
                hour = int(hour)
                min = int(min)
                x+=1
            except:
                message.answer("Пожалуйста введите цифры")
            return

        while False==((day>=d2 and day<=31) and (month>=m2 and month<=12) and (hour>=hour_ and hour<=23) and (min>=min_ and min<=59)):
            message.answer("Пожалуйста введите корректную дату.")
            return

        await message.answer(f"Дата принята.\n{date_}")
        await state.update_data(data=message.text())
        await message.delete()
        await message.answer("Пожалуйста введите текст.")
        await new_post.next()



#ввод текста
@dp.message_handler(state=new_post.text)
async def txt__vv(message: types.Message,state:FSMContext):
    await new_post.update_data(text=message.text())
    await message.delete()
    await message.answer(f"Выберите группу из списка.'\n"
                         f"Введите id группы.\n"
                         f"")
    await new_post.next()

#ввод текста
@dp.message_handler(state=new_post.group)
async def group__vv(message: types.Message,state:FSMContext):
    await message.answer("gg")





###########################################################################

#удаление публикации
@dp.callback_query_handler(text="del_post")
async def del_post(call: types.CallbackQuery):
    await call.message.answer(f'Удаление поста.'
                         f'Пожалуста выберите из существующих пост для удаления.')#,reply_markup=butt.
    await call.message.delete()

#Изменение сущ публикации
@dp.callback_query_handler(text="re_post")
async def re_post(call: types.CallbackQuery):
    await call.message.answer(f'Изменение опубликованных постов.'
                         f'Пожалуйста выберите пост для изменения')#,reply_markup=butt.
    await call.message.delete()

#удаление\изменение поста в обработке
@dp.callback_query_handler(text="exp_post")
async def rd_post(call: types.CallbackQuery):
    await call.message.answer(f'Удаление\изменение поста в обработке.'
                         f'Пожалуйста выберите действие.')#,reply_markup=butt.
    await call.message.delete()

#удаление поста в обработке
@dp.callback_query_handler(text="exp_post")
async def del_exp_post(call: types.CallbackQuery):
    await call.message.answer(f'Удаление\изменение поста в обработке.'
                         f'Пожалуйста выберите действие.')#,reply_markup=butt.
    await call.message.delete()


###########################################################################
###########################################################################
###########################################################################
###########################################################################

#действия с группами
#главное меню групп
@dp.callback_query_handler(text="groups")
async def groups(call: types.CallbackQuery):
    groups=db_select_group()
    a=""
    if groups==None:
        a="Групп не добавлено."
    else:

        await call.message.answer(f'Ваша группа/группы :\n'
                                  f'ID.Название'
                                  f'{groups_untable()}',reply_markup=butt.group_butt)#,reply_markup=butt.
        await call.message.delete()

#удаление группы
@dp.callback_query_handler(text="del_groups")
async def del_groups(call: types.CallbackQuery):









#старт полинг
if __name__ == '__main__':
    executor.start_polling(dp)

