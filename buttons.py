from aiogram import types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

import conf


################## КЛИЕНТСКИЕ КНОПКИ ###############################
beck_butt=InlineKeyboardButton("Назад.",callback_data='back')
mark_beck_butt = InlineKeyboardMarkup().add(beck_butt)

################ Админская ЧАСТЬ #########################

#стартовые кнопки меню
admin_groups_butt=InlineKeyboardButton("Группы.",callback_data='groups')
admin_posts_butt=InlineKeyboardButton("Публикации.",callback_data='posts')
admin_doc_butt=InlineKeyboardButton("Документация.",callback_data='doc')
admin_pref_butt=InlineKeyboardButton("Настройки.",callback_data='pref')
#admin_werbs_butt=InlineKeyboardButton("Ключевые слова.",callback_data='werbs')
admin_adm_butt=InlineKeyboardButton("Администраторы",callback_data='adm')
admin_start_butts = InlineKeyboardMarkup().add(admin_posts_butt,admin_groups_butt).add(admin_adm_butt,admin_doc_butt).add(admin_pref_butt)

#кнопки в аадминах
admin_delite=InlineKeyboardButton("Удалить администратора.",callback_data='del_admins')
admins_butts = InlineKeyboardMarkup().add(admin_delite).add(beck_butt)

#кнопки групп
add_group=InlineKeyboardButton("Добавить группу.",callback_data='add_groups')
del_group=InlineKeyboardButton("Удалить группу",callback_data='del_groups')
group_butt = InlineKeyboardMarkup().add(add_group,del_group).add(beck_butt)

#Удаление группы
dell_group_but=InlineKeyboardButton('Удалить группу',callback_data='del_groups')
del_group_butt = InlineKeyboardMarkup().add().add(beck_butt)

#меню поста
new_post=InlineKeyboardButton('Новый пост.',callback_data='new_post')
del_post=InlineKeyboardButton('Удалить существующий.',callback_data='del_post')
re_post=InlineKeyboardButton('Изменить существующий.',callback_data='re_post')
exp_post=InlineKeyboardButton('Изменить/удалить пост в ожидании.',callback_data='exp_post')

new_post_menu=InlineKeyboardMarkup().add(new_post,del_post).add(re_post,exp_post).add(beck_butt)

#Удаление\изменение поста в обработке.
re_exp_post=InlineKeyboardButton('Изменить пост в ожидании.',callback_data='re_exp_post')
del_exp_post=InlineKeyboardButton('Удалить пост в ожидании.',callback_data='del_exp_post')
exp_post_menu=InlineKeyboardMarkup().add(re_exp_post).add(del_exp_post).add(beck_butt)