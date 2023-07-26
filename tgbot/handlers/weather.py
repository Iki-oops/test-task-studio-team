from aiogram import Dispatcher
from aiogram.types import Message


async def weather(message: Message):

    return await message.answer('Погода')


def register_weather(dp: Dispatcher):
    dp.register_message_handler(weather, commands=['weather'])

