from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data import section_of_mathematics
from keyboards.inline.choice_buttons import fractal_items

menu_start1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            # KeyboardButton(text='\U0001F30B') # вулкан
            KeyboardButton(text='\U0001F4DA')
        ]
    ],
    resize_keyboard=True
)
menu_start2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            # KeyboardButton(text='\U0001F30B') # вулкан
            KeyboardButton(text='Математика'),
            KeyboardButton(text='Физика(в разработке)'),
            KeyboardButton(text='IT(в разработке)')
        ]
    ],
    resize_keyboard=True
)

menu_ = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='\U0001F30B')  # вулкан
        ]
    ],
    resize_keyboard=True
)
back_to_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='ГM')
        ]
    ],
    resize_keyboard=True
)


def main_keyboard(number):
    menu_main = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='назад'),
                KeyboardButton(text='теория'),
                KeyboardButton(text='✨'),
                KeyboardButton(text='дальше')
            ],
            [
                KeyboardButton(text="ГM"),
                KeyboardButton(text=f"тема:{fractal_items[number].get('тема')}")
            ]
        ],
        resize_keyboard=True
    )
    return menu_main


def section_of_mathematics_topic():
    size = len(section_of_mathematics)
    menu_topic = ReplyKeyboardMarkup(resize_keyboard=True)
    for number in range(size):
        topic = section_of_mathematics[number].get('topic')
        if topic:
            menu_topic.insert(
                KeyboardButton(text=topic)
            )
    return menu_topic


def fractal_photo(number):
    menu_fractal_photo = ReplyKeyboardMarkup(resize_keyboard=True)
    if fractal_items[number].get('photo'):
        for item in fractal_items[number].get('photo'):
            menu_fractal_photo.insert(
                KeyboardButton(text=item),
            )
        menu_fractal_photo.insert(KeyboardButton(text='назад'))

    return menu_fractal_photo
