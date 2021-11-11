from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.deep_linking import get_start_link
from loader import dp, RegistrationStates, UsersDb
from aiogram import types
from keyboards.default.account_keyboard import menu
from loader import dp, RegistrationStates, UsersDb

@dp.message_handler(text="Главное меню")
@dp.message_handler(CommandStart())
async def menu_main(message: types.Message):
    if await UsersDb.user_exists(message.chat.id):
        await message.answer(f"Добро пожаловать на хорошую вечеринку",
                             reply_markup=menu())
        print(message)
    else:
        await RegistrationStates.name.set()
        await message.answer("Введите ваш ФИО:")

@dp.message_handler(state=RegistrationStates.name)
async def full_name(message: types.Message, state:FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer("Ваш мобильный номер:")
    await RegistrationStates.number.set()

@dp.message_handler(state=RegistrationStates.number)
async def number(message: types.Message, state:FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answers = message.text
    await message.answer("✅",reply_markup=menu())
    await UsersDb.register_user(message.chat.id)
    await UsersDb.fullnameprocess(answer1, message.chat.id)
    await UsersDb.numberprocess(answers, message.chat.id)
    await state.finish()

