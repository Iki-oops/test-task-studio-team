from io import BytesIO
from pathlib import Path

from aiogram import Dispatcher
from aiogram.types import Message, InputFile

from tgbot.misc import generate_weather_image
from tgbot.services.aiohttp_service import AiohttpService
from tgbot.services.exceptions import WeatherAPIError


async def weather(message: Message, service: AiohttpService):
    city = message.get_args()
    token = message.bot.get('config').misc.weather_token
    try:
        data = await service.get_weather(city, token)
        root = Path().resolve()
        path = Path(root, 'static/images/background.jpg')
        photo = generate_weather_image(str(path), data)
        caption = f'Сейчас {data.get("weather")}. Температура: {data.get("temp")}.'

        return await message.answer_photo(photo, caption=caption)
    except WeatherAPIError:
        return await message.answer('Не нашел такого города')
    except KeyError:
        return await message.answer('Что-то пошло не так')


def register_weather(dp: Dispatcher):
    dp.register_message_handler(weather, commands=['weather'])

