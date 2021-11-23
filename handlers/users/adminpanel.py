from aiogram import types
from keyboards.default.account_keyboard import admin_menu, admin_panel
from loader import dp, UsersDb

@dp.message_handler(commands="admgetfromuser")
async def adminstab(message: types.Message):
    await UsersDb.adminget(message.chat.id)
    await message.answer("Вы получили права администратора🧙\n"
                         "Напишите /startadmin,чтобы войти в ЛК с правами администрации❗️")

@dp.message_handler(commands="adminremove")
async def adminsremove(message: types.Message):
    await UsersDb.adminremove(message.chat.id)
    await message.answer("Вы сняты!🧙\n")

@dp.message_handler(commands="startadmin")
async def admins(message: types.Message):
    admin_check = await UsersDb.admin_checks()
    if admin_check == 1:
        await message.answer("Вы вошли в ЛК с возможностью администратора", reply_markup=admin_menu())

    else:
        await message.answer("Куда лезит этот новичок?\n "
                             "Отказано в доступе админ панели")

@dp.message_handler(text ="Панель администратора")
async def admins_tab(message: types.Message):
    admin_check = await UsersDb.admin_checks()
    if admin_check == 1:
        await message.answer("Вы вошли в панель администратора", reply_markup=admin_panel())
    else:
        print(admin_check)
        await message.answer("Отказано в доступе")

@dp.message_handler(text= "Назад в ЛК")
async def admins_tabs(message: types.Message):
        admin_check = await UsersDb.admin_checks()
        if admin_check == 1:
            await message.answer("Вы вошли в ЛК с возможностью администратора", reply_markup=admin_menu())

        else:
            await message.answer("Куда лезит этот новичок?\n "
                                 "Отказано в доступе админ панели")
