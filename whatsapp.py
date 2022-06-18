import json
from time import sleep
import requests
import os

from_num = os.environ.get("FROM_PHONE_NUM_ID")
to_num = os.environ.get("TO_PHONE_NUM_ID")

api_endpoint = f"https://graph.facebook.com/v14.0/{from_num}/messages"
access_token = os.environ.get("ACESS_TOKEN_WHATSAPP")

headers = {"Authorization": f"Bearer {access_token}"}


def send_alert(gid: int) -> None:
    with open("json/alerta.json", "r") as f:
        data = json.load(f)
    
    data['to'] = to_num
    data['text']['body'] = f"10+ news change on guild id: \"{gid}\", please verify."

    requests.post(api_endpoint, json=data, headers=headers)


def send_news(news: list) -> None:
    with open("json/noticia.json", "r") as f:
        data = json.load(f)
    
    data['to'] = to_num
    components = data['template']['components']

    for n in news:
        components[0]['parameters'][0]['image']['link'] = n.thumbnail
        components[1]['parameters'][0]['text'] = n.title
        components[1]['parameters'][1]['text'] = n.description
        components[2]['parameters'][0]['text'] = n.link.split('/')[-1]

        data['template']['components'] = components

        r = requests.post(api_endpoint, json=data, headers=headers)
        sleep(10)
