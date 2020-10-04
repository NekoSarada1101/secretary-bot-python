def theme_json() -> dict:
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
                            "text": "カラーテーマのメインの色を選択してください",
                        },
                        "accessory": {
                            "type": "static_select",
                            "action_id": "select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select a color",
                            },
                            "options": [
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Red",
                                    },
                                    "value": "red",
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Orange",
                                    },
                                    "value": "orange",
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Yellow",
                                    },
                                    "value": "yellow",
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Green",
                                    },
                                    "value": "green",
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Blue",
                                    },
                                    "value": "blue",
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Black",
                                    },
                                    "value": "black",
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "White",
                                    },
                                    "value": "white",
                                },
                            ],
                        },
                    },
                ],
            },
        ],
    }
    return data


def theme_list_json(select_value: str) -> dict:
    fallback = ""  # type: str
    color = ""  # type: str
    textAndValue1 = ""  # type: str
    textAndValue2 = ""  # type: str
    textAndValue3 = ""  # type: str
    textAndValue4 = ""  # type: str
    textAndValue5 = ""  # type: str

    if select_value == "red":
        fallback = "赤"
        color = "FF0000"
        textAndValue1 = "Arizona State University"
        textAndValue2 = "Big Red"
        textAndValue3 = "Kansas City Chiefs"
        textAndValue4 = "Laravel"
        textAndValue5 = "Polygon"

    elif select_value == "orange":
        fallback = "橙"
        color = "EF810F"
        textAndValue1 = "FOLIO orange"
        textAndValue2 = "Halloween"
        textAndValue3 = "Kimbie"
        textAndValue4 = "osTicket"
        textAndValue5 = "University Of Texas"

    elif select_value == "yellow":
        fallback = "黄"
        color = "FFFF00"
        textAndValue1 = "Gruvbox Light Medium"
        textAndValue2 = "JavaScript"
        textAndValue3 = "ill Bill"
        textAndValue4 = "KKTOWN"
        textAndValue5 = "Put.io"

    elif select_value == "green":
        fallback = "緑"
        color = "00FF00"
        textAndValue1 = "Autumn"
        textAndValue2 = "Christmas"
        textAndValue3 = "Drupal Twig"
        textAndValue4 = "Forest"
        textAndValue5 = "Starbucks"

    elif select_value == "blue":
        fallback = "青"
        color = "3300ff"
        textAndValue1 = "Dropbox"
        textAndValue2 = "PlayStation"
        textAndValue3 = "Python"
        textAndValue4 = "Trello"
        textAndValue5 = "Twitter"

    elif select_value == "black":
        fallback = "黒"
        color = "000000"
        textAndValue1 = "Film Noir"
        textAndValue2 = "GitKraken"
        textAndValue3 = "Ingress Enlightened"
        textAndValue4 = "Solarized Dark"
        textAndValue5 = "Terminal"

    elif select_value == "white":
        fallback = "白"
        color = "ffffff"
        textAndValue1 = "Github"
        textAndValue2 = "macOs"
        textAndValue3 = "Skype"
        textAndValue4 = "Solarized"
        textAndValue5 = "Youtube"

    data = {
        "response_type": "ephemeral",
        "attachments": [
            {
                "callback_id": "button",
                "text": "適用するカラーテーマを選択してください",
                "fallback": fallback,
                "color": color,
                "attachment_type": "default",
                "actions": [
                    {
                        "name": "theme",
                        "text": textAndValue1,
                        "type": "button",
                        "value": textAndValue1,
                    },
                    {
                        "name": "theme",
                        "text": textAndValue2,
                        "type": "button",
                        "value": textAndValue2,
                    },
                    {
                        "name": "theme",
                        "text": textAndValue3,
                        "type": "button",
                        "value": textAndValue3,
                    },
                    {
                        "name": "theme",
                        "text": textAndValue4,
                        "type": "button",
                        "value": textAndValue4,
                    },
                    {
                        "name": "theme",
                        "text": textAndValue5,
                        "type": "button",
                        "value": textAndValue5,
                    },
                ],
            },
        ],
    }
    return data


