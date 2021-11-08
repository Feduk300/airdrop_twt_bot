from aiogram import types


def menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    keyboard.insert(types.KeyboardButton(text="Информация"))
    keyboard.insert(types.KeyboardButton(text="Ближайшая туса"))
    keyboard.insert(types.KeyboardButton(text="Оплата"))
    keyboard.insert(types.KeyboardButton(text="Настроить аккаунт"))
    return keyboard