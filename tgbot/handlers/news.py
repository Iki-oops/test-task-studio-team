from aiogram import Dispatcher
from aiogram.types import Message


async def news(message: Message):

    return await message.answer('Новости')


def register_news(dp: Dispatcher):
    dp.register_message_handler(news, commands=['news'])
