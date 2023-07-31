from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from tgbot.models.db_commands import (
    get_or_create_profile, get_profile,
)


class UsersManagerMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        user = await get_profile(message.from_user.id)

        if not user:
            avatar_url = await message.from_user.get_profile_photos(0, 1)
            avatar_url = avatar_url.photos[0][-1]

            avatar_url = await data['service'].upload_photo(avatar_url)

            user = await get_or_create_profile(
                message.from_user.id,
                message.from_user.username,
                message.from_user.first_name,
                message.from_user.last_name,
                avatar_url,
            )

        data['user'] = user
