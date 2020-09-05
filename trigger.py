from datetime import datetime, timedelta, timezone
import google_calendar
import json
import requests
import base64
from setting_secret import *


def morning_trigger(event, context):
    if 'data' in event:
        frequency = base64.b64decode(event['data']).decode('utf-8')
    else:
        frequency = None

    JST = timezone(timedelta(hours=+9), 'JST')
    today = datetime.now(JST)

    if frequency == "day":
        data = google_calendar.fetch_day_calendar_data(today)

    elif frequency == "week":
        data = google_calendar.fetch_week_calendar_data(today)

    json_data = json.dumps(data).encode("utf-8")
    requests.post(DIARY_URL, json_data)
    return ""


if __name__ == '__main__':
    morning_trigger()
