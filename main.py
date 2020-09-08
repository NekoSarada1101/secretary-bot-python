from setting_secret import *
import google_calendar
import weather
import json
import requests
from datetime import datetime, timedelta, timezone


def do_post(e):
    token = e.form.get('token')
    payload = None
    try:
        payload = json.loads(e.form.get("payload"))
    except TypeError as error:
        print(error)

    if token != SLACK_TOKEN and payload['token'] != SLACK_TOKEN:
        raise Exception("not allowed token")

    if token == SLACK_TOKEN:
        data = menu_json()

    else:
        value = None
        action_id = None
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
            today = datetime.now(timezone(timedelta(hours=+9), 'JST'))
            pick_date = datetime.strptime(payload["actions"][0]["selected_date"], "%Y-%m-%d")
            pick_date = today.replace(year=pick_date.year, month=pick_date.month, day=pick_date.day)
            data = google_calendar.fetch_day_calendar_data(pick_date)

    json_data = json.dumps(data).encode("utf-8")
    print(data)
    requests.post(HISHO_URL, json_data)
    return ""


def menu_json():
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
