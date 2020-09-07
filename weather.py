import requests
from setting_secret import *


def weather():
    url = ("https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&exclude=minutely,hourly" % (LAT,
                                                                                                               LON,
                                                                                                               OPEN_WEATHER_API_KEY))

    response = requests.get(url)
    print(response.text)


if __name__ == "__main__":
    weather()