def theme_info_json(value: str) -> dict:
    text = ""  # type: str
    title = ""  # type: str
    color = ""  # type: str
    image = ""  # type: str

    if value == "Arizona State University":
        text = "#8C1D40,#5C6670,#FFC627,#FFFFFF,#5C6670,#FFFFFF,#94E864,#00A3E0"
        title = "Arizona State University"
        color = "8C1D40"
        image = "https://drive.google.com/uc?id=15wkbxe6Kk6V7xmt8nh1CDYQpctflR9j6"

    elif value == "Big Red":
        text = "#754242,#BD3737,#9C4444,#FFFFFF,#434745,#FFFFFF,#99D04A,#DB6668"
        title = "Big Red"
        color = "754242"
        image = "https://drive.google.com/uc?id=1TdO1GApC_P7_POfd7mo_x7QIGVhn-uBc"

    elif value == "Kansas City Chiefs":
        text = "#B51815,#A51815,#FFFFFF,#B51815,#FF1815,#FFD21F,#FFE21F,#FF5555"
        title = "Kansas City Chiefs"
        color = "B51815"
        image = "https://drive.google.com/uc?id=1zngOXScJo9LE0MK-i5O40FTSdqxR08b3"

    elif value == "Laravel":
        text = "#F56262,#F56262,#424242,#F5F5F5,#ed5151,#F5F5F5,#F5F5F5,#424242"
        title = "Laravel"
        color = "F56262"
        image = "https://drive.google.com/uc?id=1mT9D9rjN2VVEttacVdZl_2ugiagtXPh2"

    elif value == "Polygon":
        text = "#C10048,#920A3D,#2E0002,#FFFFFF,#610A29,#FFFFFF,#FFFFFF,#610A29"
        title = "Polygon"
        color = "C10048"
        image = "https://drive.google.com/uc?id=1xk5cZBJ0uzWhY7HCbKz3lKdWNLZcRjeA"

    elif value == "FOLIO orange":
        text = "#DA6A2D,#737272,#38307F,#FFFFFF,#737272,#FFFFFF,#38307F,#38307F"
        title = "FOLIO orange"
        color = "DA6A2D"
        image = "https://drive.google.com/uc?id=18hHd8YkR37ni-cRugPLnMdd4OWQFkU3b"

    elif value == "Halloween":
        text = "#ff8800,#000000,#ffffff,#000000,#4a5664,#000000,#000000,#736e65"
        title = "Halloween"
        color = "ff8800"
        image = "https://drive.google.com/uc?id=1yyfu6qOcEZG3K0oOANDYOk2YCglZ3rOa"

    elif value == "Kimbie":
        text = "#F3E3CD,#F3E3CD,#F3951D,#DA3D61,#F26328,#183E1C,#DA3D61,#F26328"
        title = "Kimbie"
        color = "F3E3CD"
        image = "https://drive.google.com/uc?id=1vdYF6oyk3FNuoj0Y3LPOsjYkCGSBtoUt"

    elif value == "osTicket":
        text = "#F68D29,#F99A3F,#F99A3F,#FFFFFF,#ED8624,#FFFFFF,#FFFFFF,#F9A55A"
        title = "osTicket"
        color = "F68D29"
        image = "https://drive.google.com/uc?id=12dQG42-oEO93pplNBbiVheD9R7eBrvC_"

    elif value == "University Of Texas":
        text = "#BF5700,#333F48,#FFFFFF,#333F48,#333F48,#FFFFFF,#94E864,#00A3E0"
        title = "University Of Texas"
        color = "BF5700"
        image = "https://drive.google.com/uc?id=1BU5ytajAMzLAF9DaCMdgW_eH1u2-JNoj"

    elif value == "Gruvbox Light Medium":
        text = "#FBF1C7,#EBDBB2,#79740E,#ffffff,#D5C4A1,#3C3836,#8F3F71,#076678"
        title = "FBF1C7"
        color = "Gruvbox Light Medium"
        image = "https://drive.google.com/uc?id=1Rk_Mtlz1gjOxoBRiYvFy3848tA4BldBh"

    elif value == "JavaScript":
        text = "#F0DB4F,#F0DB4F,#323330,#FFFFFF,#e6cd2c,#323330,#323330,#323330"
        title = "JavaScript"
        color = "F0DB4F"
        image = "https://drive.google.com/uc?id=1zwwT3pGDF8YJjtzdxbsmPsheySrWkYR6"

    elif value == "Kill Bill":
        text = "#FDE13A,#FDE13A,#000000,#E72D25,#FFF09E,#000000,#E72D25,#E72D25"
        title = "Kill Bill"
        color = "FDE13A"
        image = "https://drive.google.com/uc?id=1oM2D02e9gFfhDAb47xtuy1et8UHlEJNO"

    elif value == "KKTOWN":
        text = "#FFD552,#FFffff,#FFffff,#30322A,#ECEEF2,#30322A,#17B5DA,#17B5DA"
        title = "KKTOWN"
        color = "FFD552"
        image = "https://drive.google.com/uc?id=1Md9G3j0uGcpk7UeBLzqLvjasMCWMKJC_"

    elif value == "Put.io":
        text = "#FFFFFF,#FDCE45,#FDCE45,#0F1216,#ECEEF2,#0F1216,#1FAE7D,#1FAE7D"
        title = "Put.io"
        color = "FFFFFF"
        image = "https://drive.google.com/uc?id=1vXu5IiiULHuK1wPekmvJdnzMqBGS0LR1"

    elif value == "Autumn":
        text = "#194234,#9c2e33,#E7C12e,#194234,#9c2e33,#FFFFFF,#ee6030,#9C2E33"
        title = "Autumn"
        color = "194234"
        image = "https://drive.google.com/uc?id=1GsiXEFdQeqQExYh9vq20IwWsts3LjQ3b"

    elif value == "Christmas":
        text = "#138724,#1B5E48,#db2e3f,#FFFFFF,#2D9A48,#FFFFFF,#1B5E48,#DB2E3F"
        title = "Christmas"
        color = "138724"
        image = "https://drive.google.com/uc?id=1ddwRC4s2mMa4fPuBhwbGVBrKfi8cn9Fp"

    elif value == "Drupal Twig":
        text = "#6fa36f,#3E313C,#01690b,#ffff00,#3E313C,#ffffff,#faff78,#ed687e"
        title = "Drupal Twig"
        color = "6fa36f"
        image = "https://drive.google.com/uc?id=1rTcvTpHZdw_P7Z5-y3VB3M2EmDQH5Lcf"

    elif value == "Forest":
        text = "#033313,#077a07,#02ad44,#FFFFFF,#076e27,#FFFFFF,#94E864,#78AF8F"
        title = "Forest"
        color = "033313"
        image = "https://drive.google.com/uc?id=1GsVvxg2nAlgnfMQ3Mbzfhv-5XXEVR5gl"

    elif value == "Dropbox":
        text = "#007EE5,#007EE5,#47525D,#FFFFFF,#7B8994,#FFFFFF,#47525D,#47525D"
        title = "Dropbox"
        color = "007EE5"
        image = "https://drive.google.com/uc?id=1DTscePwMDppd8WFOkZeJDHI9ndnwnpQi"

    elif value == "PlayStation":
        text = "#173f85,#0072CE,#0072ce,#FFFFFF,#0072CE,#FFFFFF,#FFDA00,#FFDA00"
        title = "PlayStation"
        color = "173f85"
        image = "https://drive.google.com/uc?id=1ZzgKoHSXxU0Z0tC-qRph3_EV2xK51dJl"

    elif value == "Python":
        text = "#306998,#FFD43B,#FFD43B,#7F7F7F,#5A9FD4,#F4F4F4,#FFE873,#FFD43B"
        title = "Python"
        color = "306998"
        image = "https://drive.google.com/uc?id=1gvOXI0NWfjFKzj75xR3X0m2thGUZ0v_Q"

    elif value == "Trello":
        text = "#0079BF,#026AA7,#5BA4CF,#FFFFFF,#026AA7,#FFFFFF,#61BD4F,#EB5A46"
        title = "Trello"
        color = "0079BF"
        image = "https://drive.google.com/uc?id=1veKHgfLU8VsenWAzcZm6-8xrF9Jv7JjB"

    elif value == "Twitter":
        text = "#55ACEE,#55ACEE,#E1E8ED,#292F33,#ADDCFF,#F5F8FA,#E1E8ED,#E1E8ED"
        title = "Twitter"
        color = "55ACEE"
        image = "https://drive.google.com/uc?id=1bo9zdpxee5wURK5OCrquapJx6373jid2"

    elif value == "Film Noir":
        text = "#101010,#101010,#D3D3CA,#BB313E,#424242,#F0F0E6,#BB313E,#BB313E"
        title = "Film Noir"
        color = "101010"
        image = "https://drive.google.com/uc?id=1ZzQeOoCvcvL2dHhujLDWHgs84kVtHrrp"

    elif value == "GitKraken":
        text = "#141422,#259692,#259692,#FFFFFF,#4A5664,#ffffff,#ff8800,#FF8800"
        title = "GitKraken"
        color = "141422"
        image = "https://drive.google.com/uc?id=1MlafeF0XrMduxrHQJ9iSf1jts-oZ1Fvb"

    elif value == "Ingress Enlightened":
        text = "#000E0F,#000E0F,#393218,#F1C248,#006D77,#34EAF5,#02BF02,#F1C248"
        title = "Ingress Enlightened"
        color = "000E0F"
        image = "https://drive.google.com/uc?id=1t9of7jbV4Pkw69Jfc2MOSmbiyWzMpZFR"

    elif value == "Solarized Dark":
        text = "#073642,#002B36,#B58900,#FDF6E3,#CB4B16,#FDF6E3,#2AA198,#DC322F"
        title = "Solarized Dark"
        color = "073642"
        image = "https://drive.google.com/uc?id=1PkM8HIP17MeXIj_-a7pKHJuz5dvgjFAW"

    elif value == "Terminal":
        text = "#101010,#000000,#FFFFFF,#000000,#A0A0A0,#FFFFFF,#00A400,#5858FE"
        title = "Terminal"
        color = "101010"
        image = "https://drive.google.com/uc?id=1rp3XLGOEIqraCQ5jBVtZiNbfI0VfIu-z"

    elif value == "Github":
        text = "#ffffff,#24292e,#e9f0f7,#1d4880,#ffefc6,#666666,#28a745,#92979b"
        title = "Github"
        color = "ffffff"
        image = "https://drive.google.com/uc?id=1-NOoauO3W6oQDpn0PRNpeyjBl47UVGR6"

    elif value == "macOs":
        text = "#F1F3F5,#DAD8DA,#D3DFE3,#303030,#C2E2ED,#303030,#1682FB,#34C749"
        title = "macOs"
        color = "F1F3F5"
        image = "https://drive.google.com/uc?id=16hXZxqN0C0CVO90DSaJqSVA6Qv7thGZs"

    elif value == "Skype":
        text = "#F0F4F8,#39B1DF,#C7EDFC,#000000,#F0F4F8,#000000,#7FBA00,#FF8C00"
        title = "Skype"
        color = "F0F4F8"
        image = "https://drive.google.com/uc?id=1eluaP79JqLcNn28fuGT2EAuZhMnHMFBL"

    elif value == "Solarized":
        text = "#FDF6E3,#EEE8D5,#93A1A1,#FDF6E3,#EEE8D5,#657B83,#2AA198,#DC322F"
        title = "Solarized"
        color = "FDF6E3"
        image = "https://drive.google.com/uc?id=1mOKLMMB-yU8pXPHy688rW9uaXQdmP68T"

    elif value == "Youtube":
        text = "#FFFFFF,#CC181E,#CC181E,#FFFFFF,#444444,#0D0D0D,#CC181E,#E04A4D"
        title = "Youtube"
        color = "FFFFFF"
        image = "https://drive.google.com/uc?id=1vz1YdRAbe85gd1Myk7tnxFIGEO5UBoqp"

    data = {  # type: dict
        "text": text,
        "response_type": "ephemeral",
        "attachments": [
            {
                "title": title,
                "color": color,
                "image_url": image,
            },
        ],
    }
    return data
