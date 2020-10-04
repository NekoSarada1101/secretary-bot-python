from datetime import datetime, timedelta, timezone
import google_calendar
import weather
import notification_events
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

    # 技術イベント通知
    connpass_data = notification_events.fetch_tech_events("https://connpass.com/explore/ja.atom")  # type: dict
    techplay_data = notification_events.fetch_tech_events("https://rss.techplay.jp/event/w3c-rss-format/rss.xml")  # type: dict

    print(weather_data)
    json_data = json.dumps(weather_data).encode("utf-8")  # type json
    requests.post(DIARY_URL, json_data)
    print(calendar_data)
    json_data = json.dumps(calendar_data).encode("utf-8")
    requests.post(DIARY_URL, json_data)
    print(connpass_data)
    json_data = json.dumps(connpass_data).encode("utf-8")
    requests.post(TECH_EVENT_URL, json_data)
    print(techplay_data)
    json_data = json.dumps(techplay_data).encode("utf-8")
    requests.post(TECH_EVENT_URL, json_data)
    return ""
