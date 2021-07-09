from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.main_menu_keyboard import main_menu
from loader import dp, RegistrationStates, UsersDb


@dp.message_handler(state=RegistrationStates.enter_captcha)
async def check_subscribe_to_all_channels(message: types.Message, state:  FSMContext):
    data = await state.get_data()
    captcha = data.get('captcha')
    try:
        number = int(message.text)
    except ValueError:
        await message.answer(f"Пожалуйста, введите число {captcha}")
        return
    if number == captcha:
        await UsersDb.register_user(message.from_user.id)
        await message.answer("Добро пожаловать в бота",
                             reply_markup=main_menu())
        await state.finish()
    else:
        await message.answer("Вы ввели неправильный код")
