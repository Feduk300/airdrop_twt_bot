from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import check_channel
from keyboards.default.account_keyboard import admin_menu
from keyboards.default.main_menu_keyboard import main_menu, dop_menuadm

from loader import dp, RegistrationStates, UsersDb


@dp.message_handler(text="Информация")
async def information(message: types.Message):
    admin_check = await UsersDb.admin_checks()
    if admin_check != 0:
        await message.answer("Выберите пункт.", reply_markup = dop_menuadm())
    else:
        await message.answer("Выберите пункт.", reply_markup = main_menu())