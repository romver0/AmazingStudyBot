from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

lecture1_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='\U0001F4C3', url="https://proproprogs.ru/fractals/krivaya-koha-i-snezhinka-koha")
        ]
    ])

lecture2_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='\U0001F4C3',
                                 url="https://proproprogs.ru/fractals/fractals-risuem-krivuyu-koha-i-snezhinku-koha")
        ]
    ])

items = [
    {
        "foreground": "black",
        "background": "azure",
        "item_id": 1
    },
    {
        "foreground": "green",
        "background": "black",
        "item_id": 2
    },
    {
        "foreground": "cyan",
        "background": "black",
        "item_id": 3
    },
    {
        "foreground": "DarkOrange",
        "background": "black",
        "item_id": 4
    },
    {
        "foreground": "DarkOrchid",
        "background": "black",
        "item_id": 5
    },
]
fractal_items = [
    {
        "тема": "Кривая Коха и снежинка Коха",
        "ссылка": "https://proproprogs.ru/fractals/krivaya-koha-i-snezhinka-koha",
        "item_id": 1,
        "photo": {"тык":"https://64.media.tumblr.com/628fb444ea7cd2aa212f6a6c06e7e0a9/cc16a328d920a410-65/s540x810/beaea96bce7eb4ab9a9bca57f0b8841da36137e2.jpg"}

    },
    {
        "тема": "Рисуем кривую Коха и снежинку Коха",
        "ссылка": "https://proproprogs.ru/fractals/fractals-risuem-krivuyu-koha-i-snezhinku-koha",
        "item_id": 2,
        "photo": {'снежинка Коха': 'selfedu/screen/2_2.png', 'снежинка Коха(обратная)': 'selfedu/screen/2_1.png'}
    },
    {
        "тема": "Простая L-система на плоскости",
        "ссылка": "https://proproprogs.ru/fractals/fractals-prostaya-l-sistema-na-ploskosti",
        "item_id": 3,
        "photo": {"сюрикен :)": "selfedu/screen/3_1.png", "ковёр :)": "selfedu/screen/3_2.png"}
    },
    {
        "тема": "L-система для дракона...",
        "ссылка": "https://proproprogs.ru/fractals/l-sistema-dlya-drakona-hartera-haytveya-kovra-serpinskogo-i-krivoy-gilberta",
        "item_id": 4,
        "photo": {"дракон Хартера-Хатвея": "selfedu/screen/4_1.png", "квадратик :)": "selfedu/screen/4_3.png",
                  "Треугольник Серпинского": "selfedu/screen/4_2.png"}

    },
    {
        "тема": "L-система с ветвлениями...",
        "ссылка": "https://proproprogs.ru/fractals/fractals-l-sistema-s-vetvleniyami-risuem-derevya-i-travy",
        "item_id": 5,
        "photo": {"дерево №1": "selfedu/screen/5_1.png", "дерево №2": "selfedu/screen/5_2.png",
                  "дерево №3": "selfedu/screen/5_3.png", "дерево №4": "selfedu/screen/5_4.png"}
    },
    {
        "тема": "Добавляем параметры в L-систему...",
        "ссылка": "https://proproprogs.ru/fractals/fractals-dobavlyaem-parametry-v-l-sistemu",
        "item_id": 6
    },
    {
        "тема": "Добавляем случайности в L-систему",
        "ссылка": "https://proproprogs.ru/fractals/fractals-dobavlyaem-sluchaynosti-v-l-sistemu",
        "item_id": 7
    },
    {
        "тема": "Добавляем цвет в L-систему",
        "ссылка": "https://proproprogs.ru/fractals/fractals-dobavlyaem-cvet-v-l-sistemu",
        "item_id": 8
    },
    {
        "тема": "Как вычисляется фрактальная размерность...",
        "ссылка": "https://proproprogs.ru/fractals/fractals-kak-vychislyaetsya-fraktalnaya-razmernost-po-hausdorfu",
        "item_id": 9
    },
    {
        "тема": "Системы итерированных функций СИФ",
        "ссылка": "https://proproprogs.ru/fractals/fractals-sistemy-iterirovannyh-funkciy-sif",
        "item_id": 10
    },
    {
        "тема": "Рандомизированная система итерированных функций",
        "ссылка": "https://proproprogs.ru/fractals/fractals-randomizirovannaya-sistema-iterirovannyh-funkciy",
        "item_id": 11
    },
    {
        "тема": "Примеры фракталов, сгенерированных СИФ",
        "ссылка": "https://proproprogs.ru/fractals/fractals-primery-fraktalov-sgenerirovannyh-sif",
        "item_id": 12
    },
    {
        "тема": "Как построить множества Жюлиа",
        "ссылка": "https://proproprogs.ru/fractals/fractals-kak-postroit-mnozhestva-zhyulia",
        "item_id": 13
    },
    {
        "тема": "Рисуем множество Мандельброта",
        "ссылка": "https://proproprogs.ru/fractals/fractals-risuem-mnozhestvo-mandelbrota",
        "item_id": 14
    }
]
fractal_callback = CallbackData("fractal", "category", "foreground", "background", "item_id")
fractal = CallbackData("fractals", "item_id")


# def create_keyboard():
#     keyboard = InlineKeyboardMarkup()
#     for item in items:
#         keyboard.insert(
#             InlineKeyboardButton(
#                 text=f"{item.get('foreground')} | {item.get('background')}",
#                 # text="...",
#                 callback_data=fractal_callback.new(category="color", foreground=item.get('foreground'),
#                                                    background=item.get('background'), item_id=item.get("item_id"))
#             )
#         )
#     return keyboard

# def create_keyboard(value):
#     keyboard = InlineKeyboardMarkup()
#     # for item in items:
#     print(items[value])
#     keyboard.insert(
#         InlineKeyboardButton(
#             text=f"{items[value].get('foreground')} | {items[value].get('background')}",
#             # text="...",
#             callback_data=fractal_callback.new(category="color", foreground=items[value].get('foreground'),
#                                                background=items[value].get('background'),
#                                                item_id=items[value].get("item_id"))
#         )
#
#     )
#     return keyboard


def fractal_keyboard(number):
    # print(fractal_items[1].get('тема'))
    keyboard = InlineKeyboardMarkup()
    keyboard.insert(
        InlineKeyboardButton(
            text=f"{fractal_items[number].get('тема')}",
            url=f"{fractal_items[number].get('ссылка')}",
            callback_data=fractal.new(item_id=fractal_items[number].get('item_id'))
        )
    )
    return keyboard
