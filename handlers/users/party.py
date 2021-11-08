from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(text="Ближайшая туса")
async def info(message: types.Message):
    await message.answer("Тут будет информация")