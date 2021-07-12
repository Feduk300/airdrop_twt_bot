from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import check_channel
from keyboards.default.main_menu_keyboard import main_menu
from loader import dp, RegistrationStates, UsersDb


@dp.callback_query_handler(text="subscribed")
async def back_cart(call: types.CallbackQuery):
    chat_mamber = await dp.bot.get_chat_member(check_channel[0], call.message.chat.id)
    print(chat_mamber.status)
    if chat_mamber.status == "member" or "creator":
        await UsersDb.register_user(call.message.chat.id)
        await call.message.delete()
        await call.message.answer("Подписались",
                             reply_markup=main_menu())

    else:
        await call.answer("Вы не подписались на канал")

