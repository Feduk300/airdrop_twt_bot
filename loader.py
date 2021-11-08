from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from states import *
from data import config
from utils.db_api.database import UsersDb


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML,)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
