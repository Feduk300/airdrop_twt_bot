from aiogram import types


def new_acc_kb():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Проверить подписку", callback_data="subscribed"))
    keyboard.add(types.InlineKeyboardButton(text="Подписаться", url="https://t.me/chakchak1111"))
    return keyboard
