from io import BytesIO
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from tgbot.services.types import Weather


def generate_weather_image(background_path: str, data: Weather):
    color = (255, 255, 255)
    root = Path().resolve()
    font_path = str(Path(root, 'static/fonts/Oswald-Medium.ttf'))

    background_image = Image.open(background_path)

    draw = ImageDraw.Draw(background_image)
    font = ImageFont.truetype(font_path)
    font_temp = font.font_variant(size=82)
    font_weather = font.font_variant(size=24)
    font_city = font.font_variant(size=48)
    font_time = font.font_variant(size=48)

    background_width, background_height = background_image.size
    temp_width, temp_height = font_temp.getsize(data.temp)
    weather_width, weather_height = font_weather.getsize(data.weather)
    city_width, city_height = font_city.getsize(data.city)
    time_width, time_height = font_time.getsize(data.time)
    left_space = (temp_width - weather_width + 30) // 2

    if left_space < 10:
        left_space = 10

    draw.text((30, 0), data.temp, color, font=font_temp)
    draw.text((left_space, temp_height), data.weather, color, font=font_weather)
    draw.text((20, background_height - city_height - 20), data.city, color, font=font_city)
    draw.text(
        (background_width - time_width - 20, background_height - time_height - 20),
        data.time,
        color,
        font=font_time
    )

    bio = BytesIO()
    bio.name = 'image.png'
    background_image.save(bio, 'PNG')
    bio.seek(0)

    return bio
