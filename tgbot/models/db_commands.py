from asgiref.sync import sync_to_async
from django.db import IntegrityError

from tgdjango.app.models import Profile, Response, Message, MessageResponse


@sync_to_async
def get_or_create_profile(telegram_id, username=None,
                          first_name=None, last_name=None,
                          avatar_url=None,):
    try:
        profile = Profile.objects.create(
            telegram_id=telegram_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            avatar_url=avatar_url,
        )
        return profile
    except IntegrityError as err:
        print(err)
        return Profile.objects.get(telegram_id=telegram_id)


@sync_to_async
def get_profile(telegram_id):
    return Profile.objects.filter(telegram_id=telegram_id).first()


@sync_to_async
def add_message(message_id: int,
                message_text: str,
                telegram_id: int,
                command: str | None = None):
    try:
        profile = Profile.objects.get(telegram_id=telegram_id)
        message = Message.objects.create(
            message_id=message_id,
            command=command,
            text=message_text,
            from_user=profile
        )

        return MessageResponse.objects.create(message=message, response=None)
    except IntegrityError as err:
        print(err)



@sync_to_async
def add_message_response(message_id: int,
                         message_text: str,
                         response_text: str,
                         photo_url: str | None,
                         telegram_id: int,
                         command: str | None = None):
    try:
        profile = Profile.objects.get(telegram_id=telegram_id)
        message = Message.objects.create(
            message_id=message_id,
            command=command,
            text=message_text,
            from_user=profile
        )

        response = Response.objects.create(
            message_id=message_id, text=response_text, photo_url=photo_url
        )
        return MessageResponse.objects.create(message=message, response=response)
    except IntegrityError as err:
        print(err)
