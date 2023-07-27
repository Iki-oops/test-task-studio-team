import datetime as dt
from typing import Optional

import aiohttp

from tgbot.services.config import BASE_WEATHER_API_LINK
from tgbot.services.exceptions import WeatherAPIError


class AiohttpService:
    def __init__(self):
        self._session: Optional[aiohttp.ClientSession] = None

    async def get_weather(self, city: str, token: str):
        url = BASE_WEATHER_API_LINK.format(city=city, token=token)
        session = await self.get_session()
        response = await session.get(url)

        if not response.ok:
            raise WeatherAPIError(
                "Something went wrong, response from "
                "open.weather is not successful. "
                f"Response: {response}"
            )

        json_response = await response.json()
        weather = json_response['weather'][0]
        temp = int(json_response['main']['temp'] - 273.15)
        delta_timezone = dt.timedelta(seconds=json_response['timezone'])
        now = dt.datetime.now() + delta_timezone
        city = json_response['name']
        weather = weather['description']
        temp = f'+{temp}°' if temp > 0 else f'{temp}°'

        data = {
            'time': now.strftime('%H:%M'),
            'weather': weather,
            'city': city,
            'temp': temp,
        }
        return data

    async def get_session(self) -> aiohttp.ClientSession:
        if self._session is None:
            new_session = aiohttp.ClientSession()
            self._session = new_session
        return self._session

    async def close(self) -> None:
        if self._session is None:
            return None
        await self._session.close()
