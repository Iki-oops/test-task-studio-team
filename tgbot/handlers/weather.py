from pathlib import Path

from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.misc import generate_weather_image
from tgbot.models.db_commands import add_message_response
from tgbot.services.aiohttp_service import AiohttpService
from tgbot.services.exceptions import WeatherAPIError, TooManyRequestsAPIError


async def get_weather(message: Message, service: AiohttpService):
    city = message.get_args()
    token = message.bot.get('config').misc.weather_token

    try:
        root = Path().resolve()
        path = Path(root, 'static/images/background.jpg')
        data = await service.get_weather(city, token)

        photo = generate_weather_image(str(path), data)
        caption = (f'Сейчас в городе {data.city} {data.weather}.\n'
                   f'Температура: {data.temp}. Время в городе: {data.time}')

        photo = await service.upload_photo(photo)

        await add_message_response(
            message.message_id,
            message.text,
            caption,
            photo,
            message.from_user.id,
            '/weather',
        )

        return await message.answer_photo(photo, caption=caption)
    except WeatherAPIError:
        return await message.answer('Не нашел такого города')
    except TooManyRequestsAPIError:
        return await message.answer('Вы превысили лимит запросов.')
    except Exception as err:
        print(err)
        return await message.answer('Что-то пошло не так')


def register_weather(dp: Dispatcher):
    dp.register_message_handler(get_weather, commands=['weather'])

