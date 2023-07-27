import random
from typing import Optional

import aiohttp

from tgbot.services.config import BASE_WEATHER_API_LINK, BASE_NEWS_API_LINK
from tgbot.services.exceptions import (
    WeatherAPIError,
    NewsAPIError,
    TooManyRequestsAPIError,
)
from tgbot.services.types import Weather, News


class AiohttpService:
    DEFAULT_LANG = 'ru'
    DEFAULT_LIMIT = 10

    def __init__(self):
        self._session: Optional[aiohttp.ClientSession] = None

    async def get_weather(self, city: str, token: str) -> Weather:
        url = BASE_WEATHER_API_LINK.format(city=city, token=token)
        session = await self.get_session()
        response = await session.get(url)

        if response.status == 429 or response.status == 402:
            raise TooManyRequestsAPIError(f'Too Many Requests. Response: {response}')
        elif not response.ok:
            raise WeatherAPIError(
                "Something went wrong, response from "
                "open.weather is not successful. "
                f"Response: {response}"
            )

        json_response = await response.json()
        weather = Weather.model_validate({
            'city': json_response['name'],
            'weather': json_response['weather'][0]['description'],
            'temp': json_response['main']['temp'],
            'time': json_response['timezone'],
        })

        return weather

    async def get_news(self, token: str) -> News:
        url = BASE_NEWS_API_LINK.format(
            language=self.DEFAULT_LANG,
            offset=random.randint(0, 1000),
            limit=self.DEFAULT_LIMIT,
            token=token
        )
        session = await self.get_session()
        response = await session.get(url)

        if response.status == 429 or response.status == 402:
            raise TooManyRequestsAPIError(f'Too Many Requests. Response: {response}')
        elif not response.ok:
            raise NewsAPIError(
                "Something went wrong, response from "
                "https://worldnewsapi.com is not successful. "
                f"Response: {response}"
            )

        json_response = await response.json()
        news = random.choice(json_response['news'])
        text = news['text']

        for i in range(800, len(text)):
            if text[i] == ' ' and text[i-1].isalpha():
                text = f'{text[:i]}...'
                break
            if text[i] in ('.', '!', '?'):
                text = text[:i+1]
                break

        news = News.model_validate({
            'title': news['title'],
            'text': text,
            'url': news['url'],
            'image': news['image'],
            'publish_date': news['publish_date'],
        })

        return news

    async def get_session(self) -> aiohttp.ClientSession:
        if self._session is None:
            new_session = aiohttp.ClientSession()
            self._session = new_session
        return self._session

    async def close(self) -> None:
        if self._session is None:
            return None
        await self._session.close()
