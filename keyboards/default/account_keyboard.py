from aiogram import types


def menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    keyboard.insert(types.KeyboardButton(text="Информация"))
    keyboard.insert(types.KeyboardButton(text="Ближайшее пати"))
    keyboard.insert(types.KeyboardButton(text="Оплата"))
    keyboard.insert(types.KeyboardButton(text="Настроить аккаунт"))
    return keyboard
def admin_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    keyboard.insert(types.KeyboardButton(text="Информация"))
    keyboard.insert(types.KeyboardButton(text="Ближайшее пати"))
    keyboard.insert(types.KeyboardButton(text="Оплата"))
    keyboard.insert(types.KeyboardButton(text="Настроить аккаунт"))
    keyboard.insert(types.KeyboardButton(text="Панель администратора"))
    return keyboard

def admin_panel():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    keyboard.insert(types.KeyboardButton(text="Пользователи, которые заплатили"))
    keyboard.insert(types.KeyboardButton(text="Все пользователи"))
    keyboard.insert(types.KeyboardButton(text="Назад в ЛК"))
    return keyboard
