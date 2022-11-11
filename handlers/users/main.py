from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.markdown import hitalic, hlink, link

from data import section_of_mathematics
from keyboards.default.menu_start import menu_start1, menu_start2, \
    main_keyboard, fractal_photo, back_to_main_menu, section_of_mathematics_topic
from keyboards.inline.choice_buttons import fractal_keyboard, fractal_items
from loader import dp, bot
from states.test import MenuStart


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    service_message = await message.answer("Немного подождите⌛")
    await service_message.delete()
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEGYO1jbXRVV7LOORKFerTTcuBqLIm2yQACIgADTlzSKWF0vv5zFvwUKwQ")
    await message.answer("Приветствую тебя дорогой друг,ты попал в удивительного бота...\n"
                         "Для интересного изучения материала нажмите на стопку книг", reply_markup=menu_start1)
    await MenuStart.Q1.set()


@dp.message_handler(Text("\U0001F4DA"), state=MenuStart.Q1)
async def menu(message: types.Message):
    await message.answer("Выбирай свой дисциплину", reply_markup=menu_start2)
    await MenuStart.Q2.set()


@dp.message_handler(Text("Математика"), state=MenuStart.Q2)
async def menu(message: types.Message, state: FSMContext):
    await message.answer('Выберите тему',reply_markup=section_of_mathematics_topic())
    await MenuStart.topic_selection.set()


# Оптимизировать код
@dp.message_handler(Text(section_of_mathematics[1]['topic']),state=MenuStart.topic_selection)
async def selection_topic_info(message: types.Message):
    await message.reply('Данная тема в находиться в разработке')


@dp.message_handler(Text(section_of_mathematics[2]['topic']),state=MenuStart.topic_selection)
async def selection_topic_tack(message: types.Message):
    await message.reply('Данная тема в находиться в разработке')


@dp.message_handler(Text(section_of_mathematics[3]['topic']),state=MenuStart.topic_selection)
async def selection_topic_math_game(message: types.Message):
    await message.reply('Данная тема в находиться в разработке')


@dp.message_handler(Text(section_of_mathematics[4]['topic']),state=MenuStart.topic_selection)
async def selection_topic_fleri(message: types.Message):
    await message.reply('Данная тема в находиться в разработке')


@dp.message_handler(Text(section_of_mathematics[5]['topic']),state=MenuStart.topic_selection)
async def selection_topic_shifr(message: types.Message):
    await message.reply('Данная тема в находиться в разработке')


@dp.message_handler(Text(section_of_mathematics[6]['topic']),state=MenuStart.topic_selection)
async def selection_topic_number(message: types.Message):
    await message.reply('Данная тема в находиться в разработке')


@dp.message_handler(Text(section_of_mathematics[7]['topic']),state=MenuStart.topic_selection)
async def selection_topic_potok(message: types.Message):
    await message.reply('Данная тема в находиться в разработке')


@dp.message_handler(Text(section_of_mathematics[8]['topic']),state=MenuStart.topic_selection)
async def selection_topic_music(message: types.Message):
    await message.reply('Данная тема в находиться в разработке')


@dp.message_handler(Text(section_of_mathematics[9]['topic']),state=MenuStart.topic_selection)
async def selection_topic_counting_uncountable(message: types.Message):
    await message.reply('Данная тема в находиться в разработке')


@dp.message_handler(Text(section_of_mathematics[10]['topic']),state=MenuStart.topic_selection)
async def selection_topic_problem(message: types.Message):
    await message.reply('Данная тема в находиться в разработке')


@dp.message_handler(Text(section_of_mathematics[0]['topic']),state=MenuStart.topic_selection)
async def selection_topic_fractal(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if not data:
        await message.answer("Пока из имеющихся тем только фракталы.\n"
                             "Ознакомься с теорией данного курса\n"
                             "В каждой теме своя порция теории ;)", reply_markup=main_keyboard(0))
        await message.answer_video(open('selfedu/screen/теория.gif_', 'rb'))
    else:
        await message.answer("Вы вышли в главное меню.\nВаши действия?", reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text='Продолжить'),
                    KeyboardButton(text='Сначала')
                ],
            ],
            resize_keyboard=True
        ))
    await MenuStart.Q3.set()


@dp.message_handler(Text("теория"), state='*')  # ,state=Menu.Q1)
async def theory_menu(message: types.Message, state: FSMContext):
    service_message = await message.answer("Немного подождите⌛")
    await service_message.delete()
    data = await state.get_data()
    data.setdefault('items', 0)
    await state.set_data(data)
    number = data['items']
    await message.answer(f"Сейчас мы изучаем тему - {fractal_items[number].get('тема')}",
                         reply_markup=fractal_keyboard(number))
    await MenuStart.Q5.set()


