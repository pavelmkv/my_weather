from datetime import datetime
from enum import Enum
from typing import NamedTuple

from coordinates import Coordinates

Celsius = int


class WeatherType(Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморозь"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordinates: Coordinates) -> Weather:
    return Weather(
        temperature=20,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat("2023-17-04 04:00:00"),
        sunset=datetime.fromisoformat("2023-17-04 20:20:00"),
        city="SPB"
    )

