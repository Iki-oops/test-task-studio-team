import datetime as dt

from pydantic import BaseModel, field_validator


class Weather(BaseModel):
    city: str
    weather: str
    temp: float | str
    time: int | str

    @field_validator('temp')
    def temp_validator(cls, value: int):
        temp = round(value - 273.15)
        return f'+{temp}°' if temp > 0 else f'{temp}°'

    @field_validator('time')
    def time_validator(cls, value: int):
        delta_timezone = dt.timedelta(seconds=value)
        now = dt.datetime.utcnow() + delta_timezone
        return now.strftime('%H:%M')


class News(BaseModel):
    title: str
    text: str | None
    url: str
    image: str | None
    publish_date: str

    @field_validator('text')
    def text_validator(cls, value: str | None):
        return value if value else 'Нет описании'

    @field_validator('image')
    def image_validator(cls, value: str | None):
        return value if value else 'https://i.ibb.co/bPQrwGd/image-not-found.jpg'
