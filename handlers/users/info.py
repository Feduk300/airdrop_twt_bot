from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import check_channel
from keyboards.default.main_menu_keyboard import main_menu

from loader import dp, RegistrationStates, UsersDb


@dp.message_handler(text="Информация")
async def information(message: types.Message):
    await message.answer("Выберите пункт.", reply_markup = main_menu())