import requests
from setting_secret import *

def fetch_weather_data():




def weather():
    url = ("https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&exclude=minutely,hourly" % (LAT,
                                                                                                               LON,
                                                                                                               OPEN_WEATHER_API_KEY))

    response = requests.get(url)
    print(response.text)


def weather_menu_json():
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
                                    "text": "現在の天気"
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
    weather()
