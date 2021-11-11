from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from data.config import amount
from keyboards.inline.payments import payments
from loader import dp, UsersDb
from utils.misc.payments import qiwi_check



@dp.message_handler(text="Оплата")
async def check_payeds(message: types.Message):
    check_payeds = await UsersDb.check_pay()
    if check_payeds < 100:
            await message.answer(f"Нажмите на кнопку оплаты\n"
                                     f"После перевода денег проверьте оплату\n"
                                     f"Сумма к оплате: {amount} Руб.\n"
                                     f"После успешной оплаты зайдите в Информация → Написасть в саппорт"
                                     f"И напишите коментарий который был у платежа.", reply_markup=payments(message.chat.id))
    else:
                await message.answer("Мест больше нет")

@dp.callback_query_handler(text="payments")
async def payments_check(call: types.CallbackQuery):
   if qiwi_check(call.message.chat.id, amount):
        await UsersDb.successfull(call.message.chat.id)
        await call.message.edit_text(f"✅ Оплата прошла успешна. Отправьте в саппорт: {call.message.chat.id}")
   else:
        await call.answer("❌ Оплата не найдена")
