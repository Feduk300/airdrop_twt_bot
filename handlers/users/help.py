from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку")
    
    await message.answer("\n".join(text))

@dp.message_handler(text="Контакты")
async def contacts(message: types.Message):
    await message.answer("Есть1")

@dp.message_handler(text="Раздачи")
async def distribution(message: types.Message):
    await message.answer("Есть2")

@dp.message_handler(text="Статистика")
async def distribution(message: types.Message):
    await message.answer("Есть3")