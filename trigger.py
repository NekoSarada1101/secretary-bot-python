from datetime import datetime, timedelta, timezone
import google_calendar
import weather
import json
import requests
import base64
from setting_secret import *


def morning_trigger(event: dict, context) -> str:
    if 'data' in event:
        frequency = base64.b64decode(event['data']).decode('utf-8')  # type: str
    else:
        frequency = ""

    today = datetime.now(timezone(timedelta(hours=+9), 'JST'))  # type: datetime

    calendar_data = {}  # type: dict
    if frequency == "day":  # 今日の予定
        calendar_data = google_calendar.fetch_day_calendar_data(today)
    elif frequency == "week":  # 1週間の予定
        calendar_data = google_calendar.fetch_week_calendar_data(today)

    # 今日の天気
    weather_data = weather.fetch_weather_data("today")  # type: dict

    json_data = json.dumps(calendar_data).encode("utf-8")  # type json
    requests.post(DIARY_URL, json_data)
    json_data = json.dumps(weather_data).encode("utf-8")
    requests.post(DIARY_URL, json_data)
    return ""
