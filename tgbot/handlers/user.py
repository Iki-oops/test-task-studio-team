from typing import Union

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.callback_datas import command_callback_data
from tgbot.keyboards.inline import help_inline_keyboard
from tgbot.misc import get_translited_username
from tgbot.models.db_commands import add_message_response


async def user_start(message: Message):
    username = message.from_user.username

    if message.from_user.full_name:
        username = message.from_user.full_name

    text = (f'Привет {get_translited_username(username)}!👋\n\n'
            f'Я - бот, и моя задача помогать тебе получать актуальную информацию.\n\n'
            f'Независимо от того, где ты находишься, я помогу тебе быть в курсе '
            f'погодных условий в любом городе мира.\n'
            f'Буду отправлять случайную новость из разных областей, '
            f'чтобы ты мог быть в курсе последних событий в мире.\n\n'
            f'Жми /help - чтобы узнать команды или на кнопку👇')

    await add_message_response(
        message_id=message.message_id,
        message_text=message.text,
        response_text=text,
        photo_url=None,
        telegram_id=message.from_user.id,
        command='/start'
    )

    return await message.answer(
        text=text,
        reply_markup=help_inline_keyboard
    )


async def user_help(update: Union[Message, CallbackQuery]):
    if isinstance(update, CallbackQuery):
        message_id = update.message.message_id
    else:
        message_id = update.message_id

    text = ('Вот все мои команды и их описания:\n\n'
            '  /start - Приветствую пользователя и рассказываю о своих функциях.\n'
            '  /help - Вывожу список доступных команд.\n'
            '  /weather [город] - Показываю текущую погоду в указанном городе.\n'
            '  /news - Отправляю пользователю случайную новость')

    await add_message_response(
        message_id=message_id,
        message_text='/help',
        response_text=text,
        photo_url=None,
        telegram_id=update.from_user.id,
        command='/help',
    )

    if isinstance(update, CallbackQuery):
        return await update.message.edit_text(text)

    return await update.answer(text)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=['start'], state='*')
    dp.register_message_handler(user_help, commands=['help'], state='*')
    dp.register_callback_query_handler(user_help, command_callback_data.filter(key='help'))
