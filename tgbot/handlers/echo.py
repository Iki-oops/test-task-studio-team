from aiogram import types, Dispatcher

from tgbot.models.db_commands import add_message


async def bot_echo(message: types.Message):
    await add_message(
        message_id=message.message_id,
        message_text=message.text,
        telegram_id=message.from_user.id,
        command='/not command'
    )


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo, state='*')
