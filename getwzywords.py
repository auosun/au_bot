import requests
import json
import time
import random

def getHitokoto():
    r = requests.get('https://v1.hitokoto.cn/')
    s = json.loads(r.text)
    return s["hitokoto"][:random.randint(5,len(s["hitokoto"]))]

def getwzywords():
    words = ''
    for i in range(3):
        words = getHitokoto()+","+words
        time.sleep(0.5)
    return words
