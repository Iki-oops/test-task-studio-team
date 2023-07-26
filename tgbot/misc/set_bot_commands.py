from aiogram import types, Dispatcher


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Запустить бота'),
            types.BotCommand('help', 'Выводит список доступных команд.'),
            types.BotCommand('weather', 'Показывает текущую погоду в указанном городе.'),
            types.BotCommand('news', 'Отправляет пользователю случайную новость.'),
        ]
    )
