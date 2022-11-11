from aiogram.dispatcher.filters.state import StatesGroup, State


class MenuStart(StatesGroup):
    Q1 = State()
    Q2 = State()
    topic_selection = State()
    Q3 = State()
    Q4 = State()
    Q5 = State()
    Q6 = State()


class Menu(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()
    Q5 = State()
    Q6 = State()


class Sticker(StatesGroup):
    Q1 = State()