@dp.message_handler(Text('Сначала'), state=MenuStart.Q3)
async def warning(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data:
        data['items'] = 0
        await state.update_data(data)
        await message.answer("Для начала ознакомтесь с теорией :)", reply_markup=main_keyboard(data['items']))
    await MenuStart.Q4.set()


@dp.message_handler(state=MenuStart.Q3)
async def warning(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data:
        await message.answer("Для начала ознакомтесь с теорией :)", reply_markup=main_keyboard(data['items']))
    await MenuStart.Q4.set()


@dp.message_handler(Text("IT(в разработке)"), state=MenuStart.Q2)
async def menu(message: types.Message):
    await message.answer("По данной теме пока ничего нет")


@dp.message_handler(Text("Физика(в разработке)"), state=MenuStart.Q2)
async def menu(message: types.Message):
    await message.answer("По данной теме пока ничего нет")


# @dp.message_handler(Text("\U0001F30B"), state=Menu_start.Q4)
# async def start_fractal(message: types.Message):
#     service_message = await message.answer("Немного подождите⌛")
#     await service_message.delete()
#     await message.answer(text="...", reply_markup=main_keyboard(5))
#     # "Остальные разделы в процессе разработки,по мере поступления предложений список будет доробатываться", reply_markup=menu_main)
#     await Menu.Q1.set()


@dp.message_handler(Text('ГM'), state='*')
async def main_menu(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer("Ты попал в главное меню,выбирай своб дисциплину", reply_markup=menu_start2)
    # await message.answer("Ты попал в главное меню,выбирай своб дисциплину", reply_markup=main_keyboard(data['items']))
    await MenuStart.Q2.set()


# @dp.message_handler(Text("\U0001F30B"))
# async def start_fractal(message: types.Message):
#     service_message = await message.answer("Немного подождите⌛")
#     await service_message.delete()
#     await message.answer(text="Всё,обратно пути нет...", reply_markup=main_keyboard(0))
#     await Menu.Q1.set()


# class Forward_Back(StatesGroup):
#     q1 = State()
#     q2 = State()


@dp.message_handler(Text("назад"), state=MenuStart.Q5)
async def back(message: types.Message, state: FSMContext):
    data = await state.get_data()
    number = data.get("items")
    if number > 0:
        data['items'] = number - 1
        await state.update_data(data)
        await message.answer("Вы перешли к предыдущей теме!", reply_markup=main_keyboard(data['items']))
    else:
        await message.answer("Попробуй ещё раз!")


@dp.message_handler(Text("дальше"), state=MenuStart.Q5)
async def forward(message: types.Message, state: FSMContext):
    data = await state.get_data()
    number = data.get("items")
    if 0 <= number < 13:
        data['items'] = number + 1
        await state.update_data(data)
        await message.answer("Вы перешли к следующей теме!", reply_markup=main_keyboard(data['items']))
        if number == 12:
            text = hitalic(
                'Совутую\n') + '<a href="https://vk.com/public199200116?w=wall-199200116_4">Пост в котором прикрепил несколько полезных документов</a>\n' \
                               '<a href="https://www.youtube.com/watch?v=mnSKZyRFhIM&ab_channel=%D0%A1%D0%9C%D0%9E%D0%A2%D0%A0%D0%98%D0%9C%D0%BA%D0%B8%D0%BD%D0%BE%D0%B8%D1%81%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D1%8B">Интересный фильм</a>'
            await message.reply("Позравляю!Вы дошли до конца!\nЯ очень горжусь Вами")
            await bot.send_sticker(message.from_user.id,
                                   sticker="CAACAgIAAxkBAAEGYPFjbXaPh4eq1eQ2HbCJWjwTZND98wACugIAAs9fiwdwwz1RnDFRdCsE")
            await message.answer(text, parse_mode="HTML")
            await message.answer('Для дальшейшего обучения вернитесь в главное меню', reply_markup=back_to_main_menu)
            # await MenuStart.Q2.set()
    else:
        await message.answer("Попробуй ещё раз!")


@dp.message_handler(Text("✨"), state=MenuStart.Q5)
async def button(message: types.Message, state: FSMContext):
    service_message = await message.answer("Немного подождите⌛")
    await service_message.delete()
    data = await state.get_data()
    number = data['items']
    if fractal_items[number].get('photo'):
        await message.answer("Появились кнопки?", reply_markup=fractal_photo(number))
        await MenuStart.Q6.set()
    else:
        await message.answer("В разработке")


@dp.message_handler(state=MenuStart.Q6)
async def photo(message: types.Message, state: FSMContext):
    service_message = await message.answer("Немного подождите⌛")
    await service_message.delete()
    data = await state.get_data()
    number = data['items']
    answer = message.text
    if answer == 'назад':
        await message.answer("Вы вернулись обратно", reply_markup=main_keyboard(number))
        await MenuStart.Q5.set()
    elif answer == 'тык':
        await message.answer_photo(photo=fractal_items[number].get('photo')[answer])
    else:
        await message.answer_photo(open(fractal_items[number].get('photo')[answer], 'rb'), caption=hitalic(answer))
