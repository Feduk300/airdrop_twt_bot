from aiogram import types


def main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.insert(types.KeyboardButton(text="Написать в саппорт"))
    keyboard.insert(types.KeyboardButton(text="Правила мероприятия"))
    keyboard.insert(types.KeyboardButton(text="Главное меню"))
    return keyboard