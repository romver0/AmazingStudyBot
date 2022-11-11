import logging

from aiogram import Dispatcher

from data.config import BIG_ADMINS


async def on_startup_notify(dp:Dispatcher):
    for admin in BIG_ADMINS:
        try:
            await dp.bot.send_message(admin,"Хозяин бот запущен!")
        except Exception as err:
            logging.exception(err)