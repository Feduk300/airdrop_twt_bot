from aiogram import types


def main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton(text="Заработать TWT"))
    keyboard.insert(types.KeyboardButton(text="Получить TWT"))
    keyboard.insert(types.KeyboardButton(text="Раздачи"))
    keyboard.insert(types.KeyboardButton(text="Статистика"))
    keyboard.insert(types.KeyboardButton(text="Контакты"))
    keyboard.insert(types.KeyboardButton(text="Реклама"))
    return keyboard