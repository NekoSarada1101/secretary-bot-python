from setting_secret import *
import google_calendar
import weather
import json
import requests
from datetime import datetime, timedelta, timezone


def do_post(e: requests) -> str:
    token = e.form.get('token')  # type: str
    payload = {}  # type: dict
    try:
        payload = json.loads(e.form.get("payload"))
    except TypeError as error:
        print(error)

    # 認証
    if token != SLACK_TOKEN and payload['token'] != SLACK_TOKEN:
        raise Exception("not allowed token")

    data = {}  # type: dict
    # Slack上で最初に表示する
    if token == SLACK_TOKEN:
        data = menu_json()
    else:  # Slack上でメニューの操作がされた時
        value = ""  # type: str
        action_id = ""  # type: str
        # valueの取得、判定
        try:
            value = payload["actions"][0]["value"]
            print(value)
        except KeyError as error:
            print(error)

        if value == "calendar":
            data = google_calendar.date_pick_json()
        elif value == "weather":
            data = weather.weather_menu_json()
        elif value == "weatherToday":
            data = weather.fetch_weather_data("today")
        elif value == "weatherTomorrow":
            data = weather.fetch_weather_data("tomorrow")
        elif value == "weatherWeek":
            data = weather.fetch_weather_data("week")

        # action_idの取得、判定
        try:
            action_id = payload['actions'][0]['action_id']
            print(action_id)
        except KeyError as error:
            print(error)

        if action_id == "date":
            today = datetime.now(timezone(timedelta(hours=+9), 'JST'))  # type: datetime
            pick_date = datetime.strptime(payload["actions"][0]["selected_date"], "%Y-%m-%d")  # type: datetime
            pick_date = today.replace(year=pick_date.year, month=pick_date.month, day=pick_date.day)
            data = google_calendar.fetch_day_calendar_data(pick_date)

    print(data)
    json_data = json.dumps(data).encode("utf-8")  # type: json
    requests.post(HISHO_URL, json_data)
    return ""


def menu_json() -> dict:
    data = {  # type: dict
        "response_type": "ephemeral",
        "attachments": [
            {
                "color": "FFFFFF",
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "plain_text",
                            "text": "何かご用でしょうか？",
                        }
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "予定を教えて"
                                },
                                "value": "calendar"
                            },
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "天気を教えて"
                                },
                                "value": "weather"
                            },
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "テーマを変えたい"
                                },
                                "value": "theme"
                            }
                        ]
                    }
                ]
            }
        ]
    }
    return data
