class auConfigs():
    def __init__(self):
        # Telegram bot api token
        self.token = 'telegram api token'

        # REQUEST_KWARGS
        self.proxy = {'proxy_url': 'http-proxy',}

        # Baidu voice api
        self.BAIDU_VOICE_API_ID = 'baidu api'
        self.BAIDU_VOICE_API_KEY = 'baidu api'
        self.BAIDU_VOICE_SECRET_KEY = 'baidu api'

        # ffmpeg file address
        self.ffmpeg = 'ffmpeg'

    def get_token(self):
        return self.token