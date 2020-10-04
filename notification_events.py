import feedparser
import gspread
import random
from typing import List
from setting_secret import *


def connect_gspread():
    gc = gspread.authorize(CREDENTIALS)
    worksheet = gc.open_by_key(SPREAD_SHEET_KEY).sheet1
    return worksheet


def fetch_tech_events(url: str) -> dict:
    ws = connect_gspread()
    i = 1  # type: int
    search_words = []  # type: List[str]

    # spread sheetに書き込んだ検索ワードを取得
    while True:
        word = ws.cell(i, 1).value  # type: str
        if word == "":
            break
        search_words.append(word)
        i += 1

    dic = feedparser.parse(url)  # type: dict
    attachments = []  # type: List[dict]
    for entry in dic.entries:
        title = entry.title  # type: str
        contain_word = [i for i in search_words if i in title]  # type: list
        if len(contain_word) > 0:
            summary = entry.summary  # type: str
            time = ""  # type: str
            place = ""  # type: str
            if "connpass" in url:
                time = summary[summary.find("日時"):summary.find("<")]
                place = summary[summary.find("場所"):summary.find("<", summary.find("場所"))]
            elif "techplay" in url:
                time = summary[summary.find("日時"):summary.find(" ", summary.find("日時"))]
                place = summary[summary.find("会場"):len(summary)]
            link = entry.link  # type: str
            rc = lambda: random.randint(0, 255)
            attachments.append({"text": " *" + title + "* \n" + time + "\n" + place + "\n" + link, "color": '#{:X}{:X}{:X}'.format(rc(), rc(), rc())})

    data = {  # type: dict
        "response_type": "ephemeral",
        "attachments":
            attachments
    }
    return data
