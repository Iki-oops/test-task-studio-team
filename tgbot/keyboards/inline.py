from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.callback_datas import command_callback_data

help_inline_keyboard = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Смотреть команды',
                callback_data=command_callback_data.new(key='help')
            )
        ]
    ]
)
