import googleapiclient.discovery
from datetime import datetime, timedelta, timezone
from typing import List

from setting_secret import *


def fetch_day_calendar_data(date: datetime) -> dict:
    period = create_day_period(date)  # type: List[str]
    calendar_data = fetch_all_calendar_events(period)  # type: List[str]
    data = calendar_json(calendar_data, date.strftime("%m月%d日"))  # type: dict
    return data


def create_day_period(date: datetime) -> List[str]:
    time_min = date.replace(hour=0, minute=0, second=0).strftime("%Y-%m-%dT%H:%M:%S%z")  # type: str
    time_max = date.replace(hour=23, minute=59, second=59).strftime("%Y-%m-%dT%H:%M:%S%z")  # type: str
    return [time_min, time_max]


def fetch_week_calendar_data(date: datetime) -> dict:
    period = create_week_period(date)  # type: List[str]
    calendar_data = fetch_all_calendar_events(period)  # type: List[str]
    data = calendar_json(calendar_data, "今週")  # type: dict
    return data


def create_week_period(date: datetime) -> List[str]:
    time_min = date.replace(hour=0, minute=0, second=0).strftime("%Y-%m-%dT%H:%M:%S%z")  # type: str
    time_max = (date.replace(hour=23, minute=59, second=59) +
                timedelta(days=6)).strftime("%Y-%m-%dT%H:%M:%S%z")  # type: str
    return [time_min, time_max]


def fetch_all_calendar_events(period) -> List[str]:
    my_cal = fetch_events(MY_MAIL, period)  # type: str
    work_cal = fetch_events(WORK_MAIL, period)  # type: str
    school_cal = fetch_events(SCHOOL_MAIL, period)  # type: str
    timetable_cal = fetch_events(TIMETABLE_MAIL, period)  # type: str
    return [my_cal, work_cal, school_cal, timetable_cal]


def fetch_events(calendar_id: str, period: List[str]) -> str:
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=CREDENTIALS)

    time_min = period[0]  # type: str
    time_max = period[1]  # type: str

    page_token = None
    while True:
        events = service.events().list(calendarId=calendar_id, pageToken=page_token, timeMin=time_min, timeMax=time_max,
                                       singleEvents=True, orderBy="startTime").execute()  # type: dict
        list_text = ""  # type: str
        for event in events['items']:
            start = event['start'].get('dateTime', event['start'].get('date'))  # type: str

            word_count = 10  # type: int
            if len(start) == word_count:
                start = datetime.strptime(start, "%Y-%m-%d").strftime("%m/%d ")
                list_text += start
            else:
                start = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S%z").strftime("%m/%d  %H:%M-")
                end = event['end'].get('dateTime', event['end'].get('date'))  # type: str
                end = datetime.strptime(end, "%Y-%m-%dT%H:%M:%S%z").strftime("%H:%M ")
                list_text += start + end

            list_text += "`" + event['summary'] + "`" + "\n"

        page_token = events.get('nextPageToken')
        if page_token is None:
            break

    return list_text


def calendar_json(calendar_data: List[str], today: str) -> dict:
    my_cal = calendar_data[0]  # type: str
    work_cal = calendar_data[1]  # type: str
    school_cal = calendar_data[2]  # type: str
    timetable_cal = calendar_data[3]  # type: str
    data = {  # type: dict
        "response_type": "ephemeral",
        "text": today + "の予定をお知らせします。",
        "attachments": [
            {
                "fallback": "my",
                "color": "FF0000",
                "title": "自分の予定",
                "text": my_cal
            },
            {
                "fallback": "recruit",
                "color": "00BFFF",
                "title": "仕事の予定",
                "text": work_cal
            },
            {
                "fallback": "school",
                "color": "FFFF00",
                "title": "学校の予定",
                "text": school_cal
            },
            {
                "fallback": "timetable",
                "color": "FFFFFF",
                "title": "時間割の予定",
                "text": timetable_cal
            }
        ]
    }
    return data


def date_pick_json() -> dict:
    today = datetime.now(timezone(timedelta(hours=+9), 'JST')).strftime("%Y-%m-%d")  # type: str
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
                            "text": "何日の予定を確認しますか？",
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "plain_text",
                            "text": "予定を確認したい日付を選択してください"
                        },
                        "accessory": {
                            "type": "datepicker",
                            "initial_date": today,
                            "action_id": "date",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select a date",
                            }
                        }
                    }
                ]
            }
        ]
    }
    return data
