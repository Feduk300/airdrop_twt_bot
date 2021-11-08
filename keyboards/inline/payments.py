from aiogram import types

from data.config import amount
from utils.misc.payments import QIWI_LOGIN

def payments(user_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Проверить оплату", callback_data="payments"))
    url = f"https://qiwi.com/payment/form/99?extra%5B%27account%27%5D={QIWI_LOGIN}&amount={amount}Fraction=0&extra%5B%27comment%27%5D={user_id}&currency=643&blocked[0]=account&blocked[2]=comment"
    keyboard.add(types.InlineKeyboardButton(text="Оплатить", url=url))
    return keyboard

def settings_acc():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.insert(types.InlineKeyboardButton(text="Сменить номер телефона", callback_data="number_edit"))
    keyboard.insert(types.InlineKeyboardButton(text="Сменить ФИО", callback_data="full_names"))
    keyboard.insert(types.InlineKeyboardButton(text="Закрыть меню", callback_data="but3"))
    return keyboard

def cancel():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Отменить", callback_data="cancel"))
    return keyboard