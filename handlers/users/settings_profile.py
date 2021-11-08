from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from data.config import amount
from keyboards.inline.payments import payments, settings_acc
from loader import dp, UsersDb
from utils.misc.payments import qiwi_check

@dp.message_handler(text="Настроить аккаунт")
async def settings(message: types.Message):
    name = await UsersDb.name(message.chat.id)
    number = await UsersDb.number(message.chat.id)
    await message.answer(f"Ваше имя: {name}\n"
                         f"Ваш номер телефона: {number}", reply_markup=settings_acc())

