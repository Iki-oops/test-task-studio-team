from typing import Dict, Any

from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from aiogram.types.base import TelegramObject


class IntegrationMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ['update', 'error']

    def __init__(self, service):
        super().__init__()
        self._service = service

    async def pre_process(self, obj: TelegramObject,
                          data: Dict[Any, Any],
                          *args: Any):
        data['service'] = self._service
