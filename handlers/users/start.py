from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.main_menu_keyboard import main_menu
from keyboards.inline.new_acc_inl import new_acc_kb
from loader import dp, RegistrationStates, UsersDb
from utils.misc import gen_captcha


@dp.message_handler(CommandStart())
@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):
    if await UsersDb.user_exists(message.from_user.id):
        await message.answer(f"Главное меню",
                             reply_markup=main_menu())
    else:
        await message.answer("Подпишитесь на каналы указанные снизу. Нажмите проверка.",
                             reply_markup=new_acc_kb())

