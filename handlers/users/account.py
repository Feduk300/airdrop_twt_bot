from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.deep_linking import get_start_link

from data.config import check_channel
from keyboards.default.account_keyboard import acc_kb
from keyboards.default.main_menu_keyboard import main_menu
from loader import dp, RegistrationStates, UsersDb


@dp.message_handler(text="Заработать TWT")
async def account(message: types.Message):
    link = await get_start_link(message.chat.id)
    await message.answer(f"Приглашайте друзей! За каждого приглашённого друга вы получите 0.06 TWT.\n"
                         f"Ваша реферальная ссылка: {link}\n"
                         "Ваш баланс: 0.048 TWT\n"
                         "Вы пригласили: 0",
                         reply_markup=acc_kb())

