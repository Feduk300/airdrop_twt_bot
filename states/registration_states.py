from aiogram.dispatcher.filters.state import State, StatesGroup



class RegistrationStates(StatesGroup):
    name = State()
    number = State()
    name_edites = State()
    number_edites = State()
    numberprocess = State()
    nameprocess = State()
    Text = State()