import googleapiclient.discovery
from datetime import datetime, timedelta, timezone
from setting_secret import *


def fetch_day_calendar_data(date):
    period = create_day_period(date)
    calendar_data = fetch_all_calendar(period)
    data = calendar_json(calendar_data, date.strftime("%m月%d日"))
    return data


    return data


def fetch_today_events(calendar_id, date):
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=CREDENTIALS)

    min = date.replace(hour=0, minute=0, second=0).strftime("%Y-%m-%dT%H:%M:%S%z")
    max = date.replace(hour=23, minute=59, second=59).strftime("%Y-%m-%dT%H:%M:%S%z")

    page_token = None
    while True:
        events = service.events().list(calendarId=calendar_id, pageToken=page_token, timeMin=min, timeMax=max,
                                       singleEvents=True, orderBy="startTime").execute()

        list_text = ""
        for event in events['items']:
            start = event['start'].get('dateTime', event['start'].get('date'))

            if len(start) == 10:
                start = datetime.strptime(start, "%Y-%m-%d").strftime("%m/%d ")
                list_text += start
            else:
                start = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S%z").strftime("%m/%d %H:%M-")
                end = event['end'].get('dateTime', event['end'].get('date'))
                end = datetime.strptime(end, "%Y-%m-%dT%H:%M:%S%z").strftime("%H:%M ")
                list_text += start + end

            list_text += "`" + event['summary'] + "`" + "\n"

        page_token = events.get('nextPageToken')
        if not page_token:
            break

    return list_text


def calendar_json(my_cal, work_cal, school_cal, timetable_cal, today):
    data = {
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
                "title": "インターンの予定",
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


def date_pick_json():
    JST = timezone(timedelta(hours=+9), 'JST')
    today = datetime.now(JST).strftime("%Y-%m-%d")
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
