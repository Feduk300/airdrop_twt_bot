from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.main_menu_keyboard import main_menu
from keyboards.inline.payments import cancel
from loader import dp, RegistrationStates, UsersDb


@dp.callback_query_handler(text="number_edit") #ввод номера
async def number_edit(call: types.CallbackQuery):
    await call.message.edit_text("Введите ваш новый номер", reply_markup=cancel())
    await RegistrationStates.numberprocess.set()

@dp.callback_query_handler(text="cancel",state=RegistrationStates.numberprocess) #отмена номер
async def cancel_button(call: types.CallbackQuery, state:FSMContext):
    await call.message.delete()
    await state.finish()

@dp.message_handler(state=RegistrationStates.numberprocess) #БД смена номера
async def names_process(message: types.Message, state:FSMContext):
    answer = message.text
    await message.answer("✅")
    await UsersDb.numberprocess(answer, message.chat.id)
    await state.finish()



@dp.callback_query_handler(text="full_names") #ФИО ввод
async def names_edite(call: types.CallbackQuery):
    await call.message.edit_text("Введите ваше ФИО", reply_markup=cancel())
    await RegistrationStates.name_edites.set()


@dp.callback_query_handler(text="cancel",state=RegistrationStates.name_edites) #отмена смены ФИО
async def cancel_button(call: types.CallbackQuery, state:FSMContext):
    await call.message.delete()
    await state.finish()

@dp.message_handler(state=RegistrationStates.name_edites) #БД смена ФИО
async def names_process(message: types.Message, state:FSMContext):
    answer = message.text
    await message.answer("✅")
    await UsersDb.fullnameprocess(answer, message.chat.id)
    await state.finish()



@dp.callback_query_handler(text="but3")
async def close(call: types.CallbackQuery):
    await call.message.delete()
