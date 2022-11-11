from aiogram import types

from loader import dp, bot


@dp.message_handler()
async def random(message: types.Message):
    await message.answer("Не знаю,что тебе ответить...")
    fractal = (
        ['https://cdn.fishki.net/upload/post/2016/04/17/1922148/9d6982da865449d908c62499a80f3a72.jpg',
         'Множество Мандельброта — классический образец фрактала'],
        ['https://cdn.fishki.net/upload/post/2016/04/17/1922148/a742308912741c771000cc9b31126503.jpg',
         'Фрактальная форма кочана капусты сорта Романеско (Brassica oleracea)'],
        ['https://cdn.fishki.net/upload/post/2016/04/17/1922148/47efda49357bd45c11af303456972985.jpg',
         'Множество Жюлиа'],
        ['https://cdn.fishki.net/upload/post/2016/04/17/1922148/46245841e9195a8a5682fdce3f851b8d.jpg',
         'Фрактал, созданный с помощью программы Apophysis'],
        ['https://cdn.fishki.net/upload/post/2016/04/17/1922148/98119dced21833f5006bedd3c9406387.png',
         'Фрактал, созданный с помощью программы XaoS'],
        ['https://cdn.fishki.net/upload/post/2016/04/17/1922148/ca404c85e6a624e585792a20ed30c291.png',
         'Фрактал "Вязаные кружева"'],
        ['https://cdn.fishki.net/upload/post/2016/04/17/1922148/4db932e1b8597067ecd8e5a0a689d60a.png',
         'Бассейны Ньютона для полинома пятой степени'],
        ['https://cdn.fishki.net/upload/post/2016/04/17/1922148/300df4ad9d3b8b10d721abece8bb8e3a.png',
         'дерево Пифагора'],
        ['https://cdn.fishki.net/upload/post/2016/04/17/1922148/a8bdaa9f9c4c39bf36558f7714310910.jpg',
         'Эффектные «Фаберже фракталы» Тома Беддарда (Tom Beddard)'],
        ['https://cdn.fishki.net/upload/post/2016/04/17/1922148/dcbe0c5edabcb04b38163dadb5db7e55.jpg',
         'Фракталы в 3D-графике']
    )
    random_fractal = dict(enumerate(fractal, start=1))

    import random
    value = random.randint(1, len(fractal))
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=random_fractal[value][0],
                         caption=random_fractal[value][1])
