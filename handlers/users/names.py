from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import check_channel

from loader import dp, RegistrationStates, UsersDb


num = 0

@dp.message_handler(text="Пользователи, которые заплатили")
async def admins(message: types.Message):
    admin_check= await UsersDb.admin_checks(message.chat.id)
    if admin_check == 1:
        names = await UsersDb.users(message.chat.id)
        text="Пользователи, которые заплатили:"
        for tab in names:
            text += f"\n {tab[4]}"
        await message.answer(text)
    else:
        await message.answer("Отказано")

@dp.message_handler(text="Все пользователи")
async def adminsus(message: types.Message):
    admin_check= await UsersDb.admin_checks(message.chat.id)
    if admin_check == 1:
        names = await UsersDb.users(message.chat.id)
        admusers = await UsersDb.allusersbots(message.chat.id)

        text= f"Пользователи, которые зарегестрировались:"
        for tab,nums in admusers,num:
                text += f"\n.{num}.{tab[4]}"
        await message.answer(text)
    else:
        await message.answer("Отказано")



