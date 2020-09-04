from datetime import datetime, timedelta, timezone
import google_calendar
import json
import requests
from setting_secret import *


def morning_trigger(event, context):
    JST = timezone(timedelta(hours=+9), 'JST')
    today = datetime.now(JST)

    data = google_calendar.fetch_all_calendar_data(today)

    json_data = json.dumps(data).encode("utf-8")
    requests.post(DIARY_URL, json_data)
    return ""


if __name__ == '__main__':
    morning_trigger()
