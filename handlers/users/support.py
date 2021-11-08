from aiogram import types
from aiogram.dispatcher import FSMContext


from keyboards.default.main_menu_keyboard import main_menu
from keyboards.inline.payments import cancel
from loader import dp, RegistrationStates, UsersDb

@dp.message_handler(text="Написать в саппорт")
async def mailing(message: types.Message):
    await message.answer(text="Пришлите текст вашей проблемы")
    await RegistrationStates.Text.set()


@dp.message_handler(state=RegistrationStates.Text)
async def mailing_start(message: types.Message , state: FSMContext):
    text = message.text
    data = message.from_user.id
    msgbox = (f"<a href='tg://user?id={data}'>Пользователь</a>")
    await state.update_data(text=text)
    await state.reset_state()
    await dp.bot.send_message(chat_id=1015467578,
                                   text=f"#supticket\n{text}\n{msgbox}")