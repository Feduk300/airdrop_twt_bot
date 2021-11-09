from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import check_channel

from loader import dp, RegistrationStates, UsersDb

@dp.message_handler(commands="admcommand")
async def admins(message: types.Message):
    names = await UsersDb.users(message.chat.id)

    text="Пользователи, которые заплатили:"
    for tab in names:
        text += f"\n {tab[4]}"
    await message.answer(text)


