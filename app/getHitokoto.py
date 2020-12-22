import requests
import json

class getHitokoto:

    def __init__(self):
        self.url = 'https://v1.hitokoto.cn/'

    def run(self):
        r = requests.get(self.url)
        s = json.loads(r.text)
        hitokoto = s['hitokoto'] + ' 「 '+s['from']+ ' 」'
        return hitokoto


