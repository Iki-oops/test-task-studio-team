from typing import Union

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.callback_datas import command_callback_data
from tgbot.keyboards.inline import news_inline_keyboard
from tgbot.services.aiohttp_service import AiohttpService
from tgbot.services.exceptions import NewsAPIError, TooManyRequestsAPIError


async def get_news(update: Union[Message, CallbackQuery], service: AiohttpService):
    if isinstance(update, CallbackQuery):
        await update.answer()
        update = update.message

    token = update.bot.get('config').misc.news_token

    try:
        news = await service.get_news(token)
        caption = (f'Автор: <code>worldnewsapi</code>🥸\n'
                   f'Дата публикации: <b>{news.publish_date}</b>⏰\n\n'
                   f'<b>{news.title}</b>📰\n\n'
                   f'{news.text}\n\n'
                   f'Ссылка на статью📬: {news.url}')

        return await update.answer_photo(
            photo=news.image,
            caption=caption,
            reply_markup=news_inline_keyboard,
        )
    except NewsAPIError:
        return await update.answer('Не нашел новость')
    except TooManyRequestsAPIError:
        return await update.answer('Вы превысили лимит запросов.')
    except Exception:
        return await update.answer('Что-то пошло не так')


def register_news(dp: Dispatcher):
    dp.register_message_handler(get_news, commands=['news'])
    dp.register_callback_query_handler(get_news, command_callback_data.filter(key='news'))
