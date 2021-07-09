from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.main_menu_keyboard import main_menu
from loader import dp, RegistrationStates, UsersDb
from utils.misc import gen_captcha


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    if await UsersDb.user_exists(message.from_user.id):
        await message.answer(f"Главное меню",
                             reply_markup=main_menu())
    else:
        captcha = gen_captcha()
        await state.update_data(captcha=captcha)
        await message.answer(f"Введите число {captcha} для регистрации")
        await RegistrationStates.enter_captcha.set()
