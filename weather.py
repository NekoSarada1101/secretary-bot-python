import requests
import json
from datetime import datetime
from typing import List
from setting_secret import *


def fetch_weather_data(when: str) -> dict:
    url = ("https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&exclude=current,minutely,"
           "hourly&lang=ja&units=metric" % (
               LAT,
               LON,
               OPEN_WEATHER_API_KEY))  # type: str
    response = json.loads(requests.get(url).text)  # type: dict

    index = []  # type: List[int]
    if when == "today":
        index = [0]
    elif when == "tomorrow":
        index = [1]
    elif when == "week":
        index = [0, 1, 2, 3, 4, 5, 6, 7]

    dt = []  # type: List[str]
    weather = []  # type: List[str]
    image = []  # type: List[str]
    day_temp = []  # type: List[str]
    max_temp = []  # type: List[str]
    min_temp = []  # type: List[str]
    wind_speed = []  # type: List[str]
    pop = []  # type: List[str]
    for i in index:
        weather.append(response["daily"][i]["weather"][0]["description"])
        image.append(response["daily"][i]["weather"][0]["icon"])

        if when == "today" or when == "tomorrow":
            max_temp.append(str(round(response["daily"][i]["temp"]["max"], 1)) + "°C")
            min_temp.append(str(round(response["daily"][i]["temp"]["min"], 1)) + "°C")
            wind_speed.append(str(response["daily"][i]["wind_speed"]) + "m/h")
            pop.append(str(int(response["daily"][i]["pop"] * 100)) + "%")

        elif when == "week":
            dt.append(datetime.fromtimestamp(response["daily"][i]["dt"]).strftime("%m/%d"))
            day_temp.append(str(round(response["daily"][i]["temp"]["day"], 1)) + "°C")

    data = {}  # type: dict
    if when == "today":
        data = day_weather_json("今日", weather, image, max_temp, min_temp, wind_speed, pop)
    elif when == "tomorrow":
        data = day_weather_json("明日", weather, image, max_temp, min_temp, wind_speed, pop)
    elif when == "week":
        data = week_weather_json(dt, weather, day_temp)

    return data


def day_weather_json(dt: str, weather: List[str], image: List[str], max_temp: List[str], min_temp: List[str],
                     wind_speed: List[str], pop: List[str]) -> dict:
    data = {
        "response_type": "ephemeral",
        "text": dt + "の天気をお知らせします。",
        "attachments": [
            {
                "text": "*" + dt + "の天気* ： `" + weather[0] + "`",
                "color": "33ff66",
                "image_url": "http://openweathermap.org/img/wn/" + image[0] + "@2x.png"
            },
            {
                "color": "FF0000",
                "text": " *最高気温* ： `" + max_temp[0] + "`"
            },
            {
                "color": "00BFFF",
                "text": " *最低気温* ： `" + min_temp[0] + "`"
            },
            {
                "color": "FFFFFF",
                "text": " *風速* 　　： `" + wind_speed[0] + "`"
            },
            {
                "color": "5579EC",
                "text": " *降水確率* ： `" + pop[0] + "`"
            }
        ]
    }
    return data


def week_weather_json(dt: List[str], weather: List[str], day_temp: List[str]) -> dict:
    attachments = []  # type: List[dict]
    for i in range(len(dt)):
        attachments.append({"text": " *" + dt[i] + "の天気* ： `" + weather[i] + "`  *気温* ： `" + day_temp[i] + "`",
                            "color": "FFFFFF"})

    data = {  # type: dict
        "response_type": "ephemeral",
        "attachments":
            attachments
    }
    return data


def weather_menu_json() -> dict:
    data = {
        "response_type": "ephemeral",
        "attachments": [
            {
                "color": "FFFFFF",
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "plain_text",
                            "text": "いつの天気を確認しますか？",
                        }
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "今日の天気"
                                },
                                "value": "weatherToday"
                            },
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "明日の天気"
                                },
                                "value": "weatherTomorrow"
                            },
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "1週間の天気"
                                },
                                "value": "weatherWeek"
                            }
                        ]
                    }
                ]
            }
        ]}
    return data


if __name__ == "__main__":
    data_json = fetch_weather_data("week")
    print(data_json)
