from aiogram import types


def acc_kb():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton(text="Вывести TWT"))
    keyboard.add(types.KeyboardButton(text="Назад"))
    return keyboard